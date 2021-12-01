import json
import math

def getSeatID(row,column):
    seatID = row * 8 + column
    return seatID

boardingPasses = open ('Day5\BoardingPasses.json','r').read().split('\n')
boardingPasses.pop()

highestSeatID = 0

for boardingPass in boardingPasses:

    rowRange = [0,127]
    for letter in range(7):

        region = boardingPass[letter]
        if region == 'F':
            rowRange[1] -= (rowRange[1] - rowRange[0]) / 2
            rowRange[1] = math.floor(rowRange[1])
        else:
            rowRange[0] += (rowRange[1] - rowRange[0]) / 2
            rowRange[0] = math.ceil(rowRange[0])
    row = rowRange[0]

    columnRange = [0,7]
    for letter in range(7,10):
        region = boardingPass[letter]
        if region == 'L':
            columnRange[1] -= (columnRange[1] - columnRange[0]) / 2
            columnRange[1] = math.floor(columnRange[1])
        else:
            columnRange[0] += (columnRange[1] - columnRange[0]) / 2
            columnRange[0] = math.ceil(columnRange[0])
    column = columnRange[0]

    thatSeatID = getSeatID(row,column)

    if thatSeatID > highestSeatID:
        highestSeatID = thatSeatID

print(highestSeatID)
