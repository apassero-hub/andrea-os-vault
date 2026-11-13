import os, sys, random
# rovina.py <cartella> <seme> <n> [solo-byte] : danneggia apposta n file di prova in modi diversi
root, seed, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); solo = len(sys.argv) > 4
files = sorted(os.path.relpath(os.path.join(d, f), root) for d, _, fs in os.walk(root) for f in fs if not f.startswith('.'))
random.seed(seed); scelti = random.sample(files, n)
modi = ['byte'] * n if solo else ['byte']*9 + ['blocco', 'troncato', 'troncato', 'sparito', 'sparito', 'byte'][: max(0, n-9)]
for rel, modo in zip(scelti, modi):
    p = os.path.join(root, rel); sz = os.path.getsize(p)
    if modo == 'byte':
        with open(p, 'r+b') as f: f.seek(random.randrange(sz)); b = f.read(1); f.seek(-1, 1); f.write(bytes([b[0] ^ 0x01]))
    elif modo == 'blocco':
        with open(p, 'r+b') as f: f.seek(sz // 2); f.write(b'\0' * 65536)
    elif modo == 'troncato':
        os.truncate(p, sz // 3)
    elif modo == 'sparito':
        os.remove(p)
    print(modo, rel)
