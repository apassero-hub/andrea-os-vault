// Prototipo del riordino sullo stesso disco, con registro, istantanee e ripristino (prova, non prodotto).
//   riordina istantanea <radice> <file.tsv>              elenco: percorso, id del file, dimensione, data
//   riordina applica    <radice> <piano.tsv> <reg.jsonl> piano: "da<TAB>a" relativi alla radice
//   riordina ripristina <radice> <istantanea.tsv> <reg.jsonl>
// Regole: solo rinomine che non sovrascrivono mai (RENAME_EXCL); prima di ogni passo si ricontrolla
// che il file sia lo stesso (id, dimensione, data); nessuna eliminazione: la quarantena è uno spostamento.
import Foundation
import Darwin
setvbuf(stdout, nil, _IOLBF, 0)
let args = CommandLine.arguments
let cmd = args[1], root = args[2]
let fm = FileManager.default

struct Voce { let rel: String; let ino: UInt64; let size: Int64; let mtime: Int }
func id(_ p: String) -> (UInt64, Int64, Int)? { var st = stat(); guard lstat(p, &st) == 0 else { return nil }; return (st.st_ino, st.st_size, st.st_mtimespec.tv_sec) }
func scansione() -> [Voce] {
    var out: [Voce] = []
    let en = fm.enumerator(atPath: root)!
    for case let rel as String in en {
        let p = root + "/" + rel; var st = stat(); guard lstat(p, &st) == 0, (st.st_mode & S_IFMT) == S_IFREG else { continue }
        if (rel as NSString).lastPathComponent == ".DS_Store" { continue }
        out.append(Voce(rel: rel, ino: st.st_ino, size: st.st_size, mtime: st.st_mtimespec.tv_sec))
    }
    return out
}
func leggiIstantanea(_ f: String) -> [Voce] {
    (try! String(contentsOfFile: f, encoding: .utf8)).split(separator: "\n").map { l in
        let c = l.split(separator: "\t", omittingEmptySubsequences: false).map(String.init)
        return Voce(rel: c[0], ino: UInt64(c[1])!, size: Int64(c[2])!, mtime: Int(c[3])!)
    }
}
var regFd: Int32 = -1
func registra(_ d: [String: Any]) {
    var r = d; r["t"] = ISO8601DateFormatter().string(from: Date())
    var data = try! JSONSerialization.data(withJSONObject: r, options: [.sortedKeys]); data.append(0x0A)
    data.withUnsafeBytes { _ = write(regFd, $0.baseAddress, $0.count) }; _ = fcntl(regFd, F_FULLFSYNC)
}
func apriRegistro(_ f: String) { if !fm.fileExists(atPath: f) { fm.createFile(atPath: f, contents: nil) }; regFd = open(f, O_WRONLY | O_APPEND) }
func syncDir(_ p: String) { let fd = open(p, O_RDONLY); if fd >= 0 { _ = fcntl(fd, F_FULLFSYNC); close(fd) } }

// Esegue un elenco di spostamenti (da, a, id atteso). Restituisce (fatti, saltati).
func esegui(_ passi: [(String, String, UInt64)], lotto: String) -> (Int, [String]) {
    var fatti = 0; var saltati: [String] = []
    // ripresa: passi INIZIATI e non chiusi di questo lotto si risolvono guardando dov'è davvero il file
    for (i, (da, a, ino)) in passi.enumerated() {
        let pda = root + "/" + da, pa = root + "/" + a
        if let x = id(pa), x.0 == ino { fatti += 1; continue }               // già al suo posto (ripresa)
        guard let x = id(pda) else { saltati.append("\(da): sparito, non si indovina"); continue }
        guard x.0 == ino else { saltati.append("\(da): non è più lo stesso file"); continue }
        if id(pa) != nil { saltati.append("\(a): destinazione occupata, non si sovrascrive"); continue }
        try? fm.createDirectory(atPath: (pa as NSString).deletingLastPathComponent, withIntermediateDirectories: true)
        registra(["lotto": lotto, "n": i, "stato": "INIZIATA", "da": da, "a": a, "ino": ino])
        if renamex_np(pda, pa, UInt32(RENAME_EXCL)) != 0 { saltati.append("\(da): " + String(cString: strerror(errno))); registra(["lotto": lotto, "n": i, "stato": "FALLITA"]); continue }
        registra(["lotto": lotto, "n": i, "stato": "FATTA"])
        fatti += 1
        if i % 200 == 0 { syncDir(root) }
    }
    syncDir(root)
    return (fatti, saltati)
}

switch cmd {
case "istantanea":
    let v = scansione().sorted { $0.rel < $1.rel }
    try! v.map { "\($0.rel)\t\($0.ino)\t\($0.size)\t\($0.mtime)" }.joined(separator: "\n").write(toFile: args[3], atomically: true, encoding: .utf8)
    print("istantanea: \(v.count) file, \(v.reduce(0) { $0 + $1.size }) byte")
case "applica":
    apriRegistro(args[4])
    let ora = Dictionary(uniqueKeysWithValues: scansione().map { ($0.rel, $0.ino) })
    var passi: [(String, String, UInt64)] = []
    var errori: [String] = []
    var destinazioni = Set<String>()
    for l in (try! String(contentsOfFile: args[3], encoding: .utf8)).split(separator: "\n") {
        let c = l.split(separator: "\t").map(String.init)
        let chiave = c[1].decomposedStringWithCanonicalMapping.lowercased()
        if destinazioni.contains(chiave) { errori.append("due file verso \(c[1])") }
        destinazioni.insert(chiave)
        if let ino = ora[c[0]] { passi.append((c[0], c[1], ino)) }
        else if let x = id(root + "/" + c[1]) { passi.append((c[0], c[1], x.0)) } // ripresa: già spostato
        else { errori.append("non trovato: \(c[0])") }
    }
    if !errori.isEmpty { print("PIANO RIFIUTATO:\n" + errori.prefix(10).joined(separator: "\n")); exit(2) }
    let lotto = (args[3] as NSString).lastPathComponent
    let (f, s) = esegui(passi, lotto: lotto)
    print("applica \(lotto): spostati=\(f) saltati=\(s.count)"); s.prefix(10).forEach { print("  " + $0) }
case "ripristina":
    apriRegistro(args[4])
    let voluta = leggiIstantanea(args[3]); let ora = scansione()
    let dove = Dictionary(ora.map { ($0.ino, $0.rel) }, uniquingKeysWith: { a, _ in a })
    var passi: [(String, String, UInt64)] = []; var mancanti: [String] = []
    for v in voluta {
        guard let cur = dove[v.ino] else { mancanti.append(v.rel); continue }
        if cur != v.rel { passi.append((cur, v.rel, v.ino)) }
    }
    // secondo livello: file salvati da altre app come file nuovo (identificativo cambiato).
    // Si riconoscono dal nome solo se il nome è unico sia tra i mancanti sia tra i file arrivati dopo.
    let inoVoluti = Set(voluta.map { $0.ino })
    let arrivati = ora.filter { !inoVoluti.contains($0.ino) }
    func nomeChiave(_ r: String) -> String { (r as NSString).lastPathComponent.decomposedStringWithCanonicalMapping.lowercased() }
    let arriviPerNome = Dictionary(grouping: arrivati, by: { nomeChiave($0.rel) })
    let mancantiPerNome = Dictionary(grouping: mancanti, by: { nomeChiave($0) })
    var riconosciuti = 0
    for m in mancanti {
        let k = nomeChiave(m)
        guard mancantiPerNome[k]?.count == 1, let c = arriviPerNome[k], c.count == 1 else { continue }
        if c[0].rel != m { passi.append((c[0].rel, m, c[0].ino)) }
        print("  riconosciuto dal nome (identificativo cambiato, da far confermare): \(c[0].rel) → \(m)")
        riconosciuti += 1
    }
    mancanti.removeAll { m in passi.contains { $0.1 == m } }
    // destinazioni occupate da file che a loro volta devono spostarsi: si passa da un nome temporaneo
    let occupate = Set(passi.map { $0.1 }).intersection(Set(passi.map { $0.0 }))
    var fase1: [(String, String, UInt64)] = [], fase2: [(String, String, UInt64)] = []
    for p in passi {
        if occupate.contains(p.0) { let t = ".rawline-sposta-\(p.2)"; fase1.append((p.0, t, p.2)); fase2.append((t, p.1, p.2)) }
        else { fase2.append(p) }
    }
    let spostatiDalNome = Set(passi.map { $0.2 })
    let nuovi = arrivati.filter { !spostatiDalNome.contains($0.ino) }
    _ = riconosciuti
    print("piano di ripristino: \(passi.count) spostamenti, \(mancanti.count) file dell'istantanea non trovati, \(nuovi.count) file arrivati dopo (restano dove sono)")
    nuovi.prefix(5).forEach { print("  arrivato dopo: " + $0.rel) }
    let (a, sa) = esegui(fase1, lotto: "ripristino-fase1"); let (b, sb) = esegui(fase2, lotto: "ripristino")
    print("ripristino: spostati=\(b) (via nome temporaneo: \(a)) saltati=\(sa.count + sb.count)"); (sa + sb).prefix(10).forEach { print("  " + $0) }
    // cartelle rimaste vuote: non si cancellano, si elencano
    var vuote = 0
    if let en = fm.enumerator(atPath: root) { for case let r as String in en { var d: ObjCBool = false; if fm.fileExists(atPath: root + "/" + r, isDirectory: &d), d.boolValue, ((try? fm.contentsOfDirectory(atPath: root + "/" + r)) ?? []).filter({ $0 != ".DS_Store" }).isEmpty { vuote += 1 } } }
    print("cartelle rimaste vuote (non cancellate): \(vuote)")
default: print("comando sconosciuto")
}
