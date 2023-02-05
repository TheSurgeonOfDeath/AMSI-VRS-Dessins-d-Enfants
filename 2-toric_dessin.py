from Dessin import Dessin, findMorphisms, areMorphic
from readableNestedList import readableNestedList
import jsonpickle

# 2-toric
fb = [(1,7,2,3), (4,6,5)]
fw = [(1,2,6,7,5), (3,4)]
dessinSrc = Dessin(fb, fw)
dessinSrc.calcEulerChi()


# # terminal
# gb = [(1,)]
# gw = [(1,)]
# G = Dessin(gb, gw)

dessinsTar = []
for m in [2,3]:
    with open(f"data/dessins_order({m}).json", 'r') as f:
        dessinsTar.append(jsonpickle.decode(f.read()))


morphicsPerSrc = [tar for desTari in dessinsTar for tar in desTari if areMorphic(dessinSrc, tar)]
print(len(morphicsPerSrc))

dessinSrc.printEulerChi()
[morphic.printEulerCharacteristic() for morphic in morphicsPerSrc]

# G.printEulerCharacteristic()