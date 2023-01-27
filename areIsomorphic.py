from Dessin import Dessin, isMorphism
from itertools import permutations

fb = [(1,2,3,4)]
fw = [(4,3,2,1)]
F = Dessin(fb, fw)

gb = [(2,1,3,4)]
gw = [(4,3,1,2)]
G = Dessin(gb, gw)

def areIsomorphic(F, G):
    if F.nEdges != G.nEdges:
        return False
    alphas = list(permutations(F.Edges))
    return any(isMorphism(alpha, F, G) for alpha in alphas)

print(areIsomorphic(F, G))

