from Dessin import Dessin, applyPermutation, array2cyclic
from itertools import permutations, combinations_with_replacement, combinations, groupby
from readableNestedList import readableNestedList
import time
import jsonpickle

n = 3
noniso_perm_pairs = []

b = [tuple(range(1,n+1))]
w = b

# while True:
#     noniso_perm_pairs.append((b, w))
#     for 

perms = [array2cyclic(perm) for perm in permutations(range(1, n+1))]
permsSquared = list(combinations(perms, 2))
print(readableNestedList(perms))
perms.sort(key=len)
permsSquared2 = list(combinations(perms, 2))
print(readableNestedList(perms))
print(readableNestedList(permsSquared))
print(readableNestedList(permsSquared2))
print(len(permsSquared))

# with open(f"data/dessins_order({n}).json", 'r') as f:
#     dessins = jsonpickle.decode(f.read())

# unique_desssins_mono = [des.mono for des in dessins]
# unique_desssins_mono.pop(1)
# unique_desssins_mono.pop(3)
# print(readableNestedList(unique_desssins_mono))


# unique_dessins_mono_indices = [permsSquared.index(tuple(mono)) for mono in unique_desssins_mono]
# print(readableNestedList(unique_dessins_mono_indices))

nonIsoPermPairs = []
for i in range(len(perms)):
    for j in range(i, len(perms)):
        nonIsoPermPairs.append((perms[i], perms[j]))
