# Module for dessins
import json
from readableNestedList import readableNestedList
from itertools import chain, combinations, permutations, combinations_with_replacement, product
import random
from unique_permutations import unique_permutations
import numpy as np
from multiprocessing import Pool
import networkx as nx
from sympy.utilities.iterables import multiset_permutations

dessinsTest = {}

# This is for indexing for semiID. Should use a function to get them
# but cannot be bother rn
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

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
    # modified from: sympy.combinatorics.permutations cyclic_form()
    # permutations 1-indexed
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


def dessin_to_networkx(d):
    G = nx.Graph()
    for v in d.b:
        for i in range(len(v)):
            G.add_edge(f"b{v[i]}", f"e{v[(i+1)%len(v)]}")
    for w in d.w:
        for i in range(len(w)):
            G.add_edge(f"w{w[i]}", f"e{w[(i+1)%len(w)]}")
    return G

def areIsomorphic(F, G):
    if F.nEdges != G.nEdges: #or len(F.b) != len(G.b) or len(F.w) != len(G.w):
        return False
    
    def len_items(list_of_lists):
        return {len(list) for list in list_of_lists}
    
    if len_items(F.b) != len_items(G.b) or len_items(F.w) != len_items(G.w):
        return False
    # FG = dessin_to_networkx(F)
    # GG = dessin_to_networkx(G)
    # GM = nx.isomorphism.GraphMatcher(FG, GG)
    # if not GM.is_isomorphic():
    #     return False
    
    alphas = permutations(F.Edges)
    return any(isMorphism(alpha, F, G) for alpha in alphas)

# def compute(i):
#     global dessinsTest
#     d = dessinsTest[i]
#     uniqueDessins = []
#     for dessin in d:
#         if not dessin.isConnected():
#             continue
#         iso = any(areIsomorphic(dessin, unique) for unique in uniqueDessins)
#         if not iso:
#             uniqueDessins.append(dessin)
#     return uniqueDessins

# def generate_dessins(n):
#     global dessinsTest

#     SnCycles = [array2cyclic(perm) for perm in permutations(range(1, n+1))]

#     # list of pairs of permutations (in cyclic form) in Sn
#     SnCyclesSquared = list(combinations_with_replacement(SnCycles, 2))

#     # Find potential dessin
#     for des in SnCyclesSquared:
#         des = Dessin(des[0], des[1])
#         c = dessinsTest.get(des.semiID)
#         if c is not None:
#             c.append(des)
#         else:
#             dessinsTest[des.semiID] = [des]

#     with Pool(50) as p:
#         dessins = p.map(compute, dessinsTest.keys())

#     return list(chain(*dessins))

def generate_dessins_single4(n):
    SnCycles = [array2cyclic(perm) for perm in permutations(range(1, n + 1))]
    SnCyclesSquared = combinations(SnCycles, 2)

    permOfSymDes = [tuple(range(1, n + 1))]
    symDes = Dessin(permOfSymDes, permOfSymDes)

    dessins = {symDes.semiID: [symDes]}
    dessin_hashes = {symDes.semiID: {hash((tuple(map(tuple, symDes.b)), tuple(map(tuple, symDes.w))))}}

    def addIfNew(dessin):
        semiID = dessin.semiID
        h = hash((tuple(map(tuple, dessin.b)), tuple(map(tuple, dessin.w))))
        existing = dessins.get(semiID)
        if existing is None:
            dessins[semiID] = [dessin]
            dessin_hashes[semiID] = {h}
            return True
        if h not in dessin_hashes[semiID] and not any(areIsomorphic(dessin, d) for d in existing):
            existing.append(dessin)
            dessin_hashes[semiID].add(h)
            return True
        return False

    for pair in SnCyclesSquared:
        des = Dessin(pair[0], pair[1])
        if des.isConnected() and addIfNew(des):
            desOp = Dessin(pair[1], pair[0])
            addIfNew(desOp)

    return list(chain(*dessins.values()))

from multiprocessing import Pool, cpu_count

def _process_dessin_pair(pair):
    """Generate connected dessins from a pair and its opposite if connected."""
    results = []
    des = Dessin(pair[0], pair[1])
    if des.isConnected():
        results.append(des)
    des_op = Dessin(pair[1], pair[0])
    if des_op.isConnected():
        results.append(des_op)
    return results

def generate_dessins_single_fast(n):
    SnCycles = [array2cyclic(perm) for perm in permutations(range(1, n + 1))]
    SnCyclesSquared = list(combinations(SnCycles, 2))

    # Include the symmetric dessin (identity, identity)
    permOfSymDes = [tuple(range(1, n + 1))]
    symDes = Dessin(permOfSymDes, permOfSymDes)
    dessins = {symDes.semiID: [symDes]}
    dessin_hashes = {symDes.semiID: {hash((tuple(map(tuple, symDes.b)), tuple(map(tuple, symDes.w))))}}

    def addIfNew(dessin):
        semiID = dessin.semiID
        h = hash((tuple(map(tuple, dessin.b)), tuple(map(tuple, dessin.w))))
        existing = dessins.get(semiID)
        if existing is None:
            dessins[semiID] = [dessin]
            dessin_hashes[semiID] = {h}
            return True
        if h not in dessin_hashes[semiID] and not any(areIsomorphic(dessin, d) for d in existing):
            existing.append(dessin)
            dessin_hashes[semiID].add(h)
            return True
        return False

    # Use multiprocessing to evaluate valid connected dessins
    with Pool(processes=min(cpu_count(), 8)) as pool:
        all_dessins = pool.map(_process_dessin_pair, SnCyclesSquared)

    # Flatten and filter
    for dessin_list in all_dessins:
        for des in dessin_list:
            addIfNew(des)

    return list(chain(*dessins.values()))


def _process_pair_for_dessin(pair):
    # This must be at module level for pickling!
    results = []
    des = Dessin(pair[0], pair[1])
    if not des.isConnected():
        return results
    hashDessin(des, results)
    # Check opposite colouring
    desOp = Dessin(pair[1], pair[0])
    hashDessin(desOp, results)
    return results

def hashDessin(arg0, results):
    h = hash((tuple(map(tuple, arg0.b)), tuple(map(tuple, arg0.w))))
    semiID = arg0.semiID
    results.append((semiID, h, arg0))

def generate_dessins_single3(n):
    """
    Generates all unique, connected dessins of size n, using a hash of a canonical tuple
    representation for fast uniqueness checks before isomorphism testing.
    This version parallelizes the outer loop using multiprocessing.
    """
    SnCycles = [array2cyclic(perm) for perm in permutations(range(1, n+1))]
    SnCyclesSquared = combinations(SnCycles, 2)
    permOfSymDes = [tuple(range(1, n+1))]
    symDes = Dessin(permOfSymDes, permOfSymDes)
    dessins = {symDes.semiID: [symDes]}
    dessin_hashes = {symDes.semiID: {hash((tuple(map(tuple, symDes.b)), tuple(map(tuple, symDes.w))))}}

    with Pool(processes=cpu_count()) as pool:
        all_results = pool.map(_process_pair_for_dessin, SnCyclesSquared)

    # Flatten results and filter for uniqueness
    for result_list in all_results:
        for semiID, h, des in result_list:
            dessinsWithSameSemiID = dessins.get(semiID)
            hashes = dessin_hashes.get(semiID, set())
            if dessinsWithSameSemiID is None:
                dessins[semiID] = [des]
                dessin_hashes[semiID] = {h}
            elif h not in hashes and not any(areIsomorphic(des, d) for d in dessinsWithSameSemiID):
                dessinsWithSameSemiID.append(des)
                hashes.add(h)
                dessin_hashes[semiID] = hashes

    return list(chain(*dessins.values()))

def generate_dessins_single2(n):
    """
    Generates all unique, connected dessins of size n, using a hash of a canonical tuple
    representation for fast uniqueness checks before isomorphism testing.
    """
    SnCycles = [array2cyclic(perm) for perm in permutations(range(1, n+1))]
    SnCyclesSquared = combinations(SnCycles, 2)
    permOfSymDes = [tuple(range(1, n+1))]
    symDes = Dessin(permOfSymDes, permOfSymDes)
    dessins = {symDes.semiID: [symDes]}
    dessin_hashes = {symDes.semiID: {hash((tuple(map(tuple, symDes.b)), tuple(map(tuple, symDes.w))))}}

    def addedDes(des):
        # Use a tuple of tuples for a fast, hashable, canonical representation
        h = hash((tuple(map(tuple, des.b)), tuple(map(tuple, des.w))))
        dessinsWithSameSemiID = dessins.get(des.semiID)
        hashes = dessin_hashes.get(des.semiID, set())
        if dessinsWithSameSemiID is None:
            dessins[des.semiID] = [des]
            dessin_hashes[des.semiID] = {h}
            return True
        elif h not in hashes and not any(areIsomorphic(des, d) for d in dessinsWithSameSemiID):
            dessinsWithSameSemiID.append(des)
            hashes.add(h)
            dessin_hashes[des.semiID] = hashes
            return True
        return False

    for pair in SnCyclesSquared:
        des = Dessin(pair[0], pair[1])
        if not des.isConnected():
            continue
        if addedDes(des):
            desOp = Dessin(pair[1], pair[0])
            addedDes(desOp)
    return list(chain(*dessins.values()))


def generate_dessins_single(n):
    SnCycles = [array2cyclic(perm) for perm in permutations(range(1, n+1))]

    # list of pairs of permutations (in cyclic form) in Sn
    SnCyclesSquared = combinations(SnCycles, 2)

    # symmetric dessin - repeated combination
    permOfSymDes = [tuple(range(1, n+1))]
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

def generate_all_dessins(n):
    SnCycles = [array2cyclic(perm) for perm in permutations(range(1, n+1))]

    # list of pairs of permutations (in cyclic form) in Sn
    SnCyclesSquared = list(combinations(SnCycles, 2))

    dessins = []
    for i, pair in enumerate(SnCyclesSquared):
        print([len(dessins), i, len(SnCyclesSquared)])
        des = Dessin(pair[0], pair[1])
        if des.isConnected():
            dessins.append(des)
            des.calcEulerChi()
            if des.EulerChi < -4:
                print(des.EulerChi)
                return
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
        # self.semiID = (int(np.prod([primes[len(i)] for i in b])), int(np.prod([primes[len(i)] for i in w])))
        self.semiID = (tuple(sorted(len(i) for i in b)), tuple(sorted(len(i) for i in w)))

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
                eNew = self.permuteBlack(e) if self.monoStr[i] == 'b' else self.permuteWhite(e)
                dNewIdx = i - 1
                fNew = (eNew, self.monoStr[dNewIdx])
                it = 0
                while fNew != f0:
                    it += 1
                    face.append(fNew)
                    eNew = self.permuteBlack(eNew) if self.monoStr[dNewIdx] == 'b' else self.permuteWhite(eNew)
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

    def printEulerChi(self):
        if not hasattr(self, 'EulerChi'):
            self.calcEulerChi()
        print(f"Faces: {readableNestedList(self.Faces)}")
        print(f"Initial edges: {self.initFaces}")
        print(f"No. faces: {self.nFaces}")
        print(f"No. edges: {self.nEdges}")
        print(f"No. vertices: {self.nVertices}")
        print(f"Euler Characteristic: {self.EulerChi}")

    # def isConnected(self):
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

        from collections import deque
        queue = deque([0])
        visited = {0}
        # Build adjacency for each edge
        adj = [[] for _ in range(self.nEdges)]
        for cycle in self.b:
            for i in range(len(cycle)):
                a, b = cycle[i], cycle[(i+1)%len(cycle)]
                adj[a-1].append(b-1)
                adj[b-1].append(a-1)
        for cycle in self.w:
            for i in range(len(cycle)):
                a, b = cycle[i], cycle[(i+1)%len(cycle)]
                adj[a-1].append(b-1)
                adj[b-1].append(a-1)
        # BFS
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited) == self.nEdges

    def permuteBlack(self, n):
        return self.br[n]

    def permuteWhite(self, n):
        return self.wr[n]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
