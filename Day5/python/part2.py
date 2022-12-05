# Import our lord and savior re
import re

with open("input.txt", "r") as f:
    arrangements, instructions = f.read().split("\n\n")

levels = [
    [j[i : i + 4][1] for i in range(0, len(j), 4)]
    for j in arrangements.split("\n")
    if not j.startswith(" 1")
]

instructions = [
    re.match(r"move (\d+) from (\d) to (\d)", i).groups()
    for i in instructions.split("\n")
]

crates = []
for column in range(max([len(level) for level in levels])):
    thisColumn = []
    for level in levels:
        if column < len(level) and level[column] != " ":
            thisColumn.append(level[column])
    crates.append(thisColumn)

for instruction in instructions:
    toMove = crates[int(instruction[1]) - 1][: int(instruction[0])]
    crates[int(instruction[2]) - 1][:0] = toMove
    crates[int(instruction[1]) - 1] = crates[int(instruction[1]) - 1][
        int(instruction[0]) :
    ]

top = "".join([i[0] for i in crates])
print(top)
