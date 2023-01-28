from Dessin import Dessin
from sympy.combinatorics import Permutation, PermutationGroup
from sympy import init_printing
init_printing(perm_cyclic=True, pretty_print=False)
import time

fb = [(1,3,2),(4,5),(6,7),(8,9)]
fw = [(1,5),(2,3,4),(7,8),(9,6)]
F = Dessin(fb, fw)

gb = [(1,3,2),(4,5),(10,6,7),(8,9)]
gw = [(1,5),(2,3,4,10),(7,8),(9,6)]
G = Dessin(gb, gw)

tic = time.perf_counter()
print(F.isConnected())
print(G.isConnected())
toc = time.perf_counter()
print(f"Brute check connected time: {toc - tic:0.4f} seconds")

def perm_zero_index(perm):
    return [tuple(e - 1 for e in cycle) for cycle in perm]

def isConnected2(F):
    pfb = Permutation(perm_zero_index(F.b))
    pfw = Permutation(perm_zero_index(F.w))
    Fgrp = PermutationGroup(pfb, pfw)
    return Fgrp.is_transitive()

tic = time.perf_counter()
print(isConnected2(F))
print(isConnected2(G))
toc = time.perf_counter()
print(f"Sympy check connected time: {toc - tic:0.4f} seconds")


        
