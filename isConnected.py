from Dessin2 import Dessin

fb = [(3,2,1),(4,5),(6,7),(8,9)]
fw = [(1,5),(2,3,4),(7,8),(9,6)]
F = Dessin(fb, fw)

gb = [(3,2,1),(4,5),(10,6,7),(8,9)]
gw = [(1,5),(2,3,4,10),(7,8),(9,6)]
G = Dessin(gb, gw)

print(F.isConnected())
print(G.isConnected())
