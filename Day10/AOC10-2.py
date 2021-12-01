with open("Day10\AdaptersEx.txt", "r") as fp:
    Adapters = [int(line.rstrip()) for line in fp.readlines()]

Adapters.sort()
Adapters.insert(0,0)
Adapters.append(3+Adapters[len(Adapters)-1])
print(Adapters)

listLen = len(Adapters)

paths = []

for a in range(listLen-1):
    combos = []
    for nextAdapter in range(1,4):
        if a+nextAdapter <= listLen-1:
            difference = Adapters[a+nextAdapter]-Adapters[a]
            if difference <= 3:
                combos.append(Adapters[a+nextAdapter])
    combos.sort()
    paths.append({'Adapter':Adapters[a], 'Connections':combos})
    print(f'{Adapters[a]}: {combos}')

print(paths)

possibilities = 0

def connectOptions(adapter):
    global paths
    global possibilities

    def getDict(list,value):
        for d in range(len(list)):
            if list[d]['Adapter'] == value:
                return list[d]

    if adapter == paths[-1]:
        possibilities += 1
        return

    adapterDict = getDict(paths,adapter)
    print(adapterDict)
    connections=adapterDict['Connections']
    print(connections)
    for thisAdapter in connections:
        connectOptions(thisAdapter)

connectOptions(3)
