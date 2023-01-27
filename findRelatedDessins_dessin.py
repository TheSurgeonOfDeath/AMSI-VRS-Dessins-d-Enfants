# Find all dessins that a given dessin can be morphed to

from Dessin import Dessin, findMorphisms
from functools import reduce

def factors(n):   
    # source: https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python 
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

b = [(1,2,3,4,5,6,7,8)]
w = [(8,7,6,5,4,3,2,1)]
F = Dessin(b, w)


facts = factors(F.nEdges)
print(facts)

# dessins = []
# for fact in facts:
#     for i in range(1, fact + 1):
