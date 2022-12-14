with open("input.txt", "r") as f:
    input = f.readlines()

paths = [
    [[int(c) for c in coord.split(",")] for coord in path.split(" -> ")]
    for path in input
]

maxY = max([max([i[1] for i in j]) for j in paths]) + 3
minX = 500 - maxY
maxX = 500 + maxY

cave = [["." for _ in range(maxX - minX)] for _ in range(maxY)]

for path in paths:
    for i in range(len(path) - 1):
        start = path[i]
        end = path[i + 1]

        if start[0] == end[0]:
            if end[1] >= start[1]:
                for y in range(start[1], end[1]):
                    cave[y][start[0] - minX - 1] = "#"
            else:
                for y in range(end[1], start[1] + 1):
                    cave[y][start[0] - minX - 1] = "#"

        else:
            if end[0] >= start[0]:
                for x in range(start[0], end[0] + 1):
                    cave[start[1]][x - minX - 1] = "#"
            else:
                for x in range(end[0], start[0] + 1):
                    cave[start[1]][x - minX - 1] = "#"

for x in range(maxX - minX):
    cave[maxY - 1][x] = "#"

source = [0, 500 - minX - 1]
cave[source[0]][source[1]] = "+"

sand = 0
hitSource = False
while not hitSource:
    pos = source.copy()
    while True:
        if cave[pos[0] + 1][pos[1]] == ".":
            pos[0] += 1
        elif cave[pos[0] + 1][pos[1] - 1] == ".":
            pos[0] += 1
            pos[1] -= 1
        elif cave[pos[0] + 1][pos[1] + 1] == ".":
            pos[0] += 1
            pos[1] += 1
        elif pos == source:
            hitSource = True
            break
        else:
            break

    sand += 1
    cave[pos[0]][pos[1]] = "o"


print(sand)
