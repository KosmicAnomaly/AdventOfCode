with open("input.txt", "r") as f:
    input = f.readlines()

terrain = [[*i.removesuffix("\n")] for i in input]
terrain = [[row[i] for row in terrain] for i in range(len(terrain[0]))]

for i in range(len(terrain)):
    for j in range(len(terrain[0])):
        if terrain[i][j] == "S":
            start = (i, j)
            break

for i in range(len(terrain)):
    for j in range(len(terrain[0])):
        if terrain[i][j] == "E":
            end = (i, j)
            break


def height(pos: tuple) -> int:
    if terrain[pos[0]][pos[1]] == "S":
        return ord("a") - 96
    if terrain[pos[0]][pos[1]] == "E":
        return ord("z") - 96
    return ord(terrain[pos[0]][pos[1]]) - 96


def can_reach(pos: tuple, dest: tuple) -> bool:
    if height(pos) + 1 >= height(dest):
        return True
    return False


graph = dict()

for i in range(len(terrain)):
    for j in range(len(terrain[0])):
        graph[(i, j)] = {"cost": -1, "neighbors": []}

        if i > 0 and can_reach((i, j), (i - 1, j)):
            graph[(i, j)]["neighbors"].append((i - 1, j))

        if i + 1 < len(terrain) and can_reach((i, j), (i + 1, j)):
            graph[(i, j)]["neighbors"].append((i + 1, j))

        if j > 0 and can_reach((i, j), (i, j - 1)):
            graph[(i, j)]["neighbors"].append((i, j - 1))

        if j + 1 < len(terrain[0]) and can_reach((i, j), (i, j + 1)):
            graph[(i, j)]["neighbors"].append((i, j + 1))

visited = set()

queue = [start]

while len(queue):
    thisNode = queue.pop(0)

    visited.add(thisNode)

    for neighbor in graph[thisNode]["neighbors"]:
        if neighbor in visited:
            continue

        thisCost = graph[thisNode]["cost"] + 1
        if graph[neighbor]["cost"] == -1 or graph[neighbor]["cost"] > thisCost:
            graph[neighbor]["cost"] = thisCost
            queue.append(neighbor)

print(graph[end]["cost"] + 1)
