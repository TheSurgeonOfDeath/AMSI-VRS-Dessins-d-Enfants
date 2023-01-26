from itertools import product

def max_value(inputlist):
    return max(max(sublist) for sublist in inputlist)

def permute(permutation, n):
    for row in permutation:
        for i in range(len(row)):
            if row[i] == n:
                return row[(i + 1) % len(row)]

def isMorphism(alpha, fb, fw, gb, gw):
    for e in range(1, len(alpha) + 1):
    #alpha fb = gb alpha
        if alpha[permute(fb, e)-1] != permute(gb, alpha[e-1]):
            return(False)
        elif alpha[permute(fw, e)-1] != permute(gw, alpha[e-1]):
            return(False)
    return(True)

def findMorphisms(fb, fw, gb, gw):
    nEdgesF = max_value(fb)
    nEdgesG = max_value(gb)
    Maps = list(product(range(1, nEdgesG + 1), repeat = nEdgesF))
    surjMaps = [Map for Map in Maps if set(range(1, nEdgesG + 1)) <= set(Map)]
    return [surjMap for surjMap in surjMaps if isMorphism(surjMap, fb, fw, gb, gw)]