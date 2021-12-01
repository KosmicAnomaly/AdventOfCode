import json

Cypher = open ('Day9\XMAScypher.json','r').read().split('\n')
Cypher.pop()

for n in range(len(Cypher)):
    Cypher[n] = int(Cypher[n])

preambleLength = 25

def canSum(sumList,value):
    for a in range(len(sumList)):
        for b in range(len(sumList)):
            if sumList[a]+sumList[b]==value:
                return True
    return False

for x in range(len(Cypher)-preambleLength):
    preamble = Cypher[x:x+preambleLength]
    nextValue = Cypher[x+preambleLength]
    print(preamble)
    if canSum(preamble,nextValue):
        print(f'Value Valid: {nextValue}')
    else:
        print(f'Value Invalid: {nextValue}')
        exit()
