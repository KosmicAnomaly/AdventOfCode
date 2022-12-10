with open("input.txt", "r") as f:
    instructions = [
        [2, int(i.split(" ")[1])] if i != "noop" else i for i in f.read().split("\n")
    ]

register = 1
pixel = 0

for i in range(1, 241):
    if pixel % 40 == 0:
        pixel = 0
        print()

    if abs(pixel - register) <= 1:
        print("#", end=" ")
    else:
        print(".", end=" ")

    if len(instructions):
        if instructions[0] == "noop":
            instructions.pop(0)
        else:
            instructions[0][0] -= 1
            if instructions[0][0] == 0:
                register += instructions[0][1]
                instructions.pop(0)

    pixel += 1

print()
