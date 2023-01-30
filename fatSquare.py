from Dessin import Dessin, findMorphisms
from readableNestedList import readableNestedList


# fat square
fb = [(2,3,1,4), (6,7,5,8)]
fw = [(1,7,2,8), (4,5,3,6)]
F = Dessin(fb, fw)

# square
gb = [(1,2), (3,4)]
gw = [(1,4), (2,3)]
G = Dessin(gb, gw)

# 4-shell
hb = [(1,2,3,4)]
hw = [(4,3,2,1)]
H = Dessin(hb, hw)

# 2-shell
ub = [(1,2)]
uw = [(2,1)]
U = Dessin(ub, uw)

# 3-chain
vb = [(1,), (2,)]
vw = [(1,2)]
V = Dessin(vb, vw)

# # morphisms
# morphisms = findMorphisms(F, G)
# print(f"Mophisms: {readableNestedList(morphisms)}")
# alpha = morphisms[1]


# Euler Characteristic
# F.printEulerCharacteristic()
# G.printEulerCharacteristic()
# H.printEulerCharacteristic()
# U.printEulerCharacteristic()
# V.printEulerCharacteristic()
print(findMorphisms(F,U))