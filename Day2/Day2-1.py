# load puzzle input
with open("Day2\Commands.txt", "r") as f:
    data = f.readlines()

# set initial depth and horizontal position to 0
x = 0
y = 0

# run through each of the commands
for command in data:

    # split the command into its direction and distanced
    direction, distance = command.split(" ")

    # convert distance from string to integer
    distance = int(distance)

    # modify depth or horizontal position accordingly
    if direction == "forward":
        x += distance
    elif direction == "up":
        y -= distance
    else:
        y += distance

# output the product of depth and horizontal position
product = x * y
print(product)
