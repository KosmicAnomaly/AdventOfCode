import json


def bootUp(code):
    global changedLine
    global highestLine
    visitedLines = []
    accumulator = 0
    line = 0
    while line != 638:
        if line in visitedLines:
            print(line)
            break

        runningLine = code[line]
        print(f"{line}: {runningLine}")
        visitedLines.append(line)
        if 'acc' in runningLine[0]:
            accumulator += runningLine[1]

        elif 'jmp' in runningLine[0]:
            line += runningLine[1]

        if not 'jmp' in runningLine[0]:
            line += 1
        if line > highestLine:
            highestLine = line

    if line == 638:
        print(accumulator)
        exit()


BootCode = open ('Day8\BootCode.json','r').read().split('\n')
BootCode.pop()

highestLine = 0

for line in range(638):
    BootCode[line] = BootCode[line].split(' ')
    BootCode[line][1] = int(BootCode[line][1])


for changedLine in range(638):
    editedBootCode = BootCode
    print(BootCode)
    if editedBootCode[changedLine][0] == 'jmp':
        editedBootCode[changedLine][0] = 'nop'
        bootUp(editedBootCode)
        editedBootCode[changedLine][0] = 'jmp'
    elif editedBootCode[changedLine][0] == 'nop':
        editedBootCode[changedLine][0] = 'jmp'
        bootUp(editedBootCode)
        editedBootCode[changedLine][0] = 'nop'

    print('=============')

print("Didn't find solution!")
print(highestLine)
