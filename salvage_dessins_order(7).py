import re
import jsonpickle
from Dessin import Dessin

correctSemiIdType = "\"py/function\": \"numpy.core.multiarray.scalar\""
with open("data/dessins_order(7)_old.json", 'r') as f:
    file = f.read()

file = file.replace("\"py/object\": \"builtins.builtin_function_or_method\"", correctSemiIdType)
file = file.replace("\"py/id\": 9\n", correctSemiIdType + "\n")
file_lines = file.split("\n")
for i, line in enumerate(file_lines):
    # print(line)
    pyid_index = line.find("\"py/id\":")
    pyid = line[pyid_index + 9:]
    if pyid_index != -1 and int(pyid) >= 9:
        # print(line)
        file_lines[i] = line.replace(pyid, str(int(pyid) - 1))
        # print(line)

with open("data/dessins_order(7)_old2.json", 'w') as f:
    for line in file_lines:
        f.write(line + "\n")


with open("data/dessins_order(7)_old2.json", 'r') as f:
    dessins = jsonpickle.decode(f.read())

for i, des in enumerate(dessins):
    dessins[i] = Dessin(des.b, des.w)
    dessins[i].calcEulerChi()

with open("data/dessins_order(7).json", 'w') as f:
    f.write(jsonpickle.encode(dessins, indent = 4))
