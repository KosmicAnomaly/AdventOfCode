# load puzzle input
with open("Day2\Commands.txt", "r") as f:
    data = f.readlines()

# set initial depth, horizontal position, and aim to 0
x = 0
y = 0
aim = 0

# run through each of the commands
for command in data:

    # split the command into its direction and distanced
    direction, distance = command.split(" ")

    # convert distance from string to integer
    distance = int(distance)

    # modify depth, horizontal position, or aim accordingly
    if direction == "forward":
        x += distance
        y += aim * distance
    elif direction == "up":
        aim -= distance
    else:
        aim += distance

# output the product of depth and horizontal position
product = x * y
print(product)
