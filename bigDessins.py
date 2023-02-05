from Dessin import generate_dessins, generate_dessins_single
import time
import jsonpickle

#### testing writing and reading json files of data
# print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=2))
# score = {'4': 5, '6': 7}
# with open("data/testfile.json", 'w') as f:
#     # indent=2 is not needed but makes the file human-readable
#     # if the data is nested
#     json.dump(score, f, indent=2)

# with open("data/testfile.json", 'r') as f:
#     score2 = json.load(f)
# print(score2)

# order
n = 3

# Generate dessins
tic = time.perf_counter()
dessins = generate_dessins_single(n)
print(len(dessins))
for des in dessins:
    des.calcEulerChi()
toc = time.perf_counter()
print(f"Generating time: {toc - tic:0.4f} seconds")


# write dessin to file
tic = time.perf_counter()
encoded_dessins = jsonpickle.encode(dessins, indent = 4)
with open(f"data/dessins_order({n}).json", 'w') as f:
    f.write(encoded_dessins)
toc = time.perf_counter()
print(f"Writing time: {toc - tic:0.4f} seconds")


# # read dessin from file
# tic = time.perf_counter()
# with open(f"data/dessins_order({n}).json", 'r') as f:
#     loadedDessins = jsonpickle.decode(f.read())
# toc = time.perf_counter()
# print(f"Loading time: {toc - tic:0.4f} seconds")
# print(len(loadedDessins))
# print([des.EulerChi for des in loadedDessins])
