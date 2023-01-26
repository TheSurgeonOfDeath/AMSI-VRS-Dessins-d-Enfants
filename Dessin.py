# Module for dessins

from itertools import product
from readableNestedList import readableNestedList

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
            return(False)
        elif alpha[permute(F.w, e)-1] != permute(G.w, alpha[e-1]):
            return(False)
    return(True)

def findMorphisms(F, G):
    nEdgesF = max_value(F.b)
    nEdgesG = max_value(G.b)
    Maps = list(product(range(1, nEdgesG + 1), repeat = nEdgesF))
    surjMaps = [Map for Map in Maps if set(range(1, nEdgesG + 1)) <= set(Map)]
    return [surjMap for surjMap in surjMaps if isMorphism(surjMap, F, G)]


class Dessin:
    def __init__(self, b, w):
        # permutations
        self.b = b
        self.w = w
        self.mono = [b, w]
        self.monoStr = ['b', 'w']
        
        # Euler characteristic
        self.Faces = self.findFaces()
        self.initFaces = self.faces2init()
        self.nFaces = len(self.Faces)
        self.nEdges = max_value(self.b)
        self.Edges = range(1, self.nEdges + 1)
        self.Vertices = self.b + self.w
        self.nVertices = len(self.b) + len(self.w)
        self.EulerChi = self.nVertices - self.nEdges + self.nFaces

    def perm2str(self, perm):
        return self.monoStr[self.mono.index(perm)];

    def findFaces(self):
        faces = []
        nEdges = max_value(self.b)
        for e in range(1, nEdges + 1):
            for d in self.mono:
                face = []
                f0 = (e, self.perm2str(d))
                if any(f0 in face for face in faces):
                    continue
                face.append(f0)
                eNew = permute(d, e)
                dNew = self.mono[self.mono.index(d) - 1]
                fNew = (eNew, self.perm2str(dNew))
                it = 0;
                while fNew != f0:
                    it += 1
                    face.append(fNew)
                    eNew = permute(dNew, eNew)
                    dNew = self.mono[self.mono.index(dNew) - 1]
                    fNew = (eNew, self.perm2str(dNew))
                faces.append(face)
        return(faces)
        

    def faces2init(self):
        return [f[0] for f in self.Faces]

    def printEulerCharacteristic(self):
        print(f"Faces: {readableNestedList(self.Faces)}")
        print(f"Initial edges: {self.initFaces}")
        print(f"No. faces: {self.nFaces}")
        print(f"No. edges: {self.nEdges}")
        print(f"No. vertices: {self.nVertices}")
        print(f"Euler Characteristic: {self.EulerChi}")