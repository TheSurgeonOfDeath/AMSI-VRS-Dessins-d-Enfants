from sympy import init_printing
from sympy.combinatorics.named_groups import SymmetricGroup
from sympy.combinatorics import Cycle, Permutation
from sympy.combinatorics.perm_groups import PermutationGroup
from itertools import product
from Dessin import Dessin, areIsomorphic

init_printing(perm_cyclic=True, pretty_print=False)

n = 7
G = SymmetricGroup(n)
# print(G.order())
Sn = list(G.generate(method = 'coset', af=False))


# write permutations in cyclic form, make cycles tuples and rightshift +1
SnCycles = [[tuple(i + 1 for i in l) for l in p.full_cyclic_form] for p in Sn]

# list of pairs of permutations (in cyclic form) in S4
SnCyclesSquared = list(product(SnCycles, repeat = 2))
# print(S4CyclesSquared[:5])

# Find all valid dessins
dessins = []
for pair in SnCyclesSquared:
    des = Dessin(pair[0], pair[1])
    # if des.isConnected() and not any(areIsomorphic(des, d) for d in dessins):
    if des.isConnected():
        dessins.append(des)

# choose representative from each isomorphism class
# def remove_isomorphic(dessins: list[Dessin]) -> list[Dessin]:
#     classRep = []
#     for des in dessins:
#         if not any(areIsomorphic(des, rep) for rep in classRep):
#             classRep.append(des)
#     return classRep

print(len(SnCyclesSquared))
print(len(dessins))
for des in dessins: 
    des.calcEulerChi()
chis = [des.EulerChi for des in dessins]
minGenus = 2
minChi = 2 - 2 * minGenus
non_triv_chi = [chi for chi in chis if chi < minChi]
print(non_triv_chi)
# print(dessins[7].mono)
# dessins[7].printEulerCharacteristic()