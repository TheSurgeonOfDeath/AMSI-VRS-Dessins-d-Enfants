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

n = 1
dessins = generate_dessins(n)
# print(len(dessins))
for des in dessins: 
    des.calcEulerChi()

# encoded_dessins = [des.__dict__ for des in dessins]
encoded_dessins = jsonpickle.encode(dessins, indent = 4)
with open(f"data/dessins_order({n}).json", 'w') as f:
    # json.dump(encoded_dessins, f, indent=4)
    f.write(encoded_dessins)

# with open(f"data/dessins_order({n+3}).json", 'r') as f:
#     loadedDessins = jsonpickle.decode(f.read())

# for des in loadedDessins:
#     des.printEulerCharacteristic()
#     print(des.monoStr)
