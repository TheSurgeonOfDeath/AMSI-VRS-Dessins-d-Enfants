from unique_permutations import unique_permutations
import time
from itertools import permutations

base = list(range(1,3)) * 4

tic = time.perf_counter_ns()
p1 = list(unique_permutations(base))
toc = time.perf_counter_ns()
print(f"p1: {toc - tic}")

tic = time.perf_counter_ns()
p2 = [tuple(perm) for perm in unique_permutations(base)]
toc = time.perf_counter_ns()
print(f"p2: {toc - tic}")

tic = time.perf_counter_ns()
p3 = list(set(permutations(base)))
toc = time.perf_counter_ns()
print(f"p3: {toc - tic}")


# print(p1)
# print(p2)
# print(p3)