from Dessin import Dessin, findSurjMaps, findSurjMaps2, randDessin
import time
import random

# source
# random.seed(10)
# randDes = randDessin(12)

# fat square
fb = [(2,3,1,4), (6,7,5,8)]
fw = [(1,7,2,8), (4,5,3,6)]
F = Dessin(fb, fw)

# square
gb = [(1,2), (3,4)]
gw = [(1,4), (2,3)]
G = Dessin(gb, gw)

# 4-shell
hb = [(1,2,3,4)]
hw = [(4,3,2,1)]
H = Dessin(hb, hw)

# 2-shell
ub = [(1,2)]
uw = [(2,1)]
U = Dessin(ub, uw)

# 3-chain
vb = [(1,), (2,)]
vw = [(1,2)]
V = Dessin(vb, vw)

targets = [G, H, U, V]

tic = time.perf_counter()
print([findSurjMaps(F, des) for des in targets])
toc = time.perf_counter()
print(f"findSurjMaps time: {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# print([findSurjMaps2(F, des) for des in targets])
# toc = time.perf_counter()
# print(f"findSurjMaps2 time: {toc - tic:0.4f} seconds")

