# Module for dessins

from itertools import product
from readableNestedList import readableNestedList
from itertools import chain, combinations
from sympy.combinatorics import Permutation

def max_value(inputlist):
    return max(max(sublist) for sublist in inputlist)

def isMorphism(alpha, F, G):
    for e in range(len(alpha)):
    #alpha fb = gb alpha
        if alpha[F.b(e)] != G.b(alpha[e]):
            return(False)
        elif alpha[F.w(e)] != G.w(alpha[e]):
            return(False)
    return(True)

def findMorphisms(F, G):
    nEdgesF = max_value(F.b)
    nEdgesG = max_value(G.b)
    Maps = list(product(range(nEdgesG), repeat = nEdgesF))
    surjMaps = [Map for Map in Maps if set(range(nEdgesG)) <= set(Map)]
    return [surjMap for surjMap in surjMaps if isMorphism(surjMap, F, G)]

def powerset(iterable):
    # source: https://docs.python.org/3/library/itertools.html#itertools-recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


class Dessin:
    def __init__(self, b: Permutation, w: Permutation):
        # permutations
        self.b = b
        self.w = w
        self.mono = [b, w]
        self.monoStr = ['b', 'w']
        
        # Euler characteristic
        self.Faces = self.findFaces()
        self.initFaces = self.faces2init()
        self.nFaces = len(self.Faces)
        self.nEdges = max_value(self.b + 1)
        self.Edges = range(self.nEdges)
        self.Vertices = self.b + self.w
        self.nVertices = len(self.b) + len(self.w)
        self.EulerChi = self.nVertices - self.nEdges + self.nFaces

    def perm2str(self, perm):
        return self.monoStr[self.mono.index(perm)];

    def findFaces(self):
        faces = []
        nEdges = max_value(self.b)
        for e in range(nEdges):
            for d in self.mono:
                face = []
                f0 = (e, self.perm2str(d))
                if any(f0 in face for face in faces):
                    continue
                face.append(f0)
                eNew = d(e)
                dNew = self.mono[self.mono.index(d) - 1]
                fNew = (eNew, self.perm2str(dNew))
                it = 0;
                while fNew != f0:
                    it += 1
                    face.append(fNew)
                    eNew = dNew(eNew)
                    dNew = self.mono[self.mono.index(dNew) - 1]
                    fNew = (eNew, self.perm2str(dNew))
                faces.append(face)
        return(faces)
        

    def faces2init(self):
        return [f[0] for f in self.Faces]

    # def calcEulerChi(self):
    #     self.Faces = self.findFaces()
    #     self.initFaces = self.faces2init()
    #     self.nFaces = len(self.Faces)
    #     self.nEdges = max_value(self.b)
    #     self.Edges = range(self.nEdges)
    #     self.Vertices = self.b + self.w
    #     self.nVertices = len(self.b) + len(self.w)
    #     self.EulerChi = self.nVertices - self.nEdges + self.nFaces

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