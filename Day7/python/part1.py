with open("input.txt", "r") as f:
    subs = [int(i) for i in f.read().split(",")]

cheapestCost = -1
for destination in range(min(subs), max(subs) + 1):
    thisCost = 0

    for sub in subs:
        thisCost += abs(sub - destination)

    if cheapestCost == -1:
        cheapestCost = thisCost
    else:
        cheapestCost = min(thisCost, cheapestCost)

print(cheapestCost)
