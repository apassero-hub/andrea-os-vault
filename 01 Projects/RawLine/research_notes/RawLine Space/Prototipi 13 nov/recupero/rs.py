"""Dati di riparazione nostri (stesso principio di PAR2: codice di Reed-Solomon, scritto da zero).
Il file si divide in k blocchi; si calcolano m blocchi di riparazione (per esempio l'1% del file).
Si possono ricostruire fino a m blocchi rovinati, ovunque siano, anche pezzi grandi.
Quali blocchi sono rovinati lo dice un controllo CRC per blocco, salvato insieme."""
import numpy as np, zlib, struct, math
# campo di Galois GF(256), polinomio 0x11d
EXP = np.zeros(512, np.uint8); LOG = np.zeros(256, np.int32); x = 1
for i in range(255):
    EXP[i] = x; LOG[x] = i; x <<= 1
    if x & 0x100: x ^= 0x11d
EXP[255:510] = EXP[:255]
def mul(a, c):   # vettore di byte × costante
    if c == 0: return np.zeros_like(a)
    r = EXP[(LOG[a] + LOG[c]) % 255]; r[a == 0] = 0; return r
def inv(c): return int(EXP[(255 - LOG[c]) % 255])
def mulc(a, b): return 0 if a == 0 or b == 0 else int(EXP[(LOG[a] + LOG[b]) % 255])
def cauchy(m, k): return [[inv(j ^ (m + i)) for i in range(k)] for j in range(m)]   # x_j = j, y_i = m+i: sempre invertibile
def blocchi(data, k):
    B = math.ceil(len(data) / k); pad = np.frombuffer(data + b"\0" * (B * k - len(data)), np.uint8)
    return pad.reshape(k, B), B
def crea(data, percento=1.0, k=200):
    m = max(1, math.ceil(k * percento / 100)); D, B = blocchi(data, k); C = cauchy(m, k)
    P = np.zeros((m, B), np.uint8)
    for j in range(m):
        for i in range(k): P[j] ^= mul(D[i], C[j][i])
    crc = [zlib.crc32(D[i].tobytes()) for i in range(k)] + [zlib.crc32(P[j].tobytes()) for j in range(m)]
    return dict(k=k, m=m, B=B, n=len(data), P=P, crc=crc)
def inverti(M):   # inversa di una matrice piccola in GF(256), Gauss-Jordan
    n = len(M); A = [row[:] + [int(i == j) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        r = next(r for r in range(c, n) if A[r][c]); A[c], A[r] = A[r], A[c]
        f = inv(A[c][c]); A[c] = [mulc(v, f) for v in A[c]]
        for r in range(n):
            if r != c and A[r][c]:
                g = A[r][c]; A[r] = [v ^ mulc(g, w) for v, w in zip(A[r], A[c])]
    return [row[n:] for row in A]
def ripara(data, rip):
    k, m, B = rip["k"], rip["m"], rip["B"]; D, _ = blocchi(data, k); D = D.copy()
    rotti = [i for i in range(k) if zlib.crc32(D[i].tobytes()) != rip["crc"][i]]
    buone = [j for j in range(m) if zlib.crc32(rip["P"][j].tobytes()) == rip["crc"][k + j]]
    if not rotti: return data, 0
    if len(rotti) > len(buone): return None, len(rotti)
    C = cauchy(m, k); usa = buone[:len(rotti)]
    S = []
    for j in usa:   # sindrome: blocco di riparazione meno il contributo dei blocchi sani
        s = rip["P"][j].copy()
        for i in range(k):
            if i not in rotti: s ^= mul(D[i], C[j][i])
        S.append(s)
    Mi = inverti([[C[j][i] for i in rotti] for j in usa])
    for a, i in enumerate(rotti):
        r = np.zeros(B, np.uint8)
        for b in range(len(usa)): r ^= mul(S[b], Mi[a][b])
        D[i] = r
    return D.tobytes()[:rip["n"]], len(rotti)
