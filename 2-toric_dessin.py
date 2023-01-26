from Dessin import Dessin, findMorphisms
from readableNestedList import readableNestedList

# 2-toric
fb = [(1,7,2,3), (4,6,5)]
fw = [(1,2,6,7,5), (3,4)]
F = Dessin(fb, fw)

# terminal
gb = [(1,)]
gw = [(1,)]
G = Dessin(gb, gw)

F.printEulerCharacteristic()
G.printEulerCharacteristic()