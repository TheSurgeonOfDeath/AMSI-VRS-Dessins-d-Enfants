from Dessin import Dessin, findMorphisms, randDessin
from readableNestedList import readableNestedList
import random
import jsonpickle


random.seed(8)
F = randDessin(12)
print(F.isConnected())
F.calcEulerChi()
F.printEulerCharacteristic()

with open(f"data/dessins_order({n}).json", 'r') as f:
    loadedDessins = jsonpickle.decode(f.read())




# random.seed(9)
# G = randDessin(6)
# print(G.isConnected())
# G.calcEulerChi()
# G.printEulerCharacteristic()