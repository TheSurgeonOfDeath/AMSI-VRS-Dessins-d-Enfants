# Find the Euler characteristic of a dessin given the black and white permutations

# from Dessin_Morphisms import permute, max_value
from Dessin import Dessin, findMorphisms
from readableNestedList import readableNestedList

# Fat square
# b = [(1,3,2,4), (5,8,6,7)]
# w = [(1,8,2,7), (3,6,4,5)]
# F = Dessin(b, w)

# square
fb = [(1,2), (3,4)]
fw = [(1,4), (2,3)]
F = Dessin(fb, fw)

# 2-torus
# b = [(1,7,2,3), (4,6,5)]
# w = [(1,2,6,7,5), (3,4)]
# F = Dessin(b, w)

# 4-onion
gb = [(1,2,3,4)]
gw = [(1,3,4,2)]
G = Dessin(gb, gw)

morphs = findMorphisms(G,F)
print(readableNestedList(morphs))

F.printEulerCharacteristic()
G.printEulerCharacteristic()