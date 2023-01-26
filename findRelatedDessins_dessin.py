from Dessin_Morphisms import max_value
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

b = [(1,2,3,4,5,6,7,8)]
w = [(8,7,6,5,4,3,2,1)]

nEdges = max_value(b)
facts = factors(nEdges)

# dessins = []
# for fact in facts:
#     for i in range(1, fact + 1):


