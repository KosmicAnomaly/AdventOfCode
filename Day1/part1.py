with open("input.txt", "r") as f:
    elves = [i.split("\n") for i in f.read().split("\n\n")]

maxCalories = 0

for elf in elves:
    if sum([int(c) for c in elf]) > maxCalories:
        maxCalories = sum([int(c) for c in elf])

print(maxCalories)
