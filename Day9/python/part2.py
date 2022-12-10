import math

with open("input.txt", "r") as f:
    movements = [(i.split(" ")[0], int(i.split(" ")[1])) for i in f.readlines()]

knots = [[0, 0] for i in range(10)]

visited = {str(knots[9])}

for m in movements:
    print(m)

    for s in range(m[1]):
        match m[0]:
            case "U":
                knots[0][1] += 1

            case "D":
                knots[0][1] -= 1

            case "L":
                knots[0][0] -= 1

            case "R":
                knots[0][0] += 1

        for k in range(1, 10):
            if math.dist(knots[k - 1], knots[k]) >= 2:
                knots[k][0] += min(1, max(-1, knots[k - 1][0] - knots[k][0]))
                knots[k][1] += min(1, max(-1, knots[k - 1][1] - knots[k][1]))

        visited.add(str(knots[9]))


print(len(visited))
