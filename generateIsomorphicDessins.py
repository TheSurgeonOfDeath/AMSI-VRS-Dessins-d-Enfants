from Dessin import Dessin, applyPermutation, array2cyclic
from itertools import permutations
from sympy.combinatorics.named_groups import SymmetricGroup
from readableNestedList import readableNestedList
import time

# fat square
fb = [(2,3,1,4), (6,7,5,8)]
fw = [(1,7,2,8), (4,5,3,6)]
F = Dessin(fb, fw)


alphas = list(permutations(F.Edges))

alphas = [array2cyclic(alpha) for alpha in alphas]
# print(readableNestedList(alphas))
# print(len(alphas))
isomorphic2F = []
for alpha in alphas:
    newb = [tuple(applyPermutation(alpha, cycle)) for cycle in F.b]
    neww = [tuple(applyPermutation(alpha, cycle)) for cycle in F.w]
    isomorphic2F.append(Dessin(newb, neww))

print(readableNestedList([des.mono for des in isomorphic2F]))
