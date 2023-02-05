#from Dessin import Dessin
from Morphism import * 
from Graph import Graph

from LDessin import Dessin as Des
from Dessin import Dessin

import jsonpickle

#D4 = Dessin([[2, 1], [4, 3]], [[1, 4], [2, 3]])
#S5 = Dessin([[1,2,3,4]], [[4,3,2,1]])

# beginDoc = "\\documentclass[preview]{standalone}\n\usepacka\\usetikzlibrary{positioning,chains,fit,shapes,calc}\n\\begin{document}\n\n"
# endDoc = "\n\\end{document}\n"
for i in range(1, 7):
    with open(f"data/dessins_order({i}).json", 'r') as f:
        D = jsonpickle.decode(f.read())

    # b = D[20].b 
    # w = D[20].w

    dessin = [Des(d.b, d.w) for d in D]
    graphs = [Graph(d) for d in dessin]

    with open(f"tikz/dessins_order({i}).tex", 'w') as f:
        # f.write(beginDoc)
        for g in graphs:
            g.plot()
            f.write(g.latex())
        # f.write(endDoc)
