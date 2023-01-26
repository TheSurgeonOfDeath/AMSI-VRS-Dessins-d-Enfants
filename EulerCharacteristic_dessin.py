# Find the Euler characteristic of a dessin given the black and white permutations

from Dessin_Morphisms import permute, max_value
from readableNestedList import readableNestedList

# Fat square
# b = [(1,3,2,4), (5,8,6,7)]
# w = [(1,8,2,7), (3,6,4,5)]

# square
# b = [(1,2), (3,4)]
# w = [(1,4), (2,3)]

# 2-torus
# b = [(1,7,2,3), (4,6,5)]
# w = [(1,2,6,7,5), (3,4)]

# 2-torus
b = [(1,2,3,4)]
w = [(1,3,4,2)]

mono = [b, w]
monoStr = ['b', 'w']
monoDict = {'b': b, 'w': w}


def perm2str(perm):
    return monoStr[mono.index(perm)];


# count faces
faces = []
nEdges = max_value(b)
for e in range(1, nEdges + 1):
    for d in mono:
        face = []
        f0 = (e, perm2str(d))
        if any(f0 in face for face in faces):
            continue
        face.append(f0)
        eNew = permute(d, e)
        dNew = mono[mono.index(d) - 1]
        fNew = (eNew, perm2str(dNew))
        it = 0;
        while fNew != f0:
            it += 1
            face.append(fNew)
            eNew = permute(dNew, eNew)
            dNew = mono[mono.index(dNew) - 1]
            fNew = (eNew, perm2str(dNew))
        faces.append(face)


# Euler Characteristic
nVertices = len(b) + len(w)
nEdges = max_value(b)
nFaces = len(faces)
chi = nVertices - nEdges + nFaces


# Print results
def faces2init(faces):
    return [f[0] for f in faces]

print(f"Faces: {readableNestedList(faces)}")
# print(f"Initial edges: {faces2init(faces)}")
print(f"No. faces: {nFaces}")
print(f"No. edges: {nEdges}")
print(f"No. vertices: {nVertices}")
print(f"Euler Characteristic: {chi}")