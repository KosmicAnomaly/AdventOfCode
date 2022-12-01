with open("input.txt", "r") as f:
    elves = [i.split("\n") for i in f.read().split("\n\n")]

calorieSums = [sum([int(c) for c in elf]) for elf in elves]

calorieSums.sort(reverse=True)

print(sum(calorieSums[:3]))
