# Import the great and powerful re
import re

with open("input.txt", "r") as f:
    input = f.read().splitlines()

groups = [
    re.fullmatch(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
        line,
    )
    for line in input
]

pairs = [
    [[int(m.group(1)), int(m.group(2))], [int(m.group(3)), int(m.group(4))]]
    for m in groups
]


def distance(a: list, b: list) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


sensorRanges = [[p[0], distance(p[0], p[1])] for p in pairs]


def get_edge_points(sensor: list, sensorRange: int) -> list:
    coords = []

    topRight = list(
        zip(
            range(sensor[0], sensor[0] + sensorRange + 1),
            range(sensor[1] + sensorRange, sensor[1] - 1, -1),
        )
    )
    coords.extend(topRight)

    bottomRight = [(i[0], -i[1]) for i in topRight]
    coords.extend(bottomRight)

    bottomLeft = [(-i[0], i[1]) for i in bottomRight]
    coords.extend(bottomLeft)

    topLeft = [(i[0], -i[1]) for i in bottomLeft]
    coords.extend(topLeft)

    return coords


upperRange = 4000000

potentialCoords = []
for sensor in sensorRanges:
    edge = get_edge_points(sensor[0], sensor[1] + 1)

    edge = [
        coord
        for coord in edge
        if coord[0] >= 0
        and coord[0] <= upperRange
        and coord[1] >= 0
        and coord[1] <= upperRange
    ]

    potentialCoords.extend(edge)

for coord in potentialCoords:
    for sensor in sensorRanges:
        if distance(coord, sensor[0]) <= sensor[1]:
            break
    else:
        break

print(4000000 * coord[0] + coord[1])
