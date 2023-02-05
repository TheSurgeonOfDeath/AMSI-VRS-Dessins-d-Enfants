from Dessin import Dessin, areIsomorphic
from itertools import combinations
import jsonpickle
import time

n = 6

# read dessin from file
tic = time.perf_counter()
with open(f"data/dessins_order({n})_all.json", 'r') as f:
    dessins = jsonpickle.decode(f.read())
toc = time.perf_counter()
print(f"Loading time: {toc - tic:0.4f} seconds")

tic = time.perf_counter()
uniqueDessins = []
for i, des in enumerate(dessins):
    print([len(uniqueDessins), i, len(dessins)])
    if not any(areIsomorphic(des, udes) for udes in uniqueDessins):
        uniqueDessins.append(des)
toc = time.perf_counter()
print(f"Unique time: {toc - tic:0.4f} seconds")
print(len(uniqueDessins))