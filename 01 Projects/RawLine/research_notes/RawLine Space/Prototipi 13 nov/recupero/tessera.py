"""Ripara nell'immagine sviluppata la tessera rovinata di un ARW senza perdita, con l'anteprima di Lightroom.
La tessera si conosce dal controllo ogni 64 KB; la sua posizione nell'immagine dai dati di ritaglio
e di orientamento del RAW. L'anteprima viene allineata e adattata nei colori sulla zona sana attorno.
Il risultato è un file NUOVO, segnato come ricostruito. Il RAW rovinato non si tocca.
uso: tessera.py <raw> <render rovinato .tif> <anteprima .jpg> <numero tessera> <uscita .tif>"""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import tiff
from PIL import Image, ImageFilter
raw, ren, prev, k, out = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5]
ifds = tiff.leggi(raw); t = [t for t in ifds if t.get(254, (0, 0, [None]))[2] == [0] and 324 in t][0]
ori = next((x[274][2][0] for x in ifds if 274 in x), 1)
tw, th, W0 = t[322][2][0], t[323][2][0], t[256][2][0]; cx, cy = t[0x74c7][2]; cw, ch = t[0x74c8][2]
per_riga = -(-W0 // tw); sx, sy = (k % per_riga) * tw - cx, (k // per_riga) * th - cy   # tessera nel ritaglio
r = np.asarray(Image.open(ren).convert("RGB")).astype(float); H, W, _ = r.shape
def ruota(x, y):   # coordinate del ritaglio orizzontale → coordinate dell'immagine orientata
    return {1: (x, y), 3: (cw - 1 - x, ch - 1 - y), 6: (ch - 1 - y, x), 8: (y, cw - 1 - x)}[ori]
(xa, ya), (xb, yb) = ruota(sx, sy), ruota(sx + tw - 1, sy + th - 1)
x0, x1 = sorted((xa, xb)); y0, y1 = sorted((ya, yb)); M = 6
x0, y0, x1, y1 = max(x0 - M, 0), max(y0 - M, 0), min(x1 + M + 1, W), min(y1 + M + 1, H)
pi = Image.open(prev).convert("RGB")
if (pi.width > pi.height) != (W > H):   # l'anteprima di Lightroom è salvata senza rotazione
    pi = pi.rotate({6: -90, 8: 90}.get(ori, 90), expand=True)
p = np.asarray(pi.resize((W, H), Image.LANCZOS)).astype(float)
# finestra attorno alla tessera; la tessera stessa non si usa per allineare né per i colori
F = 400; wx0, wy0, wx1, wy1 = max(x0 - F, 0), max(y0 - F, 0), min(x1 + F, W), min(y1 + F, H)
sana = np.ones((wy1 - wy0, wx1 - wx0), bool); sana[y0 - wy0:y1 - wy0, x0 - wx0:x1 - wx0] = False
g = lambda a: a[wy0:wy1, wx0:wx1].mean(2)
A, Bp = g(r), g(p); A = np.where(sana, A - A[sana].mean(), 0); Bp = np.where(sana, Bp - Bp[sana].mean(), 0)
R = np.fft.fft2(A) * np.conj(np.fft.fft2(Bp)); c = np.fft.ifft2(R / (np.abs(R) + 1e-9)).real
dy, dx = np.unravel_index(np.argmax(c), c.shape); dy = dy - c.shape[0] if dy > c.shape[0] // 2 else dy; dx = dx - c.shape[1] if dx > c.shape[1] // 2 else dx
p = np.roll(p, (dy, dx), (0, 1))
pa = np.zeros_like(p[wy0:wy1, wx0:wx1]); rw, pw = r[wy0:wy1, wx0:wx1], p[wy0:wy1, wx0:wx1]
for ch_ in range(3):
    X = np.stack([pw[..., ch_][sana] ** 2, pw[..., ch_][sana], np.ones(sana.sum())], 1)
    kk = np.linalg.lstsq(X, rw[..., ch_][sana], rcond=None)[0]; pa[..., ch_] = kk[0] * pw[..., ch_] ** 2 + kk[1] * pw[..., ch_] + kk[2]
m = Image.fromarray((~sana * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(4))
m = np.asarray(m).astype(float)[..., None] / 255
x = r.copy(); x[wy0:wy1, wx0:wx1] = np.clip(rw * (1 - m) + pa * m, 0, 255)
Image.fromarray(x.astype(np.uint8)).save(out)
print(f"tessera {k}: nell'immagine x {x0}-{x1}, y {y0}-{y1}; anteprima spostata di ({dx},{dy}) px e adattata nei colori")
