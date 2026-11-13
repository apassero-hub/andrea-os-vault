"""Ricostruisce l'indice (moov) di un video Sony XAVC S troncato (batteria morta, scheda tolta),
prendendo come modello un altro video della stessa fotocamera girato con le stesse impostazioni.
uso: ricostruisci.py <troncato> <modello> <uscita>
Il file troncato non si tocca: si scrive un file NUOVO con i dati recuperabili e un indice nuovo.
Struttura Sony (vista nel modello): ripetuto ogni secondo → blocco metadati (rtmd), N fotogrammi video, blocco audio."""
import sys, os, struct
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import mp4
tro, mod, out = sys.argv[1], sys.argv[2], sys.argv[3]
fm, top, tr = mp4.tracce(mod)
per = {t['handler']: t for t in tr}; V, A, M = per[b'vide'], per[b'soun'], per[b'meta']
ordine = [h for _, h in sorted((t['offsets'][0], t['handler']) for t in tr)]
assert ordine == [b'meta', b'vide', b'soun'], ordine
NF = V['stsc'][0][1]                      # fotogrammi per blocco (24)
MS = M['stsc'][0][1] * M['sizes'][0]      # byte del blocco metadati
AS = A['stsc'][0][1] * A['sizes'][0]      # byte del blocco audio
fm.seek(M['offsets'][0]); FIRMA = fm.read(12)
mdat_m = mp4.trova(top, b'mdat'); dati0 = M['offsets'][0]

d = open(tro, 'rb').read(); N = len(d)
assert d[mdat_m[1] + 4:mdat_m[1] + 8] == b'mdat' and d[dati0:dati0 + 12] == FIRMA, "il troncato non ha la stessa struttura del modello"

def fotogrammi(p, limite):
    """Da p, legge NF fotogrammi (ognuno comincia con un NAL AUD, tipo 9). Restituisce gli inizi
    e i possibili punti di fine dell'ultimo (la fine di ogni NAL dopo l'inizio dell'ultimo fotogramma)."""
    inizi = []; fini = []
    while p + 5 <= limite:
        L = struct.unpack('>I', d[p:p + 4])[0]; t = d[p + 4] & 0x1f
        if L == 0 or L > 20_000_000 or d[p + 4] & 0x80: break
        if t == 9:
            if len(inizi) == NF: break
            inizi.append(p)
        p += 4 + L
        if len(inizi) == NF: fini.append(p)
    return inizi, fini

gruppi = []; p = dati0
while p + MS <= N and d[p:p + 12] == FIRMA:
    v0 = p + MS; inizi, fini = fotogrammi(v0, N)
    if len(inizi) < NF: break
    fine = next((e for e in fini if e + AS <= N and (e + AS == N or d[e + AS:e + AS + 12] == FIRMA)), None)
    if fine is None or fine + AS > N: break   # ultimo secondo incompleto: si lascia fuori
    fv = inizi + [fine]; sizes = [fv[k + 1] - fv[k] for k in range(NF)]
    idr = [any((d[q + 4] & 0x1f) == 5 for q in nal_pos(fv[k], fv[k + 1])) for k in range(NF)] if False else None
    gruppi.append(dict(meta=p, video=v0, sizes=sizes, audio=fine)); p = fine + AS
if not gruppi: sys.exit("nessun secondo completo da recuperare")
fine_dati = p
def idr(a, b):
    while a < b:
        L = struct.unpack('>I', d[a:a + 4])[0]
        if d[a + 4] & 0x1f == 5: return True
        a += 4 + L
    return False

G = len(gruppi); nv = G * NF
vs = [s for g in gruppi for s in g['sizes']]
vstart = [g['video'] + sum(g['sizes'][:k]) for g in gruppi for k in range(NF)]
chiave = [i + 1 for i in range(nv) if idr(vstart[i], vstart[i] + vs[i])]
# l'ultimo gruppo di fotogrammi (GOP) è incompleto: i fotogrammi B in fondo si appoggiano a uno che manca.
# Si tiene solo fino all'ultimo fotogramma chiave escluso, arrotondato ai blocchi interi.
if len(chiave) >= 2 and nv - (chiave[-1] - 1) < chiave[1] - chiave[0]:
    G = max((chiave[-1] - 1) // NF, 1); gruppi = gruppi[:G]; nv = G * NF
    vs = vs[:nv]; vstart = vstart[:nv]; chiave = [k for k in chiave if k <= nv]
    fine_dati = gruppi[-1]['audio'] + AS

# ---- nuovo indice, partendo da quello del modello
def u32(x): return struct.pack('>I', x)
def atom(t, payload): return struct.pack('>I', 8 + len(payload)) + t + payload
def stco(offs):
    if max(offs) < 2 ** 32: return atom(b'stco', b'\0' * 4 + u32(len(offs)) + b''.join(u32(o) for o in offs))
    return atom(b'co64', b'\0' * 4 + u32(len(offs)) + b''.join(struct.pack('>Q', o) for o in offs))
def ctts_nuovo(t):
    """Lo schema dei fotogrammi B si ripete uguale: si prende dal modello e si taglia alla lunghezza nuova."""
    c = mp4.leggi(fm, t); n = struct.unpack('>I', c[4:8])[0]; per_campione = []
    for k in range(n):
        cnt, off = struct.unpack('>II', c[8 + 8 * k:16 + 8 * k]); per_campione += [off] * cnt
    per_campione = per_campione[:nv]; voci = []
    for off in per_campione:
        if voci and voci[-1][1] == off: voci[-1][0] += 1
        else: voci.append([1, off])
    return atom(b'ctts', c[:4] + u32(len(voci)) + b''.join(u32(a) + u32(b) for a, b in voci))

nuove = {  # per ogni traccia: (campioni, delta, tabelle nuove)
    b'vide': (nv, dict(stsz=atom(b'stsz', b'\0' * 8 + u32(nv) + b''.join(u32(s) for s in vs)),
                       stco=stco([g['video'] for g in gruppi]),
                       stss=atom(b'stss', b'\0' * 4 + u32(len(chiave)) + b''.join(u32(k) for k in chiave)))),
    b'soun': (G * A['stsc'][0][1], dict(stsz=atom(b'stsz', b'\0' * 4 + u32(A['sizes'][0]) + u32(G * A['stsc'][0][1])),
                                        stco=stco([g['audio'] for g in gruppi]))),
    b'meta': (G * NF, dict(stsz=atom(b'stsz', b'\0' * 4 + u32(M['sizes'][0]) + u32(G * NF)),
                           stco=stco([g['meta'] for g in gruppi]))),
}
mvhd = mp4.leggi(fm, mp4.trova(top, b'moov', b'mvhd')); mts = struct.unpack('>I', mvhd[12:16] if mvhd[0] == 0 else mvhd[20:24])[0]
def con_durata(payload, pos_v0, pos_v1, valore):
    b = bytearray(payload)
    if b[0] == 0: struct.pack_into('>I', b, pos_v0, valore)
    else: struct.pack_into('>Q', b, pos_v1, valore)
    return bytes(b)
durata_film = 0
def ricostruisci(nodo, traccia=None, durate=None):
    global durata_film
    t, p, sz, hl, fig = nodo
    if fig is not None:
        if t == b'trak':
            h = mp4.leggi(fm, mp4.trova(fig, b'mdia', b'hdlr'))[8:12]
            mdhd = mp4.leggi(fm, mp4.trova(fig, b'mdia', b'mdhd')); ts = struct.unpack('>I', mdhd[12:16] if mdhd[0] == 0 else mdhd[20:24])[0]
            st = mp4.leggi(fm, mp4.trova(fig, b'mdia', b'minf', b'stbl', b'stts')); delta = struct.unpack('>I', st[12:16])[0]
            n = nuove[h][0]; dm = n * delta; df = dm * mts // ts; durata_film = max(durata_film, df)
            return atom(t, b''.join(ricostruisci(x, h, (n, delta, dm, df)) for x in fig))
        return atom(t, b''.join(ricostruisci(x, traccia, durate) for x in fig))
    payload = mp4.leggi(fm, nodo)
    if traccia:
        n, delta, dm, df = durate; tab = nuove[traccia][1]
        if t in (b'stsz', b'stss'): return tab[t.decode()]
        if t in (b'stco', b'co64'): return tab['stco']
        if t == b'stts': return atom(t, payload[:4] + u32(1) + u32(n) + u32(delta))
        if t == b'ctts': return ctts_nuovo(nodo)
        if t == b'mdhd': return atom(t, con_durata(payload, 16, 24, dm))
        if t == b'tkhd': return atom(t, con_durata(payload, 20, 28, df))
        if t == b'elst':
            b = bytearray(payload)
            if b[0] == 0: struct.pack_into('>I', b, 8, df)
            else: struct.pack_into('>Q', b, 8, df)
            return atom(t, bytes(b))
    return atom(t, payload)
moov_m = mp4.trova(top, b'moov')
trak = b''.join(ricostruisci(x) for x in moov_m[4] if x[0] == b'trak')
altri = {x[0]: x for x in moov_m[4]}
mv = atom(b'mvhd', con_durata(mvhd, 16, 24, durata_film))
moov = atom(b'moov', mv + trak + b''.join(atom(x[0], mp4.leggi(fm, x)) for x in moov_m[4] if x[0] not in (b'mvhd', b'trak')))

testa = bytearray(d[:fine_dati]); mp = mdat_m[1]
struct.pack_into('>I', testa, mp, 1); struct.pack_into('>Q', testa, mp + 8, fine_dati - mp)   # dimensione vera dei dati
with open(out, 'wb') as f: f.write(testa); f.write(moov)
print(f"blocchi recuperati: {G} ({nv} fotogrammi, {len(chiave)} fotogrammi chiave); byte usati {fine_dati} su {N}; scartati {N - fine_dati} (l'ultimo secondo incompleto)")
