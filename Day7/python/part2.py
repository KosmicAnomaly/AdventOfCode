with open("input.txt", "r") as f:
    subs = [int(i) for i in f.read().split(",")]

cheapestCost = -1
for destination in range(min(subs), max(subs) + 1):
    thisCost = 0

    for sub in subs:
        stepCost = 1
        for i in range(abs(sub - destination)):
            thisCost += stepCost
            stepCost += 1

    if cheapestCost == -1:
        cheapestCost = thisCost
    else:
        cheapestCost = min(thisCost, cheapestCost)

print(cheapestCost)
