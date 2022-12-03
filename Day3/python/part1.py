with open("input.txt", "r") as f:
    rucksacks = f.readlines()

sum = 0

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for rucksack in rucksacks:
    left = rucksack[: int(len(rucksack) / 2)]
    right = rucksack[int(len(rucksack) / 2) :]

    char = [c for c in left if c in right][0]

    sum += 1 + priorities.rfind(char)

print(sum)
