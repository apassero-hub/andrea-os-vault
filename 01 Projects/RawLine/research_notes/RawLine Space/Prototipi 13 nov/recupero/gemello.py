"""Ricostruisce l'intestazione rovinata di un RAW TIFF (ARW, DNG, CR2) da uno scatto "gemello" della stessa fotocamera.
uso: gemello.py <rovinato> <gemello> <uscita> <byte rovinati dall'inizio>
Prende dal gemello la parte rovinata, poi rimette al posto giusto i puntatori ai dati del file rovinato
(tessere del RAW), che si ritrovano cercandone l'inizio nel file stesso."""
import sys, struct, tiff
rov, gem, out, K = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
a = bytearray(open(rov, 'rb').read()); g = open(gem, 'rb').read()
le = g[:2] == b'II'; e = '<' if le else '>'
nuovo = bytearray(a); nuovo[:K] = g[:K]
# l'immagine piena nel gemello
piena = [t for t in tiff.leggi(gem) if t.get(254, (0, 0, [None]))[2] == [0] and (324 in t or 273 in t)][0]
if 273 in piena:   # striscia unica (ARW compresso Sony o non compresso): lunghezza fissa, sta in fondo al file
    lun = piena[279][2][0]; inizio = len(a) - lun
    nuovo = bytearray(a); K = min(K, inizio); nuovo[:K] = g[:K]   # mai sopra i dati RAW del file
    pos = piena[273][3] if piena[273][3] is not None else piena[273][4]   # dove sta il puntatore nel gemello
    struct.pack_into(e + 'I', nuovo, pos, inizio)
    open(out, 'wb').write(nuovo); print(f"intestazione presa dal gemello: {K} byte; dati RAW ricollegati a {inizio}"); sys.exit(0)
n = piena[324][1]; off_arr, cnt_arr = piena[324][3], piena[325][3]
# le tessere del file rovinato: ogni tessera è un JPEG senza perdita che comincia con FFD8 FFC3
start = []; i = K
while len(start) < n:
    j = a.find(b'\xff\xd8\xff\xc3', i)
    if j < 0: break
    start.append(j); i = j + 4
if len(start) != n: sys.exit(f"tessere trovate {len(start)} su {n}: non ricostruibile così")
fine_dati = a.find(b'\xff\xd9', start[-1]) + 2
lun = [start[k + 1] - start[k] for k in range(n - 1)] + [fine_dati - start[-1]]
# la fotocamera scrive le tessere sempre nello stesso ordine (per la A7 IV: per colonne): lo dice il gemello
ordine = sorted(range(n), key=lambda k: piena[324][2][k])
for pos, k in enumerate(ordine):   # la tessera k-esima nel file va al suo posto nell'immagine
    struct.pack_into(e + 'I', nuovo, off_arr + 4 * k, start[pos]); struct.pack_into(e + 'I', nuovo, cnt_arr + 4 * k, lun[pos])
open(out, 'wb').write(nuovo)
print(f"intestazione presa dal gemello: {K} byte; {n} tessere del file rovinato ritrovate e ricollegate")
