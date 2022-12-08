with open("input.txt", "r") as f:
    trees = [[int(j) for j in [*i] if j.isdigit()] for i in f.readlines()]

maxI = len(trees)
maxJ = len(trees[0])

bestScore = 0
for i in range(1, maxI - 1):
    for j in range(1, maxJ - 1):
        thisTree = trees[i][j]

        score = 1

        # Horizontal
        sum = 0
        for k in range(j + 1, maxJ):
            sum += 1
            if trees[i][k] >= thisTree:
                break
        score *= sum

        sum = 0
        for k in range(j - 1, -1, -1):
            sum += 1
            if trees[i][k] >= thisTree:
                break
        score *= sum

        # Vertical
        sum = 0
        for k in range(i + 1, maxI):
            sum += 1
            if trees[k][j] >= thisTree:
                break
        score *= sum

        sum = 0
        for k in range(i - 1, -1, -1):
            sum += 1
            if trees[k][j] >= thisTree:
                break
        score *= sum

        if score > bestScore:
            bestScore = score


print(bestScore)
