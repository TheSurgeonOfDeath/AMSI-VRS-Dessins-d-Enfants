# Module for dessins

import json
from itertools import product
from readableNestedList import readableNestedList
from itertools import chain, combinations, permutations, combinations_with_replacement
from sympy.combinatorics.named_groups import SymmetricGroup
from sympy.combinatorics import Permutation, PermutationGroup
import random
from unique_permutations import unique_permutations
import numpy as np
from multiprocessing import Pool
import time
import utils

dessinsTest = {}

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def max_value(inputlist):
    return max(max(sublist) for sublist in inputlist)

def isMorphism(alpha, F, G):
    if F.nEdges % G.nEdges != 0:
        return False
    for e in range(1, len(alpha) + 1):
        # alpha fb = gb alpha
        if alpha[F.permuteBlack(e)-1] != G.permuteBlack(alpha[e-1]):
            return False
        elif alpha[F.permuteWhite(e)-1] != G.permuteWhite(alpha[e-1]):
            return False
    return True

def findValidMaps(F, G):
    if F.nEdges % G.nEdges != 0:
        return []
    return [
        tuple(perm)
        for perm in unique_permutations(
            list(G.Edges) * int(F.nEdges / G.nEdges)
        )
    ]

def findMorphisms(F, G):
    return [validMap for validMap in findValidMaps(F, G) if isMorphism(validMap, F, G)]

def areMorphic(F, G):
    return next(
        (True for validMap in findValidMaps(F, G) if isMorphism(validMap, F, G)), False
    )

def powerset(iterable):
    # source: https://docs.python.org/3/library/itertools.html#itertools-recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def areIsomorphic(F, G):
    if F.nEdges != G.nEdges: #or len(F.b) != len(G.b) or len(F.w) != len(G.w):
        return False

    #print(F.b, G.b, *zip(F.b, G.b))

    #alphas = dict(zip(F.b[0], permutations(G.b[0])))
    #print(alphas.items())
    alphas = permutations(F.Edges)

    for alpha in alphas:
        if isMorphism(alpha, F, G):
            return True

    return False


def compute(i):
    global dessinsTest
    d = dessinsTest[i]
    uniqueDessin = []

    for dessin in d:
        if not dessin.isConnected():
            continue

        iso = False
        for unique in uniqueDessin:
            if areIsomorphic(dessin, unique):
                iso = True
                break

        if not iso:
            uniqueDessin.append(dessin)


    return uniqueDessin

def generate_dessins_new(n):

    start = time.time()
    G = SymmetricGroup(n)
    Sn = list(G.generate(method = 'coset', af=False))

    # write permutations in cyclic form, make cycles tuples and rightshift +1
    SnCycles = [[tuple(e + 1 for e in cycle) for cycle in p.full_cyclic_form] for p in Sn]

    # list of pairs of permutations (in cyclic form) in Sn
    SnCyclesSquared = list(combinations_with_replacement(SnCycles, 2))

    # Find all valid dessins
    global dessinsTest
    #dessinsUnchecked = {}
    for i, pair in enumerate(SnCyclesSquared):

        des = Dessin(pair[0], pair[1])
        c = dessinsTest.get(des.semiID)

        if c is not None:
            c.append(des)

        else:
            dessinsTest[des.semiID] = [des]

    end = time.time()
    print("PREPROCESSING", end - start)

    with Pool(5) as p:
        dessins = p.map(compute, dessinsTest.keys())

    return list(chain(*dessins))

def generate_dessins_new_single(n):
    G = SymmetricGroup(n)
    Sn = list(G.generate(method = 'coset', af=False))

    # write permutations in cyclic form, make cycles tuples and rightshift +1
    SnCycles = [[tuple(e + 1 for e in cycle) for cycle in p.full_cyclic_form] for p in Sn]

    # list of pairs of permutations (in cyclic form) in Sn
    SnCyclesSquared = list(combinations_with_replacement(SnCycles, 2))

    # Find all valid dessins
    dessins = {}
    for i, pair in enumerate(SnCyclesSquared):
        des = Dessin(pair[0], pair[1])

        if not des.isConnected():
            continue

        c = dessins.get(des.semiID)

        if c is None:
            dessins[des.semiID] = [des]

        else:
            if not any(areIsomorphic(des, d) for d in c):
                c.append(des)

    return list(chain(*dessins.values()))


def generate_dessins(n):
    G = SymmetricGroup(n)
    Sn = list(G.generate(method = 'coset', af=False))

    # write permutations in cyclic form, make cycles tuples and rightshift +1
    SnCycles = [[tuple(e + 1 for e in cycle) for cycle in p.full_cyclic_form] for p in Sn]

    # list of pairs of permutations (in cyclic form) in Sn
    SnCyclesSquared = list(combinations_with_replacement(SnCycles, 2))

    # Find all valid dessins
    dessins = []
    for i, pair in enumerate(SnCyclesSquared):
        #print([len(dessins), i, len(SnCyclesSquared)])
        des = Dessin(pair[0], pair[1])
        if des.isConnected() and not any(areIsomorphic(des, d) for d in dessins):
            dessins.append(des)

            # Check opposite colouring of des
            des2 = Dessin(pair[1], pair[0])
            if not areIsomorphic(des, des2):
                dessins.append(des2)
    return dessins


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
        self.br = {}
        self.wr = {}

        self.symCycleEdges = {}

        for i in b:
            edges = self.symCycleEdges.get(len(i))
            if edges is None:
                self.symCycleEdges[len(i)] = set(i)

            else:
                edges.update(i)

        for cycle in b:
            for i, edge in enumerate(cycle):
                self.br[edge] = cycle[(i+1)%len(cycle)]

        for cycle in w:
            for i, edge in enumerate(cycle):
                self.wr[edge] = cycle[(i+1)%len(cycle)]

        #{i:j for i, j in enumerate(b)}
        self.mono = [b, w]
        self.semiID = (np.prod([primes[len(i)] for i in b]), np.prod([primes[len(i)] for i in w]))

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
                if self.mono[i] == 'b':
                    eNew = self.permuteBlack(e)
                else:
                    eNew = self.permuteWhite(e)
                dNewIdx = i - 1
                fNew = (eNew, self.monoStr[dNewIdx])
                it = 0;
                while fNew != f0:
                    it += 1
                    face.append(fNew)
                    if self.mono[dNewIdx] == 'b':
                        eNew = self.permuteBlack(eNew)
                    else:
                        eNew = self.permuteWhite(eNew)
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
        if not hasattr(self, 'EulerChi'):
            self.calcEulerChi
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

    def permuteBlack(self, n):
        return self.br[n]

    def permuteWhite(self, n):
        return self.wr[n]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
