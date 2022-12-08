with open("input.txt", "r") as f:
    trees = [[int(j) for j in [*i] if j.isdigit()] for i in f.readlines()]

maxI = len(trees)
maxJ = len(trees[0])

visibleTrees = 2 * maxI + 2 * maxJ - 4

for i in range(1, maxI - 1):
    for j in range(1, maxJ - 1):
        thisTree = trees[i][j]

        leftShorter = [
            tree for tree in [trees[k][j] for k in range(0, i)] if tree < thisTree
        ]

        rightShorter = [
            tree
            for tree in [trees[k][j] for k in range(i + 1, maxI)]
            if tree < thisTree
        ]

        aboveShorter = [
            tree for tree in [trees[i][k] for k in range(0, j)] if tree < thisTree
        ]

        belowShorter = [
            tree
            for tree in [trees[i][k] for k in range(j + 1, maxJ)]
            if tree < thisTree
        ]

        if (
            len(leftShorter) == i
            or len(rightShorter) == maxI - 1 - i
            or len(aboveShorter) == j
            or len(belowShorter) == maxJ - 1 - j
        ):
            visibleTrees += 1


print(visibleTrees)
