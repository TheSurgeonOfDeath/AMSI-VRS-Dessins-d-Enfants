from LDessin import Dessin
from Morphism import Morphism

b = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16]]
w = [[1,4],[2,3],[5,8],[6,7],[9,12],[10,11],[13,16],[14,15]]
F = Dessin(b,w)
G = Dessin([[1,2]], [[1],[2]])

Ms = Morphism.findMorphisms(F,G)
print(Ms)
