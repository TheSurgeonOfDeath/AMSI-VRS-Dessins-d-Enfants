from Dessin import Dessin, findMorphisms

fb = [(1,2,3,4)]
fw = [(4,3,2,1)]
F = Dessin(fb, fw)

gb = [(2,1,3,4)]
gw = [(4,3,1,2)]
G = Dessin(gb, gw)



print(areIsomorphic(F, G))

