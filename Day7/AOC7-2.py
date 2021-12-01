import json
import re

nestedBagCount = 0

def NestedBags(bagColor):
    global nestedBagCount
    bagList = []
    for bag in range(len(BagRules)):
        if bagColor == BagRules[bag][0]:
            bagList = BagRules[bag]
            print(bagList)

    if len(bagList) > 1:
        for contents in range(1,len(bagList)):
            count = int(bagList[contents][0])
            nestedBagCount += count
            bag = bagList[contents][2:]
            print(f'{count}x {bag}')
            for bags in range(count):
                NestedBags(bag)


BagRules = open ('Day7\BagRules.json','r').read().split('\n')
BagRules.pop()

yourBag = 'shiny gold'

for bag in range(len(BagRules)):
    bagContents = BagRules[bag].replace('no other bags.','')
    bagList = re.split(' bags contain | bags, | bag, | bag.| bags.',bagContents)
    bagList = [b for b in bagList if b and not b =='.']
    BagRules[bag] = bagList
BagRules = [br for br in BagRules if len(br) > 1]
print(BagRules)

NestedBags(yourBag)

print(nestedBagCount)
