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

minX = min([min([i[0] for i in p]) for p in pairs])
maxX = max([max([i[0] for i in p]) for p in pairs])

y = 2000000

noBeacons = []
for x in range(minX, maxX + 1):
    for sensor in sensorRanges:
        if distance([x, y], sensor[0]) <= sensor[1]:
            noBeacons.append([x, y])
            break

beacons = [p[1] for p in pairs]
noBeacons = [i for i in noBeacons if not i in beacons]

print(len(noBeacons))
