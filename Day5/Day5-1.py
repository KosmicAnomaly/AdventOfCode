# import our lord and savior numpy
import numpy as np

# load puzzle input
with open("Day5\VentField.txt", "r") as f:
    data = f.readlines()

# clean up data
vents = []
for raw_vent in data:
    fix1 = [pair.split(",") for pair in raw_vent.rstrip("\n").split(" -> ")]

    clean_vent = []
    for pair in fix1:
        clean_vent.append([int(coord) for coord in pair])

    vents.append(clean_vent)

# calculate the bounds of the vent field
max_x = 0
max_y = 0
for vent in vents:
    max_x = max(max_x, max(vent[0][0], vent[1][0]))
    max_y = max(max_x, max(vent[0][1], vent[1][1]))
max_x += 1
max_y += 1

# create an empty numpy array of size max_x by max_y
vent_field = np.zeros((max_x, max_y))

# fill in the vent_field array with vents
for vent in vents:

    # horizontal vents
    if vent[0][0] == vent[1][0]:
        # fix values for range
        start_y = min(vent[0][1], vent[1][1])
        end_y = max(vent[0][1], vent[1][1])
        for y in range(start_y, end_y + 1):
            vent_field[vent[0][0]][y] += 1

    # vertical vents
    elif vent[0][1] == vent[1][1]:
        # fix values for range
        start_x = min(vent[0][0], vent[1][0])
        end_x = max(vent[0][0], vent[1][0])
        for x in range(start_x, end_x + 1):
            vent_field[x][vent[0][1]] += 1


# count areas with a value greater than 1
danger_areas = 0
for x in range(max_x):
    for y in range(max_y):
        if vent_field[x][y] > 1:
            danger_areas += 1
print(danger_areas)
