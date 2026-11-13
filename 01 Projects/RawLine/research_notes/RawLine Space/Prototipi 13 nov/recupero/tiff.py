import struct
TIPI = {1:1,2:1,3:2,4:4,5:8,7:1,9:4,10:8,11:4,12:8,13:4}
def ifd(f, off, le):
    e = '<' if le else '>'; f.seek(off); n = struct.unpack(e+'H', f.read(2))[0]; tags = {}
    for _ in range(n):
        voce = f.tell(); t, ty, cnt, val = struct.unpack(e+'HHI4s', f.read(12)); sz = TIPI.get(ty, 1) * cnt
        if sz > 4:
            vo = struct.unpack(e+'I', val)[0]; pos = f.tell(); f.seek(vo); raw = f.read(min(sz, 1 << 16)); f.seek(pos)
        else: raw = val[:sz]; vo = None
        if ty == 3: v = list(struct.unpack(e+'%dH' % cnt, raw[:2*cnt])) if len(raw) >= 2*cnt else []
        elif ty in (4, 13): v = list(struct.unpack(e+'%dI' % cnt, raw[:4*cnt])) if len(raw) >= 4*cnt else []
        elif ty == 2: v = raw.rstrip(b'\0').decode(errors='replace')
        else: v = raw
        tags[t] = (ty, cnt, v, vo, voce + 8)
    nxt = struct.unpack(e+'I', f.read(4))[0]
    return tags, nxt
def leggi(p):
    """Restituisce elenco IFD (principale, sotto-IFD) e dati utili del RAW."""
    with open(p, 'rb') as f:
        h = f.read(8); le = h[:2] == b'II'; e = '<' if le else '>'
        off = struct.unpack(e+'I', h[4:8])[0]; ifds = []; seen = set()
        while off and off not in seen and len(ifds) < 8:
            seen.add(off); t, off = ifd(f, off, le); ifds.append(t)
            for s in (t.get(330, (0, 0, [], 0))[2] or []):
                try: ifds.append(ifd(f, s, le)[0])
                except Exception: pass
    return ifds
def info(p):
    ifds = leggi(p); out = {}
    for t in ifds:
        if 271 in t: out['marca'] = t[271][2]
        if 272 in t: out['modello'] = t[272][2]
        if 254 in t and t[254][2] == [0] and 259 in t and 256 in t:  # immagine piena
            out.update(compressione=t[259][2][0], larghezza=t[256][2][0], altezza=t[257][2][0],
                       inizio=(t.get(273) or t.get(324))[2][0] if (t.get(273) or t.get(324)) else None,
                       byte=sum((t.get(279) or t.get(325))[2]) if (t.get(279) or t.get(325)) else None,
                       bit=t.get(258, (0, 0, [0]))[2][0], tile=324 in t)
    return out
