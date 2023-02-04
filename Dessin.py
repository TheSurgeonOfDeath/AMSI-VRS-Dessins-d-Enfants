# Module for dessins

import json
from itertools import product
from readableNestedList import readableNestedList
from itertools import chain, combinations, permutations, combinations_with_replacement
# from sympy.combinatorics.named_groups import SymmetricGroup
# from sympy.combinatorics import Permutation, PermutationGroup
import random
from unique_permutations import unique_permutations

def max_value(inputlist):
    return max(max(sublist) for sublist in inputlist)

def find_in_list_of_lists(mylist, elem):
    # modified from: https://stackoverflow.com/questions/33938488/finding-the-index-of-an-element-in-nested-lists-in-python
    for sublist in mylist:
        if elem in sublist:
            return (mylist.index(sublist), sublist.index(elem))
    raise ValueError(f"{elem} is not in list")

def permute(perm, n):
    pos = find_in_list_of_lists(perm, n)
    return perm[pos[0]][(pos[1] + 1) % len(perm[pos[0]])]

def applyPermutation(perm, arr):
    return [permute(perm, n) for n in arr]

def array2cyclic(array_form):
    unchecked = [True] * len(array_form)
    cyclic_form = []
    for i in range(len(array_form)):
        if unchecked[i]:
            cycle = [i + 1]
            unchecked[i] = False
            j = i
            while unchecked[array_form[j] - 1]:
                j = array_form[j] - 1
                cycle.append(j + 1)
                unchecked[j] = False
            cyclic_form.append(tuple(cycle))
    return cyclic_form

def isMorphism(alpha, F, G):
    if F.nEdges % G.nEdges != 0:
        return False
    for e in range(1, len(alpha) + 1):
        # alpha fb = gb alpha
        if alpha[permute(F.b, e)-1] != permute(G.b, alpha[e-1]):
            return False
        elif alpha[permute(F.w, e)-1] != permute(G.w, alpha[e-1]):
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
    if F.nEdges != G.nEdges:
        return False
    alphas = list(permutations(F.Edges))
    return any(isMorphism(alpha, F, G) for alpha in alphas)

def generate_dessins(n):
    SnCycles = [array2cyclic(perm) for perm in permutations(range(1, n+1))]

    # list of pairs of permutations (in cyclic form) in Sn
    SnCyclesSquared = list(combinations_with_replacement(SnCycles, 2))

    # Find all valid dessins
    dessins = []
    for i, pair in enumerate(SnCyclesSquared):
        print([len(dessins), i, len(SnCyclesSquared)])
        des = Dessin(pair[0], pair[1])
        if des.isConnected() and not any(areIsomorphic(des, d) for d in dessins):
            dessins.append(des)

            # Check opposite colouring of des
            desOp = Dessin(pair[1], pair[0])
            if not areIsomorphic(des, desOp):
                dessins.append(desOp)
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
    return array2cyclic(randomise(list(range(n))))

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
        for e in range(1, self.nEdges + 1):
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

    # def isConnected2(self):
    #     # Checks if the underlying group is transitive
    #     perm_zero_index = lambda perm : [tuple(e - 1 for e in cycle) for cycle in perm]
    #     pfb = Permutation(perm_zero_index(self.b))
    #     pfw = Permutation(perm_zero_index(self.w))
    #     Fgrp = PermutationGroup(pfb, pfw)
    #     return Fgrp.is_transitive()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)