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

# isomorphic2F = [Dessin(applyPermutation(alpha, F.b), applyPermutation(alpha, F.w)) for alpha in alphas]
# print(readableNestedList(isomorphic2F))
