with open("input.txt", "r") as f:
    assignments = [
        [[int(k) for k in j.split("-")] for j in i.removesuffix("\n").split(",")]
        for i in f.readlines()
    ]

sum = 0

for assignment in assignments:
    startA = assignment[0][0]
    endA = assignment[0][1]
    startB = assignment[1][0]
    endB = assignment[1][1]

    a = [i for i in range(startA, endA + 1)]
    b = [i for i in range(startB, endB + 1)]

    if all(i in a for i in b) or all(i in b for i in a):
        sum += 1

print(sum)
