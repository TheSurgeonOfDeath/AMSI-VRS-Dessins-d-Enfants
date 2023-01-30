from Dessin import Dessin, areMorphic, randDessin
from readableNestedList import readableNestedList
import random
import jsonpickle


# chi = -4
random.seed(10)
F = randDessin(12)
print(F.isConnected())
F.calcEulerChi()
F.printEulerCharacteristic()

dessins = []
for n in range(1,5):
    with open(f"data/dessins_order({n}).json", 'r') as f:
        dessins.append(jsonpickle.decode(f.read()))
# print([len(desns) for desns in dessins])

# Find morphic dessins to F
morphicDes = []
for orderClass in dessins:
    morphicDes.extend(des for des in orderClass if areMorphic(F, des))

with open("data/morphic_dessins_to_n=12_chi=-2.json", 'w') as f:
    f.write(jsonpickle.encode(morphicDes, indent = 4))
# print([des.EulerChi for des in morphicDes])

# Load morphic dessins to F
# with open("data/morphic_dessins_to_n=12_chi=-2.json", 'r') as f:
#     morphicDes = jsonpickle.decode(f.read())


print(len(morphicDes))
for des in morphicDes:
    des.printEulerCharacteristic()




# random.seed(9)
# G = randDessin(6)
# print(G.isConnected())
# G.calcEulerChi()
# G.printEulerCharacteristic()