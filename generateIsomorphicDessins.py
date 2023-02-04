from Dessin import Dessin, permute, randomise
from itertools import permutations
from unique_permutations import unique_permutations
import time

# fat square
fb = [(2,3,1,4), (6,7,5,8)]
fw = [(1,7,2,8), (4,5,3,6)]
F = Dessin(fb, fw)

alphas = list(permutations(F.Edges))


def find_in_list_of_list(mylist, elem):
    for sublist in mylist:
        if elem in sublist:
            return (mylist.index(sublist), sublist.index(elem))
    raise ValueError("'{char}' is not in list".format(char = elem))

def permute2(permutation, n):
    pos = find_in_list_of_list(permutation, n)
    return permutation[pos[0]][(pos[1] + 1) % len(permutation[pos[0]])]

def applyPermutation(perm, arr):
    return [permute(perm, n) for n in arr]

def applyPermutation2(perm, arr):
    return [permute(perm, n) for n in arr]


n = 100000
arr = list(range(1,n+1))
testperm = [tuple(randomise(arr))]
# print(testperm)

tic1 = time.perf_counter_ns()
print(applyPermutation(testperm, arr))
toc1 = time.perf_counter_ns()
print(f"permute time:  {toc1 - tic1} nanoseconds")

tic2 = time.perf_counter_ns()
print(applyPermutation2(testperm, arr))
toc2 = time.perf_counter_ns()
print(f"permute2 time: {toc2 - tic2} nanoseconds")
print(f"permute/permute2 ratio time: {(toc1 - tic1) / (toc2 - tic2)}")
# isomorphic2F = []
# for alpha in alphas:
#     for 