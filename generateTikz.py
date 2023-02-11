#from Dessin import Dessin
from Morphism import *
from Graph import Graph

from LDessin import Dessin as Des
from Dessin import Dessin, applyPermutation

import jsonpickle

#D4 = Dessin([[2, 1], [4, 3]], [[1, 4], [2, 3]])
#S5 = Dessin([[1,2,3,4]], [[4,3,2,1]])

# beginDoc = "\\documentclass[preview]{standalone}\n\usepacka\\usetikzlibrary{positioning,chains,fit,shapes,calc}\n\\begin{document}\n\n"
# endDoc = "\n\\end{document}\n"
# for i in range(1, 7):
#     with open(f"data/dessins_order({i}).json", 'r') as f:
#         D = jsonpickle.decode(f.read())

#     # b = D[20].b 
#     # w = D[20].w

#     dessin = [Des(d.b, d.w) for d in D]
#     graphs = [Graph(d) for d in dessin]

#     with open(f"tikz/dessins_order({i}).tex", 'w') as f:
#         # f.write(beginDoc)
#         for g in graphs:
#             g.plot()
#             f.write(g.latex())
#         # f.write(endDoc)

with open("data/dessins_order(5).json", 'r') as f:
    dessins = jsonpickle.decode(f.read())


# normalise to (1 2 3 4 5 6 7)
complexDessins = [des for des in dessins if des.EulerChi == -2]
# for des in complexDessins:
#     print([applyPermutation([(1,), (7,2,6), (5,4,3)], *d) for d in des.mono])

# [(1, 7, 4, 5, 3, 2, 6)]
# [(6, 2, 3, 5, 4, 7, 1)]

complexDes = [Des(des.b, des.w) for des in complexDessins]
graphs = [Graph(des) for des in complexDes]

with open("tikz/dessins_order(5)_chi=-2.tex", 'w') as f:
    for i, g in enumerate(graphs):
        g.plot()
        f.write(f"%{str(complexDessins[i].mono)}\n")
        f.write(g.latex() + "\n\n")

g = Graph(Des([(1,2,3,4,5)], [(1,2,3,4,5)]))
g.plot()
print(g.latex())