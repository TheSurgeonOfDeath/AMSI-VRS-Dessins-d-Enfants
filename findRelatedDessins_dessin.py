# Find all dessins that a given dessin can be morphed to

from Dessin import Dessin, areMorphic, findMorphisms
from functools import reduce
import jsonpickle
from readableNestedList import readableNestedList

# def factors(n):   
#     # source: https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python 
#     return set(reduce(list.__add__, 
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# b = [(1,2,3,4,5,6)]
# w = [(6,5,4,3,2,1)]
# F = Dessin(b, w)


# facts = factors(F.nEdges)
# # print(facts)

n = 6
with open(f"data/dessins_order({n}).json", 'r') as f:
        dessinsSrc = jsonpickle.decode(f.read())


dessinsTar = []
for m in [2,3]:
    with open(f"data/dessins_order({m}).json", 'r') as f:
        dessinsTar.append(jsonpickle.decode(f.read()))


morphicsPerSrc = [
    [tar for desTari in dessinsTar for tar in desTari if areMorphic(src, tar)]
     for src in dessinsSrc
]

srcNtars = [
    (dessinsSrc[i], morphs) for i, morphs in enumerate(morphicsPerSrc) if morphs
]
# print(srcNtars)
for snt in srcNtars:
    # print(readableNestedList(snt[0].Faces))
    snt[0].printEulerCharacteristic()
    for t in snt[1]:
        t.printEulerCharacteristic()
        # print(readableNestedList(t.Faces))
        # print(readableNestedList(findMorphisms(snt[0], t)))
    print('\n')

# print([(i, dessinsSrc[i].EulerChi, len(morphs)) for i, morphs in enumerate(morphicsPerSrc) if morphs])

# for i, morphs in enumerate(morphicsPerSrc):
#     if morphs:
#         print(i, dessinsSrc[i].EulerChi, len(morphs))

# dessinsSrc[543].printEulerCharacteristic()
# [morphic.printEulerCharacteristic() for morphic in morphicsPerSrc[543]]

# print(dessinsSrc[543].mono)
# print([morphic.mono for morphic in morphicsPerSrc[543]])

