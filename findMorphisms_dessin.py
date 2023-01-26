# Find morphisms between two given dessins

from Dessin_Morphisms import findMorphisms
from readableNestedList import readableNestedList

# test 1
# fb = [(1,2,4,3), (7,8,6,5)]
# fw = [(1,8,7,2), (3,4,5,6)]
# gb = [(1,2), (3,4)]
# gw = [(1,4), (2,3)]

fb = [(1,2,3,4,5,6,7,8)]
fw = [(8,7,6,5,4,3,2,1)]
gb = [(1,2,3,4)]
gw = [(4,3,2,1)]

morphisms = findMorphisms(fb, fw, gb, gw)

# Print results
print(f"Valid dessin morphisms: {readableNestedList(morphisms)}")
print(f"No. valid morphisms: {len(morphisms)}")
