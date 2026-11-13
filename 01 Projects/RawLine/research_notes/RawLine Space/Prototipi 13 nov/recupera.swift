// Prototipo di RawLine Space (prova, non prodotto): recupero SENZA un'altra copia.
//   recupera impronte <cartella> <impronte.json>           salva per ogni file l'impronta intera (SHA-256)
//                                                          e un controllo CRC-64 ogni 1 MB (8 byte per MB)
//   recupera ripara <cartella> <impronte.json> <registro>  controlla e, dove si può, recupera
// 1. Letture ripetute: se una lettura fallisce, riprova settore per settore (4 KB), con pause crescenti.
//    Se alla fine il file torna integro, lo riscrive in un posto nuovo del disco ("rinfresco").
// 2. Correzione di 1 o 2 bit cambiati per ogni MB: il CRC-64 dice quale MB è rovinato e, con un calcolo
//    algebrico, in quale bit. Il risultato vale solo se l'impronta SHA-256 dell'intero file torna identica.
// Il file rovinato non viene mai cancellato: va in quarantena. Ogni passo va nel registro prima di farlo.
// Prova: PROVA_EIO="rel@offset@n;..." fa fallire n volte (n=-1 sempre) la lettura di quel settore.
import Foundation
import CryptoKit
import Darwin
setvbuf(stdout, nil, _IOLBF, 0)

let BLOCCO = 1 << 20, SETTORE = 4096, TENTATIVI = 8
let fm = FileManager.default

// ---------- CRC-64/XZ
let POLY: UInt64 = 0xC96C5795D7870F42
let tab: [UInt64] = (0..<256).map { i in var c = UInt64(i); for _ in 0..<8 { c = (c & 1) != 0 ? (c >> 1) ^ POLY : c >> 1 }; return c }
func crc64(_ p: UnsafeRawBufferPointer) -> UInt64 {
    var c: UInt64 = ~0
    tab.withUnsafeBufferPointer { t in for b in p { c = t[Int((c ^ UInt64(b)) & 0xff)] ^ (c >> 8) } }
    return ~c
}
func crcBlocchi(_ d: [UInt8]) -> [UInt64] {
    d.withUnsafeBytes { p in stride(from: 0, to: max(d.count, 1), by: BLOCCO).map { o in
        crc64(UnsafeRawBufferPointer(rebasing: p[o..<min(o + BLOCCO, d.count)])) } }
}
func sha(_ d: [UInt8]) -> String { SHA256.hash(data: d).map { String(format: "%02x", $0) }.joined() }

// Sindromi: per un blocco lungo L byte, il "segno" che lascia nel CRC un singolo bit cambiato in ogni posizione.
// Non dipende dai dati, si calcola una volta sola. Ordinate per cercarle in fretta.
var cacheSindromi: [Int: [(UInt64, UInt32)]] = [:]
func sindromi(_ L: Int) -> [(UInt64, UInt32)] {
    if let s = cacheSindromi[L] { return s }
    var out: [(UInt64, UInt32)] = []; out.reserveCapacity(L * 8)
    for b in 0..<8 { var s = tab[1 << b]
        for k in 0..<L { out.append((s, UInt32((L - 1 - k) * 8 + b))); s = tab[Int(s & 0xff)] ^ (s >> 8) } }
    out.sort { $0.0 < $1.0 }; cacheSindromi[L] = out; return out
}
func cerca(_ t: [(UInt64, UInt32)], _ s: UInt64) -> Int? {
    var lo = 0, hi = t.count
    while lo < hi { let m = (lo + hi) / 2; if t[m].0 < s { lo = m + 1 } else { hi = m } }
    return lo < t.count && t[lo].0 == s ? lo : nil
}
/// Bit (posizioni dentro il blocco) che spiegano la differenza di CRC: uno solo, o una coppia.
func correzione(sindrome s: UInt64, L: Int) -> [Int]? {
    let t = sindromi(L)
    if let i = cerca(t, s) { return [Int(t[i].1)] }
    for (si, pi) in t { if let j = cerca(t, s ^ si), t[j].1 != pi { return [Int(pi), Int(t[j].1)] } }
    return nil
}

// ---------- 1. lettura con tentativi ripetuti
var iniezioni: [String: (Int, Int)] = [:], falliti: [String: Int] = [:]
for voce in (ProcessInfo.processInfo.environment["PROVA_EIO"] ?? "").split(separator: ";") {
    let p = voce.split(separator: "@").map(String.init); iniezioni[p[0]] = (Int(p[1])!, Int(p[2])!)
}
func preadProva(_ fd: Int32, _ buf: UnsafeMutableRawPointer, _ n: Int, _ off: Int, _ rel: String) -> Int {
    if let (o, k) = iniezioni[rel], off <= o, o < off + n {
        let f = falliti[rel, default: 0]; if k < 0 || f < k { falliti[rel] = f + 1; errno = EIO; return -1 }
    }
    return pread(fd, buf, n, off_t(off))
}
struct Lettura { var dati: [UInt8]; var illeggibili: [Int]; var tentativi: Int }
func leggi(_ path: String, _ rel: String) -> Lettura? {
    let fd = open(path, O_RDONLY); guard fd >= 0 else { return nil }; defer { close(fd) }
    _ = fcntl(fd, F_NOCACHE, 1); var st = stat(); fstat(fd, &st); let size = Int(st.st_size)
    var d = [UInt8](repeating: 0, count: size); var cattivi: [Int] = []; var tent = 0
    d.withUnsafeMutableBytes { buf in
        var off = 0
        while off < size {
            let n = min(BLOCCO, size - off)
            if preadProva(fd, buf.baseAddress! + off, n, off, rel) == n { off += n; continue }
            var s = off   // lettura fallita: si riprova un settore alla volta
            while s < off + n {
                let m = min(SETTORE, off + n - s); var ok = false
                for t in 1...TENTATIVI {
                    if preadProva(fd, buf.baseAddress! + s, m, s, rel) == m { ok = true; break }
                    tent += 1; usleep(UInt32(100_000 * t))
                }
                if !ok { cattivi.append(s); memset(buf.baseAddress! + s, 0, m) }
                s += m
            }
            off += n
        }
    }
    return Lettura(dati: d, illeggibili: cattivi, tentativi: tent)
}

func elenco(_ root: String) -> [String] {
    (fm.enumerator(atPath: root)?.allObjects as? [String] ?? []).filter { rel in
        !rel.split(separator: "/").contains { $0.hasPrefix(".") } &&
        ((try? fm.attributesOfItem(atPath: root + "/" + rel)[.type] as? FileAttributeType) == .typeRegular)
    }.sorted()
}
let a = CommandLine.arguments

if a[1] == "impronte" {
    let root = a[2]; var out: [[String: Any]] = []; var blocchi = 0; let t = Date()
    for rel in elenco(root) {
        guard let l = leggi(root + "/" + rel, rel) else { continue }
        var st = stat(); lstat(root + "/" + rel, &st); let c = crcBlocchi(l.dati); blocchi += c.count
        out.append(["rel": rel, "dim": l.dati.count, "sha256": sha(l.dati), "crc": c.map { String(format: "%016llx", $0) }.joined(),
                    "mtime": [st.st_mtimespec.tv_sec, st.st_mtimespec.tv_nsec], "btime": [st.st_birthtimespec.tv_sec, st.st_birthtimespec.tv_nsec]])
    }
    try! JSONSerialization.data(withJSONObject: out, options: [.sortedKeys]).write(to: URL(fileURLWithPath: a[3]))
    let byte = out.reduce(0) { $0 + ($1["dim"] as! Int) }
    print(String(format: "IMPRONTE: %d file, %.2f GB, %d blocchi da 1 MB in %.0f s. Spazio dei controlli a blocchi: %d byte (%.4f%% dei dati)",
                 out.count, Double(byte) / 1e9, blocchi, Date().timeIntervalSince(t), blocchi * 8, Double(blocchi * 8) / Double(byte) * 100))
    exit(0)
}

// ---------- ripara
let root = a[2]
let voci = try! JSONSerialization.jsonObject(with: Data(contentsOf: URL(fileURLWithPath: a[3]))) as! [[String: Any]]
let regRip = a[4]; if !fm.fileExists(atPath: regRip) { fm.createFile(atPath: regRip, contents: nil) }
let regFd = open(regRip, O_WRONLY | O_APPEND)
func registra(_ d: [String: Any]) {
    var r = d; r["t"] = ISO8601DateFormatter().string(from: Date())
    var data = try! JSONSerialization.data(withJSONObject: r, options: [.sortedKeys]); data.append(0x0A)
    data.withUnsafeBytes { _ = write(regFd, $0.baseAddress, $0.count) }; _ = fcntl(regFd, F_FULLFSYNC)
}
let quarantena = root + "/.RawLineSpace/Quarantena/recupero-" + ISO8601DateFormatter().string(from: Date()).replacingOccurrences(of: ":", with: "-")

/// Scrive i dati buoni su un temporaneo, li rilegge dal disco, sposta il vecchio in quarantena e dà il nome.
func sostituisci(_ rel: String, _ d: [UInt8], _ v: [String: Any], _ perche: String) -> String? {
    let dest = root + "/" + rel, dir = (dest as NSString).deletingLastPathComponent
    let tmp = dir + "/.rawline-tmp-" + UUID().uuidString, h = v["sha256"] as! String
    registra(["rel": rel, "stato": "RECUPERO_INIZIATO", "come": perche, "tmp": tmp])
    let fo = open(tmp, O_WRONLY | O_CREAT | O_EXCL, 0o600); guard fo >= 0 else { return "apertura temporaneo" }
    _ = fcntl(fo, F_NOCACHE, 1)
    let w = d.withUnsafeBytes { write(fo, $0.baseAddress, $0.count) }
    if w != d.count { close(fo); unlink(tmp); return "scrittura" }
    _ = copyfile(dest, tmp, nil, copyfile_flags_t(COPYFILE_METADATA))   // permessi, etichette, attributi
    let mt = v["mtime"] as! [Int], bt = v["btime"] as! [Int]            // le date di quando era integro
    var tm = [timespec(tv_sec: mt[0], tv_nsec: mt[1]), timespec(tv_sec: mt[0], tv_nsec: mt[1])]; futimens(fo, &tm)
    var al = attrlist(); al.bitmapcount = u_short(ATTR_BIT_MAP_COUNT); al.commonattr = attrgroup_t(ATTR_CMN_CRTIME)
    var b = timespec(tv_sec: bt[0], tv_nsec: bt[1]); fsetattrlist(fo, &al, &b, MemoryLayout<timespec>.size, 0)
    _ = fcntl(fo, F_FULLFSYNC); close(fo)
    guard let rl = leggi(tmp, ""), rl.illeggibili.isEmpty, sha(rl.dati) == h else { unlink(tmp); return "la copia riletta non coincide" }
    registra(["rel": rel, "stato": "RECUPERO_PRONTO", "hash": h])
    let q = quarantena + "/" + rel
    try? fm.createDirectory(atPath: (q as NSString).deletingLastPathComponent, withIntermediateDirectories: true)
    if renamex_np(dest, q, UInt32(RENAME_EXCL)) != 0 { unlink(tmp); return "quarantena" }
    registra(["rel": rel, "stato": "ROVINATO_IN_QUARANTENA", "a": q])
    if renamex_np(tmp, dest, UInt32(RENAME_EXCL)) != 0 { return "rinomina finale" }
    let dfd = open(dir, O_RDONLY); _ = fcntl(dfd, F_FULLFSYNC); close(dfd)
    registra(["rel": rel, "stato": "RECUPERATO", "come": perche, "hash": h])
    return nil
}

var integri = 0; let t0 = Date()
for v in voci {
    let rel = v["rel"] as! String, p = root + "/" + rel, dim = v["dim"] as! Int, h = v["sha256"] as! String
    guard fm.fileExists(atPath: p) else { print("  NON RECUPERABILE \(rel): il file non c'è più. Serve un'altra copia"); continue }
    guard var l = leggi(p, rel) else { print("  ERRORE \(rel): non si apre"); continue }
    if !l.illeggibili.isEmpty {
        print("  NON RECUPERABILE \(rel): \(l.illeggibili.count) settori illeggibili anche dopo \(TENTATIVI) tentativi (a \(l.illeggibili.map { "\($0 / 1024) KB" }.joined(separator: ", "))). Il file resta com'è")
        registra(["rel": rel, "stato": "SETTORI_ILLEGGIBILI", "offset": l.illeggibili]); continue
    }
    if l.dati.count != dim { print("  NON RECUPERABILE \(rel): la dimensione è cambiata (\(dim) → \(l.dati.count) byte). Serve un'altra copia"); continue }
    if sha(l.dati) == h {
        if l.tentativi == 0 { integri += 1; continue }
        // letto solo dopo più tentativi: il contenuto è buono, ma sta su un punto debole del disco
        let e = sostituisci(rel, l.dati, v, "rinfresco dopo \(l.tentativi) letture fallite")
        print(e == nil ? "  RECUPERATO \(rel): letto integro dopo \(l.tentativi) tentativi falliti, riscritto in un punto nuovo del disco" : "  ERRORE \(rel): \(e!)")
        continue
    }
    // 2. quali MB sono rovinati, e quali bit
    let attesi = stride(from: 0, to: (v["crc"] as! String).count, by: 16).map { i -> UInt64 in
        let s = v["crc"] as! String; return UInt64(s[s.index(s.startIndex, offsetBy: i)..<s.index(s.startIndex, offsetBy: i + 16)], radix: 16)! }
    let trovati = crcBlocchi(l.dati); var corretti: [String] = []; var impossibile: [Int] = []
    for (k, (x, y)) in zip(trovati, attesi).enumerated() where x != y {
        let L = min(BLOCCO, dim - k * BLOCCO)
        if let bit = correzione(sindrome: x ^ y, L: L) {
            for b in bit { l.dati[k * BLOCCO + b / 8] ^= UInt8(1 << (b % 8)); corretti.append("MB \(k), byte \(k * BLOCCO + b / 8)") }
        } else { impossibile.append(k) }
    }
    if !impossibile.isEmpty || sha(l.dati) != h {
        print("  NON RECUPERABILE \(rel): danno più grande di 2 bit nei MB \(impossibile.map(String.init).joined(separator: ", ")). Il file resta com'è; il danno è localizzato")
        registra(["rel": rel, "stato": "NON_RECUPERABILE", "blocchi": impossibile]); continue
    }
    let e = sostituisci(rel, l.dati, v, "correzione di \(corretti.count) bit")
    print(e == nil ? "  RECUPERATO \(rel): \(corretti.count) bit corretti (\(corretti.joined(separator: "; "))), impronta SHA-256 di nuovo identica" : "  ERRORE \(rel): \(e!)")
}
print(String(format: "FINE: %d file controllati in %.0f s, %d integri al primo colpo. Quarantena: %@", voci.count, Date().timeIntervalSince(t0), integri, quarantena))
