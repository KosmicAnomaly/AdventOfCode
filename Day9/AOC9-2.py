import json

Cypher = open ('Day9\XMAScypher.json','r').read().split('\n')
Cypher.pop()

for n in range(len(Cypher)):
    Cypher[n] = int(Cypher[n])

invalidValue = 258585477
listIndex = Cypher.index(invalidValue)

def canSum(list,start,end,value):
    sumList=list[start:end]
    if sum(sumList)==value:
        minimum= min(sumList)
        maximum= max(sumList)
        print(f"[{minimum},{maximum}]")
        print(minimum+maximum)

        return True
    else:
        return False

for s in range(listIndex):
    for e in range(listIndex):
        if canSum(Cypher,s,e,invalidValue):
            exit()
