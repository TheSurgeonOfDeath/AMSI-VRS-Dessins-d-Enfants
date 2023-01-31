from Dessin import Dessin, findValidMaps, findValidMaps2, randDessin, findMorphisms, findMorphisms2
import time
import random
from unique_permutations import unique_permutations

# source
random.seed(10)
randDes = randDessin(12)

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

targets = [F, G, H, U, V]


tic = time.perf_counter()
# M2 = [findMorphisms2(F, des) for des in targets]
M2 = findMorphisms2(randDes,G)
toc = time.perf_counter()
print(f"findMorphisms2 time: {toc - tic:0.4f} seconds")

tic = time.perf_counter()
# M1 = [findMorphisms(F, des) for des in targets]
M1 = findMorphisms(randDes,G)
toc = time.perf_counter()
print(f"findMorphisms time: {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# M3 = [findMorphisms3(F, des) for des in targets]
# # M3 = findMorphisms3(F,G)
# toc = time.perf_counter()
# print(f"findMorphisms3 time: {toc - tic:0.4f} seconds")

# print(set(M1) == set(M2))
# print(type(M1))
# print([len(m) for m in M1])
# print([len(m) for m in M2])
# print(len(M1))
# print(len(M2))
# print([set(M1[i]) == set(M2[i]) for i in range(len(M1))])
# print(M1[3])
# print(M2[3])
# print(M1)
# print(M2)
# L = list(unique_permutations((1,1,2,2)))
# L = [tuple(perm) for perm in unique_permutations((1,1,2,2))]
# print(L)
