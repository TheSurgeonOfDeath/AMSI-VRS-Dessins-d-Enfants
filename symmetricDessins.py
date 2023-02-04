from Dessin import Dessin, findMorphisms
from readableNestedList import readableNestedList

def symDes(n):
    perm = [tuple(range(1, n + 1))]
    return Dessin(perm, perm)

# 6
F = symDes(6)
G = symDes(3)
H = symDes(2)


# calculate Euler characteristics
F.calcEulerChi()
G.calcEulerChi()
H.calcEulerChi()


# morphisms
# morphisms = findMorphisms(F, G)
# print(f"Mophisms: {readableNestedList(morphisms)}")
# alpha = morphisms[1]


# Euler Characteristic
F.printEulerCharacteristic()
G.printEulerCharacteristic()
H.printEulerCharacteristic()