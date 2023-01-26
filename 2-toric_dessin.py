from Dessin import Dessin, findMorphisms
from readableNestedList import readableNestedList

b = [(1,7,2,3), (4,6,5)]
w = [(1,2,6,7,5), (3,4)]
F = Dessin(b, w)

F.printEulerCharacteristic()