from unique_permutations import unique_permutations
import time
from itertools import permutations, combinations_with_replacement
from Dessin import array2cyclic
from sympy.combinatorics.named_groups import SymmetricGroup


# base = list(range(1,3)) * 4
n = 10
base = range(1,n + 1)

tic = time.perf_counter_ns()
p3 = [array2cyclic(perm) for perm in permutations(base)]
toc = time.perf_counter_ns()
print(f"p3: {toc - tic}")
# print(p3)

tic = time.perf_counter_ns()
p1 = [array2cyclic(perm) for perm in unique_permutations(base)]
toc = time.perf_counter_ns()
print(f"p1: {toc - tic}")

# tic = time.perf_counter_ns()
# p2 = ([array2cyclic(perm) for perm in unique_permutations(base)])
# toc = time.perf_counter_ns()
# print(f"p2: {toc - tic}")
# print(p2)


tic = time.perf_counter_ns()
G = SymmetricGroup(n)
Sn = list(G.generate(method = 'coset', af=False))

# write permutations in cyclic form, make cycles tuples and rightshift +1
SnCycles = [[tuple(e + 1 for e in cycle) for cycle in p.full_cyclic_form] for p in Sn]
toc = time.perf_counter_ns()
print(f"sympy: {toc - tic}")




# print(p1)
# print(p2)
# print(p3)