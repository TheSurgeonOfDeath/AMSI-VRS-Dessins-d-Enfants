from Dessin import Dessin, findMorphisms
from readableNestedList import readableNestedList

# fat square
fb = [(1,2,6), (3,4,8), (10,7,11), (5,9,12)]
fw = [(4,1,5), (2,3,7), (9,6,10), (11,8,12)]
F = Dessin(fb, fw)
F.calcEulerChi()
F.printEulerCharacteristic()