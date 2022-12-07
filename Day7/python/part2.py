with open("input.txt", "r") as f:
    input = f.readlines()

file_structure = {"/": {}}

path = []

for line in input:
    if line.startswith("$ cd"):
        if line.split()[2] == "..":
            path.pop()
        else:
            path.append(line.split()[2])

    else:
        whereami = file_structure
        for d in path:
            whereami = whereami[d]

        if line.startswith("dir"):
            whereami[line.split()[1]] = {}
        elif line.split()[0].isdigit():
            whereami[line.split()[1]] = int(line.split()[0])

bestdir = 70000000
toFree = 0


def get_dir_size(dir: dict) -> int:
    global bestdir
    global toFree
    thisSize = 0
    for i in dir.values():
        if isinstance(i, dict):
            thisSize += get_dir_size(i)
        else:
            thisSize += i

    if thisSize >= toFree and thisSize < bestdir:
        bestdir = thisSize
    return thisSize


toFree = 30000000 - (70000000 - get_dir_size(file_structure))
bestdir = 70000000
get_dir_size(file_structure)
print(bestdir)
