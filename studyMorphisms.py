from Dessin import Dessin, areMorphic, randDessin
from readableNestedList import readableNestedList
import random
import jsonpickle


# chi = -2
# random.seed(10)
# F = randDessin(12)
# F = Dessin(fb, fw)
# print(F.isConnected())
# F.calcEulerChi()
# F.printEulerCharacteristic()

# 3-fat square
fb = [(1,6,2,5,3,4), (7,12,8,11,9,10)]
fw = [(4,9,5,8,6,7), (10,3,11,2,12,1)]
F = Dessin(fb, fw)
F.calcEulerChi()
F.printEulerChi()

# square
gb = [(1,2), (3,4)]
gw = [(1,4), (2,3)]
G = Dessin(gb, gw)
# print(areMorphic(F,G))

# # fat square
# hb = [(2,3,1,4), (6,7,5,8)]
# hw = [(1,7,2,8), (4,5,3,6)]
# H = Dessin(hb, hw)

dessins = []
for n in [1,2,3,4,6]:
    with open(f"data/dessins_order({n}).json", 'r') as f:
        dessins.append(jsonpickle.decode(f.read()))
# print([len(desns) for desns in dessins])

# Find morphic dessins to F
morphicDes = []
for i, orderClass in enumerate(dessins):
    for j, des in enumerate(orderClass):
        print([len(morphicDes), j, len(orderClass), i, len(dessins)])
        if areMorphic(F, des):
            morphicDes.append(des)

with open("data/morphic_dessins_to_3-fat_square.json", 'w') as f:
    f.write(jsonpickle.encode(morphicDes, indent = 4))
# print([des.EulerChi for des in morphicDes])

# # Load morphic dessins to F
# # with open("data/morphic_dessins_to_n=12_chi=-2.json", 'r') as f:
# #     morphicDes = jsonpickle.decode(f.read())


print(len(morphicDes))
chis = [des.EulerChi for des in morphicDes]
print(chis)