"""Ripara un JPEG rovinato che ha i punti di ripartenza (DRI), come quasi tutti gli export di Lightroom.
uso: jpeg_ripara.py <rovinato.jpg> <uscita.jpg> <inizio zona sospetta> <fine zona sospetta>  (byte, dal controllo ogni 64 KB)
1. elenca i pezzi tra due punti di ripartenza che cadono nella zona sospetta;
2. tra questi trova quelli rovinati: i bordi non combaciano con i pixel vicini;
3. li ricostruisce dai pixel sopra e sotto. Il risultato è un file NUOVO."""
import sys, struct, numpy as np
from PIL import Image, ImageFile; ImageFile.LOAD_TRUNCATED_IMAGES = True
src, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
d = open(src, 'rb').read(); i = 2; dri = None
while i < len(d):
    m = d[i + 1]; L = struct.unpack('>H', d[i + 2:i + 4])[0]
    if m in (0xC0, 0xC1): H, W = struct.unpack('>HH', d[i + 5:i + 9]); nc = d[i + 9]
    if m in (0xC0, 0xC1): fac = [d[i + 11 + 3 * k] for k in range(nc)]; hmax = max(f >> 4 for f in fac); vmax = max(f & 15 for f in fac)
    if m == 0xC2: sys.exit("JPEG progressivo: niente punti di ripartenza")
    if m == 0xDD: dri = struct.unpack('>H', d[i + 4:i + 6])[0]
    if m == 0xDA: inizio = i + 2 + L; break
    i += 2 + L
if not dri: sys.exit("senza punti di ripartenza: il danno arriva fino in fondo; serve l'export rifatto o l'anteprima")
mw, mh = 8 * hmax, 8 * vmax; per_riga = -(-W // mw)
pos = [inizio]; j = inizio   # inizio di ogni pezzo: subito dopo ogni marcatore RSTn
while True:
    j = d.find(b'\xff', j)
    if j < 0 or j + 1 >= len(d): break
    if 0xD0 <= d[j + 1] <= 0xD7: pos.append(j + 2)
    if d[j + 1] == 0xD9: break
    j += 2 if d[j + 1] != 0 else 2
cand = [k for k in range(len(pos)) if pos[k] < b and (pos[k + 1] if k + 1 < len(pos) else len(d)) > a]
img = np.asarray(Image.open(src).convert('RGB')).astype(float)
def rett(k):   # i rettangoli di pixel di un pezzo (può andare a capo)
    out = []
    for mcu in range(k * dri, (k + 1) * dri):
        r, c = divmod(mcu, per_riga)
        if r * mh < H: out.append((r * mh, min((r + 1) * mh, H), c * mw, min((c + 1) * mw, W)))
    return out
def blocchi(k):   # i blocchi (MCU) di un pezzo, in ordine
    out = []
    for mcu in range(k * dri, (k + 1) * dri):
        r, c = divmod(mcu, per_riga)
        if r * mh < H: out.append((r * mh, min((r + 1) * mh, H), c * mw, min((c + 1) * mw, W)))
    return out
def salto(y0, y1, x0, x1):   # un blocco rovinato non combacia né con la riga sopra né con quella sotto
    if y0 < 3 or y1 > H - 3: return 0
    top = np.abs(img[y0, x0:x1] - img[y0 - 1, x0:x1]).mean(); bot = np.abs(img[y1 - 1, x0:x1] - img[y1, x0:x1]).mean()
    ref = (np.abs(np.diff(img[y0 - 3:y0, x0:x1], axis=0)).mean() + np.abs(np.diff(img[y1:y1 + 3, x0:x1], axis=0)).mean()) / 2
    return min(top, bot) / (ref + 3)
tutti = [(k, bl) for k in cand for bl in blocchi(k)]
sc = np.array([salto(*bl) for _, bl in tutti]); soglia = max(np.median(sc) * 4, 3)
# in un pezzo, dal primo blocco rovinato fino al punto di ripartenza successivo non ci si può fidare di niente
rotti = []
for k in cand:
    bl = blocchi(k); s_ = [salto(*x) for x in bl]; primo = next((n for n in range(len(s_) - 2) if min(s_[n], s_[n + 1], s_[n + 2]) > soglia), None)   # tre blocchi sospetti di fila
    if primo is not None: rotti += bl[primo:]
def rett(k): return []
x = img.copy()
for y0, y1, x0, x1 in rotti:
    if True:
        sopra = x[max(y0 - 1, 0), x0:x1]; sotto = img[min(y1, H - 1), x0:x1]
        for y in range(y0, y1):
            t = (y - y0 + 1) / (y1 - y0 + 1); x[y, x0:x1] = sopra * (1 - t) + sotto * t
Image.fromarray(np.clip(x, 0, 255).astype(np.uint8)).save(out, quality=97, subsampling=0)
print(f"punti di ripartenza ogni {dri} blocchi; pezzi nella zona sospetta: {len(cand)}; blocchi ricostruiti: {len(rotti)} ({len(rotti)*mw*mh/(W*H)*100:.3f}% dell'immagine)")
