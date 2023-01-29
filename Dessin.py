# Module for dessins

import json
from itertools import product
from readableNestedList import readableNestedList
from itertools import chain, combinations, permutations, combinations_with_replacement
from sympy.combinatorics.named_groups import SymmetricGroup
from sympy.combinatorics import Permutation, PermutationGroup
import random

def max_value(inputlist):
    return max(max(sublist) for sublist in inputlist)

def permute(permutation, n):
    for row in permutation:
        for i in range(len(row)):
            if row[i] == n:
                return row[(i + 1) % len(row)]

def isMorphism(alpha, F, G):
    for e in range(1, len(alpha) + 1):
    #alpha fb = gb alpha
        if alpha[permute(F.b, e)-1] != permute(G.b, alpha[e-1]):
            return False
        elif alpha[permute(F.w, e)-1] != permute(G.w, alpha[e-1]):
            return False
    return True

def findMorphisms(F, G):
    nEdgesF = max_value(F.b)
    nEdgesG = max_value(G.b)
    Maps = list(product(range(1, nEdgesG + 1), repeat = nEdgesF))
    surjMaps = [Map for Map in Maps if set(range(1, nEdgesG + 1)) <= set(Map)]
    return [surjMap for surjMap in surjMaps if isMorphism(surjMap, F, G)]

def powerset(iterable):
    # source: https://docs.python.org/3/library/itertools.html#itertools-recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def areIsomorphic(F, G):
    if F.nEdges != G.nEdges:
        return False
    alphas = list(permutations(F.Edges))
    return any(isMorphism(alpha, F, G) for alpha in alphas)

def generate_dessins(n):
    G = SymmetricGroup(n)
    Sn = list(G.generate(method = 'coset', af=False))

    # write permutations in cyclic form, make cycles tuples and rightshift +1
    SnCycles = [[tuple(e + 1 for e in cycle) for cycle in p.full_cyclic_form] for p in Sn]

    # list of pairs of permutations (in cyclic form) in Sn
    SnCyclesSquared = list(combinations_with_replacement(SnCycles, 2))

    # Find all valid dessins
    dessins = []
    for pair in SnCyclesSquared:
        des = Dessin(pair[0], pair[1])
        if des.isConnected() and not any(areIsomorphic(des, d) for d in dessins):
            dessins.append(des)

            # Check opposite colouring of des
            des2 = Dessin(pair[1], pair[0])
            if not areIsomorphic(des, des2):
                dessins.append(des2)


# A function to generate a random permutation of arr[]
def randomise(arr):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(len(arr)-1,0,-1):
        # Pick a random index from 0 to i
        j = random.randint(0,i)
 
        # Swap arr[i] with the element at random index
        arr[i],arr[j] = arr[j],arr[i]
    return arr


def randPerm(n):
    return [tuple(e + 1 for e in cycle) for cycle in Permutation(randomise(list(range(n)))).full_cyclic_form]

def randDessin(n):
    return Dessin(randPerm(n), randPerm(n))


class Dessin:
    monoStr = ['b', 'w']
    def __init__(self, b, w):
        # permutations
        self.b = b
        self.w = w
        self.mono = [b, w]
        
        # Euler characteristic
        # self.Faces = self.findFaces()
        # self.initFaces = self.faces2init()
        # self.nFaces = len(self.Faces)
        self.nEdges = max_value(self.b)
        self.Edges = range(1, self.nEdges + 1)
        # self.Vertices = self.b + self.w
        # self.nVertices = len(self.b) + len(self.w)
        # self.EulerChi = self.nVertices - self.nEdges + self.nFaces

    def findFaces(self):
        faces = []
        nEdges = max_value(self.b)
        for e in range(1, nEdges + 1):
            for i in range(len(self.monoStr)):
                face = []
                f0 = (e, self.monoStr[i])
                if any(f0 in face for face in faces):
                    continue
                face.append(f0)
                eNew = permute(self.mono[i], e)
                dNewIdx = i - 1
                fNew = (eNew, self.monoStr[dNewIdx])
                it = 0;
                while fNew != f0:
                    it += 1
                    face.append(fNew)
                    eNew = permute(self.mono[dNewIdx], eNew)
                    dNewIdx = i - 1 - it % 2
                    fNew = (eNew, self.monoStr[dNewIdx])
                faces.append(face)
        return(faces)
        

    def faces2init(self):
        return [f[0] for f in self.Faces]

    def calcEulerChi(self):
        self.Faces = self.findFaces()
        self.initFaces = self.faces2init()
        self.nFaces = len(self.Faces)
        # self.nEdges = max_value(self.b)
        # self.Edges = range(1, self.nEdges + 1)
        self.Vertices = self.b + self.w
        self.nVertices = len(self.b) + len(self.w)
        self.EulerChi = self.nVertices - self.nEdges + self.nFaces

    def printEulerCharacteristic(self):
        print(f"Faces: {readableNestedList(self.Faces)}")
        print(f"Initial edges: {self.initFaces}")
        print(f"No. faces: {self.nFaces}")
        print(f"No. edges: {self.nEdges}")
        print(f"No. vertices: {self.nVertices}")
        print(f"Euler Characteristic: {self.EulerChi}")

    def isConnected(self):
        # For a proper subset B of cycles of b, let S be the edge set of B and
        # for a proper subset W of cycles of w, let T be the edge set of W.
        # If any S = T, the dessin is disconnected. If all S \neq T, it is connected.
        bPowerSet = list(powerset(self.b))[1:-1]
        wPowerSet = list(powerset(self.w))[1:-1]
        bSubsets = [{item for sublist in subset for item in sublist} for subset in bPowerSet]
        wSubsets = [{item for sublist in subset for item in sublist} for subset in wPowerSet]
        return all(x not in bSubsets for x in wSubsets)

    def isConnected2(self):
        # Checks if the underlying group is transitive
        perm_zero_index = lambda perm : [tuple(e - 1 for e in cycle) for cycle in perm]
        pfb = Permutation(perm_zero_index(self.b))
        pfw = Permutation(perm_zero_index(self.w))
        Fgrp = PermutationGroup(pfb, pfw)
        return Fgrp.is_transitive()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)