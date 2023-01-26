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

# morphisms
morphisms = findMorphisms(F, G)
print(f"Mophisms: {readableNestedList(morphisms)}")
alpha = morphisms[1]


# Euler Characteristic
F.printEulerCharacteristic()
G.printEulerCharacteristic()
