with open("input.txt", "r") as f:
    rucksacks = [r.removesuffix("\n") for r in f.readlines()]

groups = zip(*(iter(rucksacks),) * 3)

sum = 0

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for group in groups:
    char = list(set.intersection(*map(set, group)))[0]
    print(group, char)
    sum += 1 + priorities.rfind(char)

print(sum)
