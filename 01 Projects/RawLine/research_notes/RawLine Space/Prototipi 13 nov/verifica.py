#!/usr/bin/env python3
"""Verifica INDIPENDENTE dal prototipo: confronta due alberi file per file (contenuto, dimensione, date, attributi).
Non scrive niente su nessuno dei due. uso: verifica.py <A> <B> [solo-metadati]"""
import os, sys, hashlib
A, B = sys.argv[1], sys.argv[2]; solo_meta = len(sys.argv) > 3
def elenco(r):
    out = {}
    for d, ds, fs in os.walk(r):
        for f in fs:
            if f == ".DS_Store" or f.startswith(".rawline-tmp-"): continue
            p = os.path.join(d, f); out[os.path.relpath(p, r)] = p
    return out
def h(p):
    x = hashlib.sha256()
    with open(p, "rb") as f:
        while b := f.read(8 << 20): x.update(b)
    return x.hexdigest()
import ctypes
libc = ctypes.CDLL(None, use_errno=True)
XATTR_NOFOLLOW = 1
def xa(p):
    bp = os.fsencode(p)
    n = libc.listxattr(bp, None, 0, XATTR_NOFOLLOW)
    if n <= 0: return {}
    buf = ctypes.create_string_buffer(n); libc.listxattr(bp, buf, n, XATTR_NOFOLLOW)
    out = {}
    for nome in buf.raw[:n].split(b"\0"):
        if not nome or nome == b"com.apple.provenance": continue
        l = libc.getxattr(bp, nome, None, 0, 0, XATTR_NOFOLLOW)
        if l < 0: continue
        v = ctypes.create_string_buffer(max(l, 1)); libc.getxattr(bp, nome, v, l, 0, XATTR_NOFOLLOW)
        out[nome] = v.raw[:l]
    return out
a, b = elenco(A), elenco(B)
solo_a = sorted(set(a) - set(b)); solo_b = sorted(set(b) - set(a)); diff = []
for k in sorted(set(a) & set(b)):
    sa, sb = os.lstat(a[k]), os.lstat(b[k])
    prob = []
    if sa.st_size != sb.st_size: prob.append("dimensione")
    if sa.st_mtime_ns != sb.st_mtime_ns: prob.append("data modifica")
    if sa.st_birthtime != sb.st_birthtime: prob.append("data creazione")
    if xa(a[k]) != xa(b[k]): prob.append("attributi")
    if not solo_meta and not prob and h(a[k]) != h(b[k]): prob.append("CONTENUTO")
    if prob: diff.append((k, prob))
print(f"file A={len(a)} B={len(b)} solo_in_A={len(solo_a)} solo_in_B={len(solo_b)} diversi={len(diff)} -> {'IDENTICI' if not (solo_a or solo_b or diff) else 'DIFFERENZE'}")
for x in (solo_a[:5], solo_b[:5], diff[:10]):
    for y in x: print("  ", y)
