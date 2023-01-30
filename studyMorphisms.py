from Dessin import Dessin, areMorphic, randDessin
from readableNestedList import readableNestedList
import random
import jsonpickle


# chi = -2
random.seed(10)
F = randDessin(12)
print(F.isConnected())
F.calcEulerChi()
F.printEulerCharacteristic()

dessins = []
for n in [1,2,3,4,6]:
    with open(f"data/dessins_order({n}).json", 'r') as f:
        dessins.append(jsonpickle.decode(f.read()))
# print([len(desns) for desns in dessins])

# Find morphic dessins to F
morphicDes = []
for i, orderClass in enumerate(dessins):
    morphicDes.extend(
        (des, print([len(morphicDes), j, len(orderClass), i, len(dessins)]))
        for j, des in enumerate(orderClass) if areMorphic(F, des)
     )

with open(f"data/morphic_dessins_to_n={F.nEdges}_chi={F.EulerChi}.json", 'w') as f:
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