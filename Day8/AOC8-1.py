import json

def acc(increment):
    global accumulator
    accumulator += int(increment)

def jmp(lineChange):
    global line
    line += int(lineChange)-1

BootCode = open ('Day8\BootCode.json','r').read().split('\n')
BootCode.pop()

accumulator = 0
visitedLines = []
line = 0

while 1 == 1:
    if line in visitedLines:
        print(f"I've seen this line ({line}) before!!! (accumulator = {accumulator}):")
        exit()

    runningLine = BootCode[line].split(' ')
    print(f"{line}/{len(BootCode)}: {runningLine}")

    if 'acc' in runningLine[0]:
        acc(runningLine[1])

    elif 'jmp' in runningLine[0]:
        jmp(runningLine[1])

    visitedLines.append(line)
    line += 1
