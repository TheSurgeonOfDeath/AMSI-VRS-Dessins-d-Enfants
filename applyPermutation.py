from Dessin import permute, randomise
import time

def permute(permutation, n):
    for row in permutation:
        for i in range(len(row)):
            if row[i] == n:
                return row[(i + 1) % len(row)]

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