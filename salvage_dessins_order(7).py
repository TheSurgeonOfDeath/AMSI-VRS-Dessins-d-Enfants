import re


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

with open("data/dessins_order(7).json", 'w') as f:
    for line in file_lines:
        f.write(line + "\n")

# pyids_indices = [m.start() for m in re.finditer("\"py/id\":", file)]

# ids = []
# for i in pyids_indices[:5]:
#     ids.append(file[i+9])

# print(ids)

"57121 = 5 digits"

