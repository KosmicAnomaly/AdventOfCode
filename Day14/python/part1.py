with open("input.txt", "r") as f:
    input = f.readlines()

paths = [
    [[int(c) for c in coord.split(",")] for coord in path.split(" -> ")]
    for path in input
]

maxY = max([max([i[1] for i in j]) for j in paths]) + 1
minX = min([min([i[0] for i in j]) for j in paths]) - 1
maxX = max([max([i[0] for i in j]) for j in paths])

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

source = [0, 500 - minX - 1]
cave[source[0]][source[1]] = "+"

sand = 0
abyss = False
while not abyss:
    pos = source.copy()
    while True:
        if pos[0] == maxY - 1:
            abyss = True
            break

        if cave[pos[0] + 1][pos[1]] == ".":
            pos[0] += 1
        elif cave[pos[0] + 1][pos[1] - 1] == ".":
            pos[0] += 1
            pos[1] -= 1
        elif cave[pos[0] + 1][pos[1] + 1] == ".":
            pos[0] += 1
            pos[1] += 1
        else:
            cave[pos[0]][pos[1]] = "o"
            sand += 1
            break


def draw(cave):
    for i in range(len(cave)):
        for j in range(len(cave[0])):
            print(cave[i][j], end="")
        print()
    print()


draw(cave)
print(sand)
