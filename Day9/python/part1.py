import math

with open("input.txt", "r") as f:
    movements = [(i.split(" ")[0], int(i.split(" ")[1])) for i in f.readlines()]

head = [0, 0]
tail = [0, 0]

visited = {str(tail)}

for m in movements:
    print(m)

    for s in range(m[1]):
        match m[0]:
            case "U":
                head[1] += 1

            case "D":
                head[1] -= 1

            case "L":
                head[0] -= 1

            case "R":
                head[0] += 1

        if math.dist(head, tail) >= 2:
            tail[0] += min(1, max(-1, head[0] - tail[0]))
            tail[1] += min(1, max(-1, head[1] - tail[1]))
            visited.add(str(tail))

        print(head, tail)

print(len(visited))
