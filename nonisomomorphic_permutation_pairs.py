from Dessin import Dessin, applyPermutation, array2cyclic
from itertools import permutations, combinations_with_replacement
from readableNestedList import readableNestedList
import time

n = 3
noniso_perm_pairs = []

b = [tuple(range(1,n+1))]
w = b

# while True:
#     noniso_perm_pairs.append((b, w))
#     for 

perms = [array2cyclic(perm) for perm in permutations(range(1, n+1))]
permsSquared = list(combinations_with_replacement(perms, 2))
print(readableNestedList(perms))
print(readableNestedList(permsSquared))
