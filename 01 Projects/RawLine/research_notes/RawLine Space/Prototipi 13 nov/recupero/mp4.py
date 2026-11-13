"""Lettore minimo di MP4/MOV: atomi e tabelle delle tracce."""
import struct
CONT = {b'moov', b'trak', b'mdia', b'minf', b'stbl', b'edts', b'dinf', b'udta'}
def atomi(f, start, end):
    out = []; p = start
    while p + 8 <= end:
        f.seek(p); h = f.read(16); sz, t = struct.unpack('>I4s', h[:8]); hl = 8
        if sz == 1: sz = struct.unpack('>Q', h[8:16])[0]; hl = 16
        elif sz == 0: sz = end - p
        out.append((t, p, sz, hl)); p += sz
    return out
def albero(f, start, end):
    res = []
    for t, p, sz, hl in atomi(f, start, end):
        res.append((t, p, sz, hl, albero(f, p + hl, p + sz) if t in CONT else None))
    return res
def trova(nodi, *path):
    for t, p, sz, hl, fig in nodi:
        if t == path[0]: return (t, p, sz, hl, fig) if len(path) == 1 else trova(fig or [], *path[1:])
def leggi(f, nodo):
    t, p, sz, hl, _ = nodo; f.seek(p + hl); return f.read(sz - hl)
def tracce(path):
    f = open(path, 'rb'); import os; size = os.path.getsize(path); top = albero(f, 0, size); out = []
    moov = trova(top, b'moov')
    for n in moov[4]:
        if n[0] != b'trak': continue
        tr = n[4]; hd = leggi(f, trova(tr, b'mdia', b'hdlr'))[8:12]
        stbl = trova(tr, b'mdia', b'minf', b'stbl')[4]
        sd = leggi(f, trova(stbl, b'stsd')); codec = sd[12:16]
        sz = leggi(f, trova(stbl, b'stsz')); uni, cnt = struct.unpack('>II', sz[4:12])
        sizes = [uni] * cnt if uni else list(struct.unpack('>%dI' % cnt, sz[12:12 + 4 * cnt]))
        co = trova(stbl, b'stco') or trova(stbl, b'co64'); cd = leggi(f, co); nch = struct.unpack('>I', cd[4:8])[0]
        offs = list(struct.unpack('>%d%s' % (nch, 'I' if co[0] == b'stco' else 'Q'), cd[8:8 + nch * (4 if co[0] == b'stco' else 8)]))
        sc = leggi(f, trova(stbl, b'stsc')); ne = struct.unpack('>I', sc[4:8])[0]
        stsc = [struct.unpack('>III', sc[8 + 12 * k: 20 + 12 * k]) for k in range(ne)]
        out.append(dict(handler=hd, codec=codec, sizes=sizes, offsets=offs, stsc=stsc, nodo=n))
    return f, top, out
