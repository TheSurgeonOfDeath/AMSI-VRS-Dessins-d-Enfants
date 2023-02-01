from Dessin import Dessin, areMorphic, findMorphisms
from readableNestedList import readableNestedList
import jsonpickle

with open("data/dessins_order(6).json", 'r') as f:
        dessins6 = jsonpickle.decode(f.read())


# # find des with 3 faces of lengths (6,3,3)
# posDes = []
# for des in dessins6:
#     flens = [len(face) for face in des.Faces]
#     if 3 in flens:
#         print(flens)

# triple 5-chain
fb = [(3,2,1),(4,5,6,9,8,7),(10,11,12)]
fw = [(1,2,3,6,5,4),(7,8,9,12,11,10)]
F = Dessin(fb, fw)

# triple 1-chain or 3-onion
gb = [(1,2,3)]
gw = [(3,2,1)]
G = Dessin(fb,fw)

print(areMorphic(F,G))
