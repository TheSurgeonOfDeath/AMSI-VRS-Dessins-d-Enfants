from Dessin import Dessin, applyPermutation, array2cyclic
from itertools import permutations
from readableNestedList import readableNestedList

# fat square
fb = [(1,2,3), (4,5,6), (7,8)]
fw = [(1,2), (7,3,5), (4,8)]
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
