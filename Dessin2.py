# Module for dessins

import json
from readableNestedList import readableNestedList
from itertools import chain, combinations, permutations, combinations_with_replacement, product
import random
from unique_permutations import unique_permutations
import numpy as np
from multiprocessing import Pool

# Note: Permutations are applied left to right by SymPy as opposed to traditional mathematics
from sympy.combinatorics import Permutation


from sympy import sieve, prime
primes = list(sieve.primerange(100))


def isMorphism(alpha, F, G):
    if F.nEdges % G.nEdges != 0:
        return False
    for e in range(len(alpha)):
        # alpha fb = gb alpha
        if alpha[F.b(e)] != G.b(alpha[e]):
            return False
        elif alpha[F.w(e)] != G.w(alpha[e]):
            return False
    return True

def findMorphisms(F, G):
    Maps = list(product(range(G.nEdges), repeat = F.nEdges))
    surjMaps = [Map for Map in Maps if set(range(G.nEdges)) <= set(Map)]
    return [surjMap for surjMap in surjMaps if isMorphism(surjMap, F, G)]

def areIsomorphic(F, G):
    if F.nEdges != G.nEdges: #or len(F.b) != len(G.b) or len(F.w) != len(G.w):
        return False
    alphas = permutations(F.Edges)
    return any(isMorphism(alpha, F, G) for alpha in alphas)

# def powerset(iterable):
#     # source: https://docs.python.org/3/library/itertools.html#itertools-recipes
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def generate_dessins_single(n):
    SnCycles = [Permutation(perm) for perm in permutations(range(n))]

    # list of pairs of permutations (in cyclic form) in Sn
    SnCyclesSquared = list(combinations(SnCycles, 2))

    # symmetric dessin - repeated combination
    permOfSymDes = Permutation([range(n)])
    symDes = Dessin(permOfSymDes, permOfSymDes)
    
    # generate unique dessins
    dessins = {symDes.semiID: [symDes]}

    # adds unique dessins to dict dessins
    def addedDes(des):
        dessinsWithSameSemiID = dessins.get(des.semiID)
        if dessinsWithSameSemiID is None:
            dessins[des.semiID] = [des]
            return True
        elif not any(areIsomorphic(des, d) for d in dessinsWithSameSemiID):
            dessinsWithSameSemiID.append(des)
            return True
        return False

    for pair in SnCyclesSquared:
        des = Dessin(pair[0], pair[1])
        if not des.isConnected():
            continue
        
        # add des if unique
        if addedDes(des):
            # Check opposite colouring of des
            desOp = Dessin(pair[1], pair[0])
            addedDes(desOp) 
    return list(chain(*dessins.values()))




class Dessin:
    def __init__(self, b: Permutation, w: Permutation):
        # permutations
        self.b = b
        self.w = w
        self.wb = b * w
        self.mono = [b, w]
        self.monoStr = ['b', 'w']

        # semiID (because not entirely unique)
        self.semiID = (int(np.prod([primes[len(i)] for i in b.full_cyclic_form])), int(np.prod([primes[len(i)] for i in w.full_cyclic_form])))

        # edges
        self.nEdges = len(self.b.array_form)
        self.Edges = range(self.nEdges)

        # vertices
        self.Vertices = self.b.cyclic_form + self.w.cyclic_form
        self.nVertices = len(self.Vertices)

        # faces
        self.nFaces = len(self.wb.cyclic_form)

    def perm2str(self, perm):
        return self.monoStr[self.mono.index(perm)]

    def findFaces(self):
        faces = []
        for e in range(self.nEdges):
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
                
                # add faces property
                self.Faces = self.findFaces()
                self.initFaces = self.faces2init()
        # return(faces)
        

    def faces2init(self):
        return [f[0] for f in self.Faces]

    def calcEulerChi(self):
        self.nFaces = len(self.wb.cyclic_form)
        self.EulerChi = self.nVertices - self.nEdges + self.nFaces

    def printEulerChi(self):
        if not hasattr(self, 'EulerChi'):
            self.calcEulerChi()
        # print(f"Faces: {readableNestedList(self.Faces)}")
        # print(f"Initial edges: {self.initFaces}")
        print(f"No. faces: {self.nFaces}")
        print(f"No. edges: {self.nEdges}")
        print(f"No. vertices: {self.nVertices}")
        print(f"Euler Characteristic: {self.EulerChi}")

    # def isConnected2(self):
    #     # For a proper subset B of cycles of b, let S be the edge set of B and
    #     # for a proper subset W of cycles of w, let T be the edge set of W.
    #     # If any S = T, the dessin is disconnected. If all S \neq T, it is connected.
    #     bPowerSet = list(powerset(self.b))[1:-1]
    #     wPowerSet = list(powerset(self.w))[1:-1]
    #     bSubsets = [{item for sublist in subset for item in sublist} for subset in bPowerSet]
    #     wSubsets = [{item for sublist in subset for item in sublist} for subset in wPowerSet]
    #     return all(x not in bSubsets for x in wSubsets)
    
    def isConnected(self):
        """Check if the dessin is connected using BFS traversal."""
        # Build adjacency: each edge is a node, connect via black and white cycles
        queue = [0]
        visited = {0}
        # Build adjacency for each edge
        adj = [[] for _ in range(self.nEdges)]
        for cycle in self.b.cyclic_form:
            for i in range(len(cycle)):
                a, b = cycle[i], cycle[(i+1)%len(cycle)]
                adj[a].append(b)
                adj[b].append(a)
        for cycle in self.w.cyclic_form:
            for i in range(len(cycle)):
                a, b = cycle[i], cycle[(i+1)%len(cycle)]
                adj[a].append(b)
                adj[b].append(a)
        # BFS
        while queue:
            node = queue.pop(0)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited) == self.nEdges
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
