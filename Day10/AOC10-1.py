with open("Day10\Adapters.txt", "r") as fp:
    Adapters = [int(line.rstrip()) for line in fp.readlines()]

Adapters.sort()
Adapters.insert(0,0)
Adapters.append(3+Adapters[len(Adapters)-1])

differencesList = [0,0,0]

print(Adapters)

for a in range(len(Adapters)-1):
    difference = Adapters[a+1]-Adapters[a]
    differencesList[difference-1] += 1

print(differencesList)
print(differencesList[0]*differencesList[2])
