from sympy import init_printing
from sympy.combinatorics.named_groups import SymmetricGroup
from sympy.combinatorics import Cycle, Permutation
from sympy.combinatorics.perm_groups import PermutationGroup

init_printing(perm_cyclic=True, pretty_print=False)

G = SymmetricGroup(8)
# print(G)
# print(G.order())
S8 = list(G.generate(method = 'coset', af=False))
S8Cycles = [perm.]
print(S8)
# print(G.is_group)


posDes = G * G



p = Permutation([1, 2, 0, 4, 5, 3, 6, 7])
print(p)
print(p in G)
# print(p)
# print(G.contains())


# [[n+2 for n in sub] for sub in all_scores]