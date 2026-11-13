// Prototipo della riparazione in parallelo di RawLine Space (prova, non prodotto).
// uso: ripara <registro della copia .jsonl> <cartella da controllare> <registro riparazioni> <cartella con altre copie> [altre...]
// 1. Controllo: rilegge in parallelo ogni file e lo confronta con l'impronta registrata alla copia.
// 2. Riparazione: per ogni file danneggiato cerca tra le altre copie una che abbia ESATTAMENTE l'impronta
//    registrata (non basta "diversa da quella rotta"). La copia buona arriva su un nome temporaneo,
//    verificata. Il file danneggiato va in quarantena, mai cancellato. Poi la copia buona prende il suo nome.
// Le altre copie si aprono SOLO in lettura.
import Foundation
import CryptoKit
import Darwin
setvbuf(stdout, nil, _IOLBF, 0)
let a = CommandLine.arguments
let regCopia = a[1], radice = a[2], regRip = a[3], altre = Array(a[4...])
let fm = FileManager.default
let quarantena = radice + "/.RawLineSpace/Quarantena/riparazione-" + ISO8601DateFormatter().string(from: Date()).replacingOccurrences(of: ":", with: "-")

// impronte registrate al momento della copia
var attese: [String: String] = [:]
for riga in (try! String(contentsOfFile: regCopia, encoding: .utf8)).split(separator: "\n") {
    if let d = try? JSONSerialization.jsonObject(with: Data(riga.utf8)) as? [String: Any], d["stato"] as? String == "VERIFICATA",
       let r = d["rel"] as? String, let h = d["hash"] as? String { attese[r] = h }
}

if !fm.fileExists(atPath: regRip) { fm.createFile(atPath: regRip, contents: nil) }
let regFd = open(regRip, O_WRONLY | O_APPEND); let regLock = NSLock()
func registra(_ d: [String: Any]) {
    var r = d; r["t"] = ISO8601DateFormatter().string(from: Date())
    var data = try! JSONSerialization.data(withJSONObject: r, options: [.sortedKeys]); data.append(0x0A)
    regLock.lock(); data.withUnsafeBytes { _ = write(regFd, $0.baseAddress, $0.count) }; _ = fcntl(regFd, F_FULLFSYNC); regLock.unlock()
}
func impronta(_ p: String) -> String? {
    let fd = open(p, O_RDONLY); guard fd >= 0 else { return nil }; defer { close(fd) }
    _ = fcntl(fd, F_NOCACHE, 1); var h = SHA256(); var b = [UInt8](repeating: 0, count: 4 << 20)
    while true { let n = read(fd, &b, b.count); if n < 0 { return nil }; if n == 0 { break }
        b.withUnsafeBytes { h.update(bufferPointer: UnsafeRawBufferPointer(rebasing: $0[0..<n])) } }
    return h.finalize().map { String(format: "%02x", $0) }.joined()
}
func syncDir(_ p: String) { let fd = open(p, O_RDONLY); if fd >= 0 { _ = fcntl(fd, F_FULLFSYNC); close(fd) } }

// Esegue lavori in parallelo con un tetto: sui dischi meccanici pochi, su SSD di più.
func inParallelo<T>(_ lavori: [T], max: Int, _ f: @escaping (T) -> Void) {
    let q = OperationQueue(); q.maxConcurrentOperationCount = max
    for l in lavori { q.addOperation { f(l) } }
    q.waitUntilAllOperationsAreFinished()
}
let paralleli = Int(ProcessInfo.processInfo.environment["PARALLELI"] ?? "4") ?? 4

// ---------- 1. controllo
var t = Date(); var danneggiati: [(String, String)] = []; let lk = NSLock()
inParallelo(Array(attese), max: paralleli) { (rel, h) in
    let p = radice + "/" + rel
    let esito: String? = !fm.fileExists(atPath: p) ? "sparito" : (impronta(p) == h ? nil : "contenuto cambiato")
    if let e = esito { lk.lock(); danneggiati.append((rel, e)); lk.unlock() }
}
danneggiati.sort { $0.0 < $1.0 }
print(String(format: "CONTROLLO: %d file riletti in %.0f s con %d letture in parallelo → %d danneggiati", attese.count, Date().timeIntervalSince(t), paralleli, danneggiati.count))
danneggiati.forEach { print("  \($0.0): \($0.1)") }
registra(["stato": "CONTROLLO", "file": attese.count, "danneggiati": danneggiati.map { $0.0 }])
if danneggiati.isEmpty { exit(0) }

// ---------- 2. riparazione in parallelo
enum Esito { case riparato(String), nessunaCopiaBuona([String]), errore(String) }
func ripara(_ rel: String) -> Esito {
    guard let h = attese[rel] else { return .errore("nessuna impronta registrata") }
    let dest = radice + "/" + rel
    // cerca una copia con esattamente l'impronta registrata
    var provate: [String] = []; var buona: String?
    for r in altre {
        let p = r + "/" + rel
        guard fm.fileExists(atPath: p) else { provate.append("\(r): non c'è"); continue }
        if impronta(p) == h { buona = p; break } else { provate.append("\(r): impronta diversa") }
    }
    guard let src = buona else { return .nessunaCopiaBuona(provate) }
    // copia verificata su un nome temporaneo accanto al file danneggiato
    let dir = (dest as NSString).deletingLastPathComponent
    try? fm.createDirectory(atPath: dir, withIntermediateDirectories: true)
    let tmp = dir + "/.rawline-tmp-" + UUID().uuidString
    registra(["rel": rel, "stato": "RIPARAZIONE_INIZIATA", "da": src, "tmp": tmp])
    let fi = open(src, O_RDONLY), fo = open(tmp, O_WRONLY | O_CREAT | O_EXCL, 0o600)
    guard fi >= 0, fo >= 0 else { return .errore("apertura") }
    _ = fcntl(fi, F_NOCACHE, 1); _ = fcntl(fo, F_NOCACHE, 1)
    var b = [UInt8](repeating: 0, count: 4 << 20)
    while true { let n = read(fi, &b, b.count); if n <= 0 { break }; var off = 0
        while off < n { let w = b.withUnsafeBytes { write(fo, $0.baseAddress! + off, n - off) }; if w <= 0 { close(fi); close(fo); unlink(tmp); return .errore("scrittura") }; off += w } }
    close(fi)
    _ = copyfile(src, tmp, nil, copyfile_flags_t(COPYFILE_METADATA))
    var st = stat(); lstat(src, &st); var tm = [st.st_mtimespec, st.st_mtimespec]; futimens(fo, &tm)
    _ = fcntl(fo, F_FULLFSYNC); close(fo)
    guard impronta(tmp) == h else { unlink(tmp); registra(["rel": rel, "stato": "RIPARAZIONE_FALLITA", "motivo": "la copia riletta non coincide"]); return .errore("verifica della copia") }
    registra(["rel": rel, "stato": "RIPARAZIONE_PRONTA", "hash": h])
    // il file danneggiato va in quarantena (se c'è ancora), poi la copia buona prende il suo nome
    if fm.fileExists(atPath: dest) {
        let q = quarantena + "/" + rel
        try? fm.createDirectory(atPath: (q as NSString).deletingLastPathComponent, withIntermediateDirectories: true)
        if renamex_np(dest, q, UInt32(RENAME_EXCL)) != 0 { unlink(tmp); return .errore("quarantena: " + String(cString: strerror(errno))) }
        registra(["rel": rel, "stato": "DANNEGGIATO_IN_QUARANTENA", "a": q])
    }
    if renamex_np(tmp, dest, UInt32(RENAME_EXCL)) != 0 { return .errore("rinomina finale: " + String(cString: strerror(errno))) }
    syncDir(dir)
    registra(["rel": rel, "stato": "RIPARATO", "hash": h, "da": src])
    return .riparato(src)
}
t = Date(); var esiti: [(String, Esito)] = []
inParallelo(danneggiati.map { $0.0 }, max: paralleli) { rel in let e = ripara(rel); lk.lock(); esiti.append((rel, e)); lk.unlock() }
esiti.sort { $0.0 < $1.0 }
var ok = 0
for (rel, e) in esiti {
    switch e {
    case .riparato(let da): ok += 1; print("  RIPARATO \(rel)  ← da \((da as NSString).deletingLastPathComponent.components(separatedBy: "/").prefix(3).joined(separator: "/"))")
    case .nessunaCopiaBuona(let p): print("  NON RIPARABILE \(rel): nessuna copia con l'impronta giusta (\(p.joined(separator: "; ")))")
    case .errore(let m): print("  ERRORE \(rel): \(m)")
    }
}
print(String(format: "RIPARAZIONE: %d su %d riparati in %.0f s. I file danneggiati sono in quarantena: %@", ok, danneggiati.count, Date().timeIntervalSince(t), quarantena))
