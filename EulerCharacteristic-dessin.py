b = [(1,3,2,4), (5,8,6,7)]
w = [(1,8,2,7), (3,6,4,5)]

mono = [b, w]
monoStr = ['b', 'w']

monoDict = {'b': b, 'w': w}

def permute(permutation, n):
    for row in permutation:
        for i in range(len(row)):
            if row[i] == n:
                return row[(i + 1) % len(row)]

def max_value(inputlist):
    return max(max(sublist) for sublist in inputlist)

def perm2str(perm):
    return monoStr[mono.index(perm)];

def readableNestedList(nestedList):
    nestedListStr = "[\n"
    for subList in nestedList:
        nestedListStr += str(subList) + ", \n"
    nestedListStr += "]"
    return nestedListStr

def faces2init(faces):
    return [f[0] for f in faces]


faces = []
nEdges = max_value(b)
for e in range(1, nEdges + 1):
    for d in mono:
        face = []
        if any((e, perm2str(d)) in face for face in faces):
            continue
        face.append((e, perm2str(d)))
        eNew = permute(d, e)
        dNew = mono[mono.index(d) - 1]
        fNew = (eNew, perm2str(dNew))
        it = 0;
        while (eNew, dNew) != (e, d):
            it += 1
            face.append(fNew)
            eNew = permute(dNew, eNew)
            dNew = mono[mono.index(dNew) - 1]
            fNew = (eNew, perm2str(dNew))
        faces.append(face)


# Euler Characteristic
nVertices = len(b) + len(w)
nFaces = len(faces)
chi = nVertices - nEdges + nFaces


# Print results
# print(faces)
print(f"Faces: {readableNestedList(faces)}")
print(f"Initial edges: {faces2init(faces)}")
print(f"No. faces: {nFaces}")
print(f"No. edges: {nEdges}")
print(f"No. vertices: {nVertices}")
print(f"Euler Characteristic: {chi}")