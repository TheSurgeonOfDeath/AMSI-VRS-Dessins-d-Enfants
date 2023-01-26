from Dessin import Dessin
from itertools import chain, combinations

b = [(3,2,1),(4,5),(6,7),(8,9)]
w = [(1,5),(2,3,4),(7,8),(9,6)]
F = Dessin(b, w)

def powerset(iterable):
    # source: https://docs.python.org/3/library/itertools.html#itertools-recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def isConnected(F):
    bPowerSet = list(powerset(F.b))[1:-1]
    wPowerSet = list(powerset(F.w))[1:-1]
    bSubsets = [{item for sublist in subset for item in sublist} for subset in bPowerSet]
    wSubsets = [{item for sublist in subset for item in sublist} for subset in wPowerSet]
    return any(x in bSubsets for x in wSubsets)

# for x in wSubsets:
#     if x in bSubsets:
#         print(x)
# print([x in bSubsets for x in wSubsets])
# for sub in bPowerSet:
#     set(sub)
