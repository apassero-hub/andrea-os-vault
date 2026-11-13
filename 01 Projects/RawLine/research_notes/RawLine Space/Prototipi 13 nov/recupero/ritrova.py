"""Ritrova foto e video cancellati leggendo un disco (o la sua immagine) byte per byte, in sola lettura.
uso: ritrova.py <disco o immagine> <cartella di uscita>
Cerca l'inizio tipico dei file (TIFF/ARW, JPEG, MP4) e ne calcola la fine dalla loro struttura interna.
Funziona quando il file è scritto in un pezzo solo (le schede formattate di fresco, quasi sempre)."""
import sys, os, mmap, struct, hashlib
img, outdir = sys.argv[1], sys.argv[2]; os.makedirs(outdir, exist_ok=True)
f = open(img, 'rb'); m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ); N = len(m)
TIPI = {1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 7: 1, 9: 4, 10: 8, 11: 4, 12: 8, 13: 4}
def fine_tiff(b):
    le = m[b:b + 2] == b'II'; e = '<' if le else '>'; fine = 8; viste = set()
    def ifd(off):
        nonlocal fine
        if off in viste or b + off + 2 > N: return
        viste.add(off); n = struct.unpack(e + 'H', m[b + off:b + off + 2])[0]
        if n > 500: return
        fine = max(fine, off + 2 + 12 * n + 4); tags = {}
        for k in range(n):
            p = b + off + 2 + 12 * k; t, ty, cnt = struct.unpack(e + 'HHI', m[p:p + 8]); sz = TIPI.get(ty, 1) * cnt
            if sz > 4: vo = struct.unpack(e + 'I', m[p + 8:p + 12])[0]; fine = max(fine, vo + sz); raw = m[b + vo:b + vo + min(sz, 1 << 16)]
            else: raw = m[p + 8:p + 8 + sz]
            if ty in (3, 4, 13) and cnt < 100000:
                fmt = 'H' if ty == 3 else 'I'; tags[t] = list(struct.unpack(e + fmt * cnt, raw[:cnt * (2 if ty == 3 else 4)]))
        for a, c in ((273, 279), (324, 325), (513, 514)):
            if a in tags and c in tags: fine = max([fine] + [o + l for o, l in zip(tags[a], tags[c])])
        for t in (330, 34665, 0xc634):
            for s in tags.get(t, []): ifd(s)
        nxt = struct.unpack(e + 'I', m[b + off + 2 + 12 * n:b + off + 6 + 12 * n])[0]
        if nxt: ifd(nxt)
    ifd(struct.unpack(e + 'I', m[b + 4:b + 8])[0]); return b + fine
def fine_jpeg(b):
    p = b + 2
    while p + 4 < N and m[p] == 0xFF:
        mk = m[p + 1]
        if mk == 0xD9: return p + 2
        L = struct.unpack('>H', m[p + 2:p + 4])[0]
        if mk == 0xDA:
            q = p + 2 + L
            while q < N - 1:
                q = m.find(b'\xff', q)
                if q < 0: return None
                if m[q + 1] == 0xD9: return q + 2
                q += 2 if (m[q + 1] == 0 or 0xD0 <= m[q + 1] <= 0xD7) else 1
                if m[q - 1] != 0 and not (0xD0 <= m[q - 1] <= 0xD7) and m[q-2] == 0xFF and m[q-1] != 0xD9: pass
            return None
        p += 2 + L
    return None
def fine_mp4(b):
    p = b
    while p + 8 <= N:
        sz, t = struct.unpack('>I4s', m[p:p + 8])
        if not t.isalpha() and t not in (b'uuid',): break
        if sz == 1: sz = struct.unpack('>Q', m[p + 8:p + 16])[0]
        if sz < 8 or p + sz > N: break
        p += sz
        if t == b'moov' and (p + 8 > N or not m[p + 4:p + 8].isalpha()): break
    return p if p > b else None
trovati = []; occupato = []
def libero(a, z): return all(z <= x or a >= y for x, y in occupato)
for nome, firma, fine, ext in ((b'mp4', b'ftyp', fine_mp4, 'MP4'), (b'tiff', b'II*\x00', fine_tiff, 'ARW'), (b'jpeg', b'\xff\xd8\xff', fine_jpeg, 'JPG')):
    p = 0
    while True:
        p = m.find(firma, p)
        if p < 0: break
        a = p - 4 if ext == 'MP4' else p
        if ext == 'MP4' and m[p + 4:p + 8] not in (b'XAVC', b'mp42', b'isom', b'qt  ', b'MSNV', b'avc1'): p += 4; continue
        if libero(a, a + 1):
            try: z = fine(a)
            except Exception: z = None
            if z and ext == 'ARW':   # Sony riempie il file di zeri fino a un multiplo di 4 KB
                z2 = a + -(-(z - a) // 4096) * 4096
                if z2 <= N and m[z:z2].count(0) == z2 - z: z = z2
            if z and z - a > 100_000 and libero(a, z):
                occupato.append((a, z)); trovati.append((a, z, ext))
        p += 4
for k, (a, z, ext) in enumerate(sorted(trovati)):
    open(os.path.join(outdir, f"ritrovato_{k:03d}.{ext}"), 'wb').write(m[a:z])
print(f"file ritrovati: {len(trovati)} ({', '.join(f'{e}: {sum(1 for x in trovati if x[2] == e)}' for e in ('ARW', 'JPG', 'MP4'))})")
