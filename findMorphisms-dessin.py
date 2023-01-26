# Find morphisms between two given dessins

from itertools import combinations_with_replacement

# test 1
# fb = [(1,2,4,3), (7,8,6,5)]
# fw = [(1,8,7,2), (3,4,5,6)]
# gb = [(1,2), (3,4)]
# gw = [(1,4), (2,3)]


fb = [(1,2,4,3), (7,8,6,5)]
fw = [(1,8,7,2), (3,4,5,6)]
gb = [(1,2), (3,4)]
gw = [(1,4), (2,3)]



def permute(permutation, n):
    for row in permutation:
        for i in range(len(row)):
            if row[i] == n:
                return row[(i + 1) % len(row)]

def max_value(inputlist):
    return max(max(sublist) for sublist in inputlist)

def applyMap(surjMap, edge):
    return surjMap[edge]

def checkMorphism(alpha, fb, fw, gb, gw):
    for e in range(1, len(alpha) + 1):
    #alpha fb = gb alpha
        if alpha[permute(fb, e)-1] != permute(gb, alpha[e-1]):
            return(False)
        elif alpha[permute(fw, e)-1] != permute(gw, alpha[e-1]):
            return(False)
    return(True)


nEdgesF = max_value(fb)
nEdgesG = max_value(gb)
surjMaps = list(combinations_with_replacement(range(1, nEdgesG + 1), nEdgesF))
# print(surjMaps)
morphisms = [surjMap for surjMap in surjMaps if checkMorphism(surjMap, fb, fw, gb, gw)]
print(morphisms)
print(len(morphisms))
