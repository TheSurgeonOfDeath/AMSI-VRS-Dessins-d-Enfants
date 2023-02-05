from Dessin import Dessin
import jsonpickle
import collections
from readableNestedList import readableNestedList

dessins = []
# for n in range(7,8):
#     with open(f"data/dessins_order({n}).json", 'r') as f:
#         dessins.append(jsonpickle.decode(f.read()))

with open("data/dessins_order(7) copy2.json", 'r') as f:
    dessins.append(jsonpickle.decode(f.read()))

for des in dessins:
    des.calcEulerChi()

chis = [[des.EulerChi for des in ord] for ord in dessins]
freqNlen = [(len(ordChis), collections.Counter(ordChis)) for ordChis in chis]
print(readableNestedList(freqNlen))


