import json
import re


def isBagNested(bagColor):
    if not bagColor in highestBags:
        highestBags.append(bagColor)
    hasHigherBag = True
    for bag in range(len(BagRules)):
        if bagColor in BagRules[bag] and not bagColor == BagRules[bag][0]:
            higherBagColor = BagRules[bag][0]
            print(f"{bagColor}, {higherBagColor}, {BagRules[bag]}")
            isBagNested(higherBagColor)


BagRules = open ('Day7\BagRules.json','r').read().split('\n')
BagRules.pop()

yourBag = 'shiny gold'
highestBags = []

for bag in range(len(BagRules)):
    bagList = re.split(' bags contain | bags, | bag, | bag.| bags.|no other bags.|1 |2 |3 |4 |5 |6 |7 |8 |9 ',BagRules[bag])
    bagList = [b for b in bagList if b and not b =='.']
    BagRules[bag] = bagList

BagRules = [br for br in BagRules if len(br) > 1]

isBagNested(yourBag)

print(highestBags)
print(len(highestBags)-1)
