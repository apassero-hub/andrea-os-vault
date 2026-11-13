// Sonda delle capacità di un volume per RawLine Space.
// Scrive SOLO dentro la cartella indicata (che deve già esistere ed essere vuota o di prova).
import Foundation
import Darwin

let base = CommandLine.arguments[1]
var esiti: [(String, String)] = []
func nota(_ k: String, _ v: String) { esiti.append((k, v)); print("\(k): \(v)") }
func err() -> String { String(cString: strerror(errno)) + " (\(errno))" }

// --- capacità dichiarate dal volume
struct VolAttrBuf { var len: UInt32 = 0; var caps = vol_capabilities_attr_t() }
var al = attrlist()
al.bitmapcount = u_short(ATTR_BIT_MAP_COUNT)
al.volattr = attrgroup_t(ATTR_VOL_INFO) | attrgroup_t(ATTR_VOL_CAPABILITIES)
var buf = VolAttrBuf()
if getattrlist(base, &al, &buf, MemoryLayout<VolAttrBuf>.size, 0) == 0 {
    let fmt = buf.caps.capabilities.0, intr = buf.caps.capabilities.1
    func c(_ v: UInt32, _ b: Int32) -> String { (v & UInt32(bitPattern: b)) != 0 ? "sì" : "no" }
    nota("RENAME_EXCL", c(intr, VOL_CAP_INT_RENAME_EXCL))
    nota("RENAME_SWAP", c(intr, VOL_CAP_INT_RENAME_SWAP))
    nota("Cloni", c(intr, VOL_CAP_INT_CLONE))
    nota("Snapshot", c(intr, VOL_CAP_INT_SNAPSHOT))
    nota("Distingue maiuscole", c(fmt, VOL_CAP_FMT_CASE_SENSITIVE))
    nota("ID dei file persistenti", c(fmt, VOL_CAP_FMT_PERSISTENTOBJECTIDS))
    nota("Journal", c(fmt, VOL_CAP_FMT_JOURNAL))
} else { nota("getattrlist", err()) }

let dir = base + "/sonda-\(getpid())"
mkdir(dir, 0o755)
func scrivi(_ p: String, _ s: String) { FileManager.default.createFile(atPath: p, contents: s.data(using: .utf8)) }
func leggi(_ p: String) -> String? { (try? String(contentsOfFile: p, encoding: .utf8)) }

// --- RENAME_EXCL non sovrascrive
scrivi(dir + "/a.txt", "A"); scrivi(dir + "/b.txt", "B")
if renamex_np(dir + "/a.txt", dir + "/b.txt", UInt32(RENAME_EXCL)) == 0 { nota("EXCL su destinazione esistente", "HA SOVRASCRITTO (grave)") }
else { nota("EXCL su destinazione esistente", "rifiutato: " + err() + ", b.txt = " + (leggi(dir + "/b.txt") ?? "?")) }

// --- l'ID del file resta uguale dopo la rinomina
func ino(_ p: String) -> UInt64 { var st = stat(); return lstat(p, &st) == 0 ? st.st_ino : 0 }
let i1 = ino(dir + "/a.txt")
renamex_np(dir + "/a.txt", dir + "/a2.txt", UInt32(RENAME_EXCL))
nota("ID uguale dopo la rinomina", i1 == ino(dir + "/a2.txt") && i1 != 0 ? "sì" : "NO")

// --- cambio di sole maiuscole
scrivi(dir + "/IMG.ARW", "raw")
if renamex_np(dir + "/IMG.ARW", dir + "/img.ARW", UInt32(RENAME_EXCL)) == 0 { nota("Sole maiuscole con EXCL, un passo", "riuscito") }
else { nota("Sole maiuscole con EXCL, un passo", "rifiutato: " + err() + " → serve il passaggio dal nome temporaneo") }
let tmpName = dir + "/.rawline-tmp-case"
let ok2 = renamex_np(dir + "/IMG.ARW", tmpName, UInt32(RENAME_EXCL)) == 0 && renamex_np(tmpName, dir + "/img.ARW", UInt32(RENAME_EXCL)) == 0
let elenco = (try? FileManager.default.contentsOfDirectory(atPath: dir)) ?? []
nota("Sole maiuscole in due passi", ok2 ? "riuscito, ora: " + elenco.filter { $0.lowercased() == "img.arw" }.joined() : "fallito: " + err())

// --- accenti: NFC contro NFD
let nfc = "Città".precomposedStringWithCanonicalMapping, nfd = "Città".decomposedStringWithCanonicalMapping
scrivi(dir + "/" + nfc + ".txt", "nfc")
let fdNfd = open(dir + "/" + nfd + ".txt", O_CREAT | O_EXCL | O_WRONLY, 0o644)
nota("Stesso nome in NFC e NFD", fdNfd >= 0 ? "DUE file distinti (attenzione ai falsi doppioni)" : "lo stesso file: " + err())
if fdNfd >= 0 { close(fdNfd) }
let salvato = ((try? FileManager.default.contentsOfDirectory(atPath: dir)) ?? []).first { $0.hasPrefix("Citt") } ?? ""
nota("Forma salvata dal disco", salvato.unicodeScalars.count == nfc.unicodeScalars.count + 4 ? "NFC (come scritto)" : "NFD")

// --- RENAME_SWAP
scrivi(dir + "/s1.txt", "uno"); scrivi(dir + "/s2.txt", "due")
nota("RENAME_SWAP", renamex_np(dir + "/s1.txt", dir + "/s2.txt", UInt32(RENAME_SWAP)) == 0 ? "riuscito, s1 = " + (leggi(dir + "/s1.txt") ?? "?") : "non disponibile: " + err())

// --- clone APFS e spazio reale
let grande = dir + "/grande.bin"
FileManager.default.createFile(atPath: grande, contents: Data(count: 64 << 20))
let rc = clonefile(grande, dir + "/grande-clone.bin", 0)
nota("Clone", rc == 0 ? "riuscito" : "non disponibile: " + err())

// --- F_FULLFSYNC su questo disco
let fd = open(dir + "/fsync.bin", O_CREAT | O_WRONLY, 0o644)
var dati = [UInt8](repeating: 7, count: 1 << 20)
write(fd, &dati, dati.count)
var t = Date()
let r1 = fcntl(fd, F_FULLFSYNC)
nota("F_FULLFSYNC sul file", r1 == 0 ? String(format: "riuscito (%.1f ms)", Date().timeIntervalSince(t) * 1000) : "FALLITO: " + err())
close(fd)
let dfd = open(dir, O_RDONLY)
t = Date()
nota("F_FULLFSYNC sulla cartella", fcntl(dfd, F_FULLFSYNC) == 0 ? String(format: "riuscito (%.1f ms)", Date().timeIntervalSince(t) * 1000) : "FALLITO: " + err())
close(dfd)

// --- F_NOCACHE
let fd2 = open(grande, O_RDONLY)
nota("F_NOCACHE", fcntl(fd2, F_NOCACHE, 1) == 0 ? "riuscito" : "FALLITO: " + err())
close(fd2)

// --- cestino di sistema sul volume
do {
    var out: NSURL?
    scrivi(dir + "/cestino.txt", "x")
    try FileManager.default.trashItem(at: URL(fileURLWithPath: dir + "/cestino.txt"), resultingItemURL: &out)
    nota("Cestino del volume", "c'è: " + (out?.path ?? "?"))
    if let p = out?.path { try? FileManager.default.removeItem(atPath: p) }
} catch { nota("Cestino del volume", "non disponibile: \(error.localizedDescription)") }

// pulizia: la cartella della sonda contiene solo file creati da questa sonda
try? FileManager.default.removeItem(atPath: dir)
nota("Pulizia", FileManager.default.fileExists(atPath: dir) ? "NON riuscita" : "cartella della sonda tolta")
