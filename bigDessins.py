from Dessin import Dessin, generate_dessins
import json, jsonpickle

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

n = 6
dessins = generate_dessins(n)
for des in dessins: 
    des.calcEulerChi()

# encoded_dessins = [jsonpickle.encode(des) for des in dessins]
encoded_dessins = jsonpickle.encode(dessins, indent = 4)
with open(f"data/dessins_order({n}).json", 'w') as f:
    # json.dump(encoded_dessins, f, indent=4)
    f.write(encoded_dessins)


# print(len(dessins))
