from sympy import init_printing
from sympy.combinatorics.named_groups import SymmetricGroup
# from sympy.combinatorics import Cycle, Permutation
# from sympy.combinatorics.perm_groups import PermutationGroup
from itertools import product, combinations_with_replacement
from Dessin import Dessin, areIsomorphic
import time
from readableNestedList import readableNestedList

init_printing(perm_cyclic=True, pretty_print=False)

n = 5
G = SymmetricGroup(n)
# print(G.order())
Sn = list(G.generate(method = 'coset', af=False))


# write permutations in cyclic form, make cycles tuples and rightshift +1
SnCycles = [[tuple(i + 1 for i in l) for l in p.full_cyclic_form] for p in Sn]

# list of pairs of permutations (in cyclic form) in S4
# SnCyclesSquared = list(product(SnCycles, repeat = 2))
tic = time.perf_counter()
SnCyclesSquared = list(combinations_with_replacement(SnCycles, 2))
# print(S4CyclesSquared[:5])

# Find all valid dessins
dessins = []
for pair in SnCyclesSquared:
    des = Dessin(pair[0], pair[1])
    if des.isConnected() and not any(areIsomorphic(des, d) for d in dessins):
    # if des.isConnected():
        dessins.append(des)
        des2 = Dessin(pair[1], pair[0])
        if not areIsomorphic(des, des2):
            # append opposite colouring of des
            dessins.append(des2)
toc = time.perf_counter()
print(f"Product generating time: {toc - tic:0.4f} seconds")

tic = time.perf_counter()
# list of pairs of permutations (in cyclic form) in Sn
SnCyclesSquared = list(product(SnCycles, repeat = 2))

# Find all valid dessins
dessins2 = []
for pair in SnCyclesSquared:
    des = Dessin(pair[0], pair[1])
    # if des.isConnected():
    if des.isConnected() and not any(areIsomorphic(des, d) for d in dessins2):
        dessins2.append(des)
toc = time.perf_counter()
print(f"Combinations generating time: {toc - tic:0.4f} seconds")

print(len(dessins))
print(len(dessins2))
print(readableNestedList([des.mono for des in dessins]))
print(readableNestedList([des.mono for des in dessins2]))

# choose representative from each isomorphism class
# def remove_isomorphic(dessins: list[Dessin]) -> list[Dessin]:
#     classRep = []
#     for des in dessins:
#         if not any(areIsomorphic(des, rep) for rep in classRep):
#             classRep.append(des)
#     return classRep

# print(len(SnCyclesSquared))
# print(len(dessins))
# for des in dessins: 
#     des.calcEulerChi()
# chis = [des.EulerChi for des in dessins]
# minGenus = 2
# minChi = 2 - 2 * minGenus
# non_triv_chi = [chi for chi in chis if chi < minChi]
# print(non_triv_chi)
# print(dessins[7].mono)
# dessins[7].printEulerCharacteristic()