// Prototipo della copia verificata di RawLine Space (prova, non codice di prodotto).
// uso: copia <cartella sorgente> <cartella destinazione> <registro.jsonl>
// La sorgente si apre SOLO in lettura. Sulla destinazione si scrive solo con nomi temporanei
// `.rawline-tmp-*`, che poi diventano il nome finale con una rinomina che non sovrascrive mai.
import Foundation
import CryptoKit
import Darwin

let src = CommandLine.arguments[1], dst = CommandLine.arguments[2], regPath = CommandLine.arguments[3]
let tag = ".rawline-tmp-"
setvbuf(stdout, nil, _IOLBF, 0)

// ---------- registro: righe JSON solo in aggiunta, forzate su disco a ogni passo
if !FileManager.default.fileExists(atPath: regPath) { FileManager.default.createFile(atPath: regPath, contents: nil) }
let reg = open(regPath, O_WRONLY | O_APPEND)
func registra(_ d: [String: Any]) {
    var r = d; r["t"] = ISO8601DateFormatter().string(from: Date())
    var data = try! JSONSerialization.data(withJSONObject: r, options: [.sortedKeys]); data.append(0x0A)
    data.withUnsafeBytes { _ = write(reg, $0.baseAddress, $0.count) }
    _ = fcntl(reg, F_FULLFSYNC)
}
// stato già registrato: file verificati e temporanei aperti
var verificati: [String: String] = [:]; var tmpAperti: [String: String] = [:]; var pronti: [String: String] = [:]
var staccoDaControllare = false
if let testo = try? String(contentsOfFile: regPath, encoding: .utf8) {
    for riga in testo.split(separator: "\n") {
        guard let d = try? JSONSerialization.jsonObject(with: Data(riga.utf8)) as? [String: Any],
              let st = d["stato"] as? String else { continue }
        // uno stacco non corretto resta "da controllare" finché un controllo completo non riesce
        if st == "PAUSA" { staccoDaControllare = true }
        if st == "CONTROLLO_OK" { staccoDaControllare = false }
        guard let rel = d["rel"] as? String else { continue }
        if st == "INIZIATA", let t = d["tmp"] as? String { tmpAperti[rel] = t; pronti[rel] = nil }
        if st == "PRONTA", let h = d["hash"] as? String { pronti[rel] = h }
        if st == "VERIFICATA", let h = d["hash"] as? String { verificati[rel] = h; tmpAperti[rel] = nil }
        if st == "FALLITA" { tmpAperti[rel] = nil }
    }
}

// ---------- ripresa dopo un'interruzione: si tolgono solo i propri temporanei
var ripuliti = 0
for (_, t) in tmpAperti where FileManager.default.fileExists(atPath: t) {
    precondition((t as NSString).lastPathComponent.hasPrefix(tag)); unlink(t); ripuliti += 1
}
if ripuliti > 0 { print("ripresa: tolti \(ripuliti) temporanei lasciati a metà") }
// sicurezza in più: qualunque temporaneo nostro rimasto senza riga nel registro
if let e = FileManager.default.enumerator(atPath: dst) {
    for case let p as String in e where (p as NSString).lastPathComponent.hasPrefix(tag) {
        unlink(dst + "/" + p); print("ripresa: tolto temporaneo orfano \(p)")
    }
}

let fm = FileManager.default
// ---------- un disco assente non è un disco vuoto: senza sorgente non si parte nemmeno
for (nome, p) in [("sorgente", src), ("destinazione", (dst as NSString).deletingLastPathComponent)] {
    let c = p.split(separator: "/")
    let vol = c.count >= 2 && c[0] == "Volumes" ? "/Volumes/" + c[1] : "/"
    var isDir: ObjCBool = false
    if !fm.fileExists(atPath: vol, isDirectory: &isDir) || (try? URL(fileURLWithPath: vol).resourceValues(forKeys: [.volumeUUIDStringKey]))?.volumeUUIDString == nil
        || (nome == "sorgente" && !fm.fileExists(atPath: p)) {
        registra(["stato": "RIFIUTATA", "motivo": "\(nome) assente: \(p)"])
        print("RIFIUTO DI PARTIRE: la \(nome) (\(p)) non c'è. Un disco assente non è un disco vuoto: collegalo e riprova.")
        exit(4)
    }
}
// ---------- controllo al riattacco: dopo uno stacco non corretto, prima di scrivere si controlla tutto
if staccoDaControllare {
    let c = dst.split(separator: "/")
    let vol = c.count >= 2 && c[0] == "Volumes" ? "/Volumes/" + c[1] : "/"
    let uuid = (try? URL(fileURLWithPath: vol).resourceValues(forKeys: [.volumeUUIDStringKey]))?.volumeUUIDString ?? vol
    print("CONTROLLO AL RIATTACCO: durante l'ultima operazione il disco \(vol) è stato staccato in modo non corretto. Prima di scrivere controllo che sia integro.")
    registra(["stato": "CONTROLLO_INIZIATO", "volume": uuid])
    // 1. il file system, in sola lettura
    let p = Process(); p.executableURL = URL(fileURLWithPath: "/usr/sbin/diskutil"); p.arguments = ["verifyVolume", uuid]
    let pipe = Pipe(); p.standardOutput = pipe; p.standardError = pipe
    try! p.run(); let out = String(decoding: pipe.fileHandleForReading.readDataToEndOfFile(), as: UTF8.self); p.waitUntilExit()
    if p.terminationStatus != 0 || !out.contains("appears to be OK") {
        registra(["stato": "CONTROLLO_FALLITO", "motivo": "file system"])
        print("IL FILE SYSTEM DEL DISCO HA PROBLEMI: non scrivo niente. Esito di macOS:\n" + out.split(separator: "\n").suffix(5).joined(separator: "\n")); exit(5)
    }
    print("  1. file system: integro")
    // 2. ogni file già dato per verificato in questa operazione si rilegge per intero
    var rotti: [String] = []; let t = Date()
    for (rel, h) in verificati.sorted(by: { $0.key < $1.key }) {
        let d = dst + "/" + rel
        if !FileManager.default.fileExists(atPath: d) { rotti.append("\(rel): sparito"); continue }
        if (try? hashFile(d)) != h { rotti.append("\(rel): contenuto cambiato") }
    }
    if !rotti.isEmpty {
        registra(["stato": "CONTROLLO_FALLITO", "motivo": "file danneggiati", "file": rotti])
        print("  2. FILE DANNEGGIATI DOPO LO STACCO (\(rotti.count)): non scrivo niente finché non si decide cosa fare."); rotti.prefix(10).forEach { print("     " + $0) }; exit(5)
    }
    print(String(format: "  2. riletti per intero i %d file già copiati: tutti integri (%.0f s)", verificati.count, Date().timeIntervalSince(t)))
    registra(["stato": "CONTROLLO_OK", "volume": uuid, "file_riletti": verificati.count])
    print("  controllo superato: riprendo.")
}
// ---------- elenco della sorgente
var files: [(String, Int)] = []
let en = fm.enumerator(at: URL(fileURLWithPath: src), includingPropertiesForKeys: [.isRegularFileKey, .fileSizeKey, .isSymbolicLinkKey])!
for case let u as URL in en {
    let v = try! u.resourceValues(forKeys: [.isRegularFileKey, .fileSizeKey, .isSymbolicLinkKey])
    guard v.isRegularFile == true, v.isSymbolicLink != true else { continue }
    let rel = String(u.path.dropFirst(src.count + 1))
    if (rel as NSString).lastPathComponent == ".DS_Store" { continue }
    files.append((rel, v.fileSize ?? 0))
}
files.sort { $0.0 < $1.0 }

func hashFile(_ p: String) throws -> String {
    let fd = open(p, O_RDONLY); guard fd >= 0 else { throw NSError(domain: "lettura \(p): " + String(cString: strerror(errno)), code: Int(errno)) }
    defer { close(fd) }
    _ = fcntl(fd, F_NOCACHE, 1)
    var h = SHA256(); var b = [UInt8](repeating: 0, count: 8 << 20)
    while true { let n = read(fd, &b, b.count); if n < 0 { throw NSError(domain: "lettura", code: Int(errno)) }; if n == 0 { break }
        b.withUnsafeBytes { h.update(bufferPointer: UnsafeRawBufferPointer(rebasing: $0[0..<n])) } }
    return h.finalize().map { String(format: "%02x", $0) }.joined()
}
func xattrs(_ p: String) -> [String: Data] {
    var out: [String: Data] = [:]
    let n = listxattr(p, nil, 0, XATTR_NOFOLLOW); guard n > 0 else { return out }
    var nb = [CChar](repeating: 0, count: n); listxattr(p, &nb, n, XATTR_NOFOLLOW)
    // com.apple.provenance lo aggiunge macOS a ogni file creato da un programma: non è un dato dell'utente
    for nome in nb.split(separator: 0).map({ String(cString: Array($0) + [0]) }) where nome != "com.apple.provenance" {
        let l = getxattr(p, nome, nil, 0, 0, XATTR_NOFOLLOW); guard l >= 0 else { continue }
        var d = Data(count: l); _ = d.withUnsafeMutableBytes { getxattr(p, nome, $0.baseAddress, l, 0, XATTR_NOFOLLOW) }
        out[nome] = d
    }
    return out
}
struct Meta: Equatable { let size: Int64; let mtime: timespec_eq; let btime: timespec_eq; let mode: UInt16; let flags: UInt32 }
struct timespec_eq: Equatable { let s: Int; let ns: Int }
func meta(_ p: String) -> Meta? {
    var st = stat(); guard lstat(p, &st) == 0 else { return nil }
    return Meta(size: st.st_size, mtime: .init(s: st.st_mtimespec.tv_sec, ns: st.st_mtimespec.tv_nsec),
                btime: .init(s: st.st_birthtimespec.tv_sec, ns: st.st_birthtimespec.tv_nsec), mode: st.st_mode & 0o7777, flags: st.st_flags)
}

// ---------- copia di un file
enum Esito { case copiato(String), gia, fallito(String) }
func copiaUno(_ rel: String, _ size: Int) -> Esito {
    let s = src + "/" + rel, d = dst + "/" + rel
    if let h = verificati[rel], fm.fileExists(atPath: d) { _ = h; return .gia }
    if fm.fileExists(atPath: d) {
        // interruzione tra la rinomina e la riga VERIFICATA: si riconosce il file solo dall'impronta registrata
        if let h = pronti[rel], let hd = try? hashFile(d), hd == h, let hsrc = try? hashFile(s), hsrc == h {
            registra(["rel": rel, "stato": "VERIFICATA", "hash": h, "size": size, "ripresa": true]); verificati[rel] = h
            print("ripresa: \(rel) aveva già il nome finale, impronta uguale, ora verificato")
            return .gia
        }
        return .fallito("il nome finale esiste già e non è nel registro con la stessa impronta: non si tocca")
    }
    try? fm.createDirectory(atPath: (d as NSString).deletingLastPathComponent, withIntermediateDirectories: true)
    let tmp = (d as NSString).deletingLastPathComponent + "/" + tag + UUID().uuidString
    guard let m0 = meta(s) else { return .fallito("sorgente sparita") }
    registra(["rel": rel, "stato": "INIZIATA", "tmp": tmp, "size": size, "src_mtime": m0.mtime.s])

    // 1. copia con l'impronta calcolata leggendo
    let fi = open(s, O_RDONLY), fo = open(tmp, O_WRONLY | O_CREAT | O_EXCL, 0o600)
    guard fi >= 0, fo >= 0 else { if fo >= 0 { close(fo); unlink(tmp) }; if fi >= 0 { close(fi) }; return .fallito("apertura: " + String(cString: strerror(errno))) }
    _ = fcntl(fi, F_NOCACHE, 1); _ = fcntl(fo, F_NOCACHE, 1)
    var h = SHA256(); var b = [UInt8](repeating: 0, count: 8 << 20); var scritti = 0
    while true {
        let n = read(fi, &b, b.count); if n < 0 { close(fi); close(fo); unlink(tmp); return .fallito("lettura") }; if n == 0 { break }
        b.withUnsafeBytes { h.update(bufferPointer: UnsafeRawBufferPointer(rebasing: $0[0..<n])) }
        var off = 0; while off < n { let w = b.withUnsafeBytes { write(fo, $0.baseAddress! + off, n - off) }; if w <= 0 { close(fi); close(fo); unlink(tmp); return .fallito("scrittura: " + String(cString: strerror(errno))) }; off += w }
        scritti += n
    }
    close(fi)
    let hs = h.finalize().map { String(format: "%02x", $0) }.joined()
    // 2. metadati: attributi estesi, permessi, flag, poi le date
    if copyfile(s, tmp, nil, copyfile_flags_t(COPYFILE_METADATA)) != 0 { close(fo); unlink(tmp); return .fallito("metadati: " + String(cString: strerror(errno))) }
    var times = [timespec(tv_sec: m0.mtime.s, tv_nsec: m0.mtime.ns), timespec(tv_sec: m0.mtime.s, tv_nsec: m0.mtime.ns)]
    futimens(fo, &times)
    var al = attrlist(); al.bitmapcount = u_short(ATTR_BIT_MAP_COUNT); al.commonattr = attrgroup_t(ATTR_CMN_CRTIME)
    var bt = timespec(tv_sec: m0.btime.s, tv_nsec: m0.btime.ns)
    fsetattrlist(fo, &al, &bt, MemoryLayout<timespec>.size, 0)
    // 3. scrittura forzata sul disco
    let durabile = fcntl(fo, F_FULLFSYNC) == 0 || fsync(fo) == 0
    close(fo)
    // 4. verifica: rilettura dal disco, metadati, attributi estesi
    guard let hd = try? hashFile(tmp) else { unlink(tmp); return .fallito("rilettura della copia") }
    var problemi: [String] = []
    if hd != hs { problemi.append("contenuto diverso") }
    if scritti != size { problemi.append("byte copiati \(scritti) invece di \(size)") }
    if let ms = meta(s), let mt = meta(tmp) {
        if ms.size != mt.size { problemi.append("dimensione") }
        if ms.mtime != mt.mtime { problemi.append("data di modifica") }
        if ms.btime != mt.btime { problemi.append("data di creazione") }
        if ms.mode != mt.mode { problemi.append("permessi") }
        if ms.flags != mt.flags { problemi.append("flag") }
    } else { problemi.append("metadati illeggibili") }
    if xattrs(s) != xattrs(tmp) { problemi.append("attributi estesi (etichette Finder ecc.)") }
    if meta(s) != m0 { problemi.append("la sorgente è cambiata durante la copia") }
    if !problemi.isEmpty { unlink(tmp); registra(["rel": rel, "stato": "FALLITA", "motivo": problemi.joined(separator: ", ")]); return .fallito(problemi.joined(separator: ", ")) }
    // 5. nome finale senza mai sovrascrivere. Prima si scrive nel registro l'impronta verificata:
    //    se il programma muore subito dopo la rinomina, alla ripresa il file si riconosce da quella.
    registra(["rel": rel, "stato": "PRONTA", "hash": hs, "size": size])
    if ProcessInfo.processInfo.environment["PROVA_MUORI_DOPO_RINOMINA"] == rel { _ = renamex_np(tmp, d, UInt32(RENAME_EXCL)); kill(getpid(), SIGKILL) }
    if renamex_np(tmp, d, UInt32(RENAME_EXCL)) != 0 { let e = String(cString: strerror(errno)); unlink(tmp); registra(["rel": rel, "stato": "FALLITA", "motivo": "rinomina: " + e]); return .fallito("rinomina: " + e) }
    let dfd = open((d as NSString).deletingLastPathComponent, O_RDONLY); _ = fcntl(dfd, F_FULLFSYNC); close(dfd)
    registra(["rel": rel, "stato": "VERIFICATA", "hash": hs, "size": size, "durabile": durabile])
    verificati[rel] = hs
    return .copiato(hs)
}

// Un disco che sparisce non è un disco vuoto: ci si ferma subito, senza concludere niente.
func radiceVolume(_ p: String) -> String { let c = p.split(separator: "/"); return c.count >= 2 && c[0] == "Volumes" ? "/Volumes/" + c[1] : "/" }
let volSrc = radiceVolume(src), volDst = radiceVolume(dst)
func idVolume(_ v: String) -> String? { (try? URL(fileURLWithPath: v).resourceValues(forKeys: [.volumeUUIDStringKey]))?.volumeUUIDString }
try? fm.createDirectory(atPath: dst, withIntermediateDirectories: true)
let uuidSrc = idVolume(volSrc), uuidDst = idVolume(volDst)
func dischiPresenti() -> String? {
    if idVolume(volSrc) != uuidSrc || !fm.fileExists(atPath: src) { return "sorgente (\(volSrc))" }
    if idVolume(volDst) != uuidDst || !fm.fileExists(atPath: dst) { return "destinazione (\(volDst))" }
    return nil
}
let t0 = Date(); var tot = 0, nuovi = 0, gia = 0; var falliti: [(String, String)] = []
for (rel, size) in files {
    if let manca = dischiPresenti() {
        registra(["stato": "PAUSA", "motivo": "disco scollegato: " + manca])
        print("DISCO SCOLLEGATO: \(manca). Mi fermo. Verificati finora: \(verificati.count) su \(files.count). Niente è stato concluso sui file non verificati.")
        exit(3)
    }
    switch copiaUno(rel, size) {
    case .copiato: nuovi += 1; tot += size
    case .gia: gia += 1
    case .fallito(let m):
        if let manca = dischiPresenti() {
            registra(["stato": "PAUSA", "motivo": "disco scollegato: " + manca])
            print("DISCO SCOLLEGATO durante \(rel): \(manca). Mi fermo. Verificati: \(verificati.count) su \(files.count)."); exit(3)
        }
        falliti.append((rel, m)); print("NON VERIFICATO: \(rel): \(m)")
    }
}
let dt = Date().timeIntervalSince(t0)

// ---------- controllo di completezza: stesso elenco, stessi byte, cartella per cartella
var mancano = 0, byteS = 0, byteD = 0
for (rel, size) in files { byteS += size; if let m = meta(dst + "/" + rel) { byteD += Int(m.size) } else { mancano += 1 } }
var extra = 0
if let e = fm.enumerator(atPath: dst) { for case let p as String in e { var isd: ObjCBool = false; fm.fileExists(atPath: dst + "/" + p, isDirectory: &isd); if !isd.boolValue && (p as NSString).lastPathComponent != ".DS_Store" && !files.contains(where: { $0.0 == p }) { extra += 1 } } }
print(String(format: "file=%d nuovi=%d già_verificati=%d non_verificati=%d  GB=%.2f  %.0f s  %.0f MB/s", files.count, nuovi, gia, falliti.count, Double(tot) / 1e9, dt, Double(tot) / 1e6 / max(dt, 0.001)))
print("completezza: mancano=\(mancano) file_in_più=\(extra) byte_sorgente=\(byteS) byte_copia=\(byteD) \(mancano == 0 && extra == 0 && byteS == byteD ? "OK" : "DIFFERENZE")")
