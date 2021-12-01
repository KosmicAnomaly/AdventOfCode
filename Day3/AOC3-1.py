import json

#30 character wide, 323 down
with open ('Day3/Forest.json','r') as f:

    sledPos = [0,-3]
    forestList = []
    treeCount = 0

    for line in f:
        forestList.append(line)
    y = 0
    while y < (len(forestList)):
        sledPos = [y,sledPos[1]+3]
        if sledPos[1] > 30:
            sledPos[1] -= 31
        character = forestList[sledPos[0]][sledPos[1]]
        if character == '#':
            treeCount += 1
        print([sledPos[0]+1,sledPos[1]+1])
        print(character)
        y +=1
    print(treeCount)
