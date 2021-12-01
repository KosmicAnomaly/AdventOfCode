import json

#31 character wide, 323 down
with open ('Day3/Forest.json','r') as f:

    slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]
    sledStartPos = [[-1,-1],[-1,-3],[-1,-5],[-1,-7],[-2,-1]]
    forestList = []
    treeCount = [0,0,0,0,0]

    for line in f:
        forestList.append(line)

    for slope in range(5):
        y = 0
        sledPos = sledStartPos[slope]
        print(sledPos)
        while y <= 322:
            sledPos = [sledPos[0]+slopes[slope][0],sledPos[1]+slopes[slope][1]]

            if sledPos[1] > 30:
                sledPos[1] -= 31
            character = forestList[sledPos[0]][sledPos[1]]
            if character == '#':
                treeCount[slope] += 1
            y += slopes[slope][0]
    result = 1
    for x in treeCount:
         result = result * x
    print(treeCount)
    print(result)
