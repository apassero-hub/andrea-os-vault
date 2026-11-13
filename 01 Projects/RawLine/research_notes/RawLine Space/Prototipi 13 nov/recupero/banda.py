"""Ripara nel RAW una fascia di righe rovinata (ARW compresso Sony o non compresso, striscia unica).
uso: banda.py <rovinato> <uscita> <inizio danno> <fine danno>  (byte, dal controllo ogni 64 KB)
Ogni riga rovinata si rifà copiando la riga sana più vicina con lo stesso colore del sensore
(due righe sopra o sotto), così il file resta un RAW modificabile."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import tiff
src, out, d0, d1 = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
i = tiff.info(src); W, H, s0 = i['larghezza'], i['altezza'], i['inizio']
bpp = 1 if i['compressione'] == 32767 else 2   # compresso Sony: 1 byte per pixel; non compresso: 2
riga = W * bpp; d = bytearray(open(src, 'rb').read())
rA = (d0 - s0) // riga; rB = (d1 - 1 - s0) // riga
for r in range(rA, rB + 1):
    if (r - rA) <= (rB - r): sr = rA - 2 + ((r - rA) % 2)   # metà alta: dalla riga sana sopra
    else: sr = rB + 2 - ((rB - r) % 2)                      # metà bassa: dalla riga sana sotto
    d[s0 + r * riga: s0 + (r + 1) * riga] = d[s0 + sr * riga: s0 + (sr + 1) * riga]
open(out, 'wb').write(d)
print(f"righe rifatte: {rA}-{rB} ({rB - rA + 1} su {H}), {W} pixel per riga")
