from Dessin import Dessin
import jsonpickle

with open("data/dessins_order(6)_old.json", 'r') as f:
    dessins = jsonpickle.decode(f.read())

for i, des in enumerate(dessins):
    dessins[i] = Dessin(des.b, des.w)
    dessins[i].calcEulerChi()

with open("data/dessins_order(6).json", 'w') as f:
    f.write(jsonpickle.encode(dessins, indent = 4))