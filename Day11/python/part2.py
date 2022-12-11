# Import our lord and savior re
import re

with open("input.txt", "r") as f:
    raw = [i.split("\n") for i in f.read().split("\n\n")]


monkeys = dict()

for m in raw:
    number = int(re.search(r"(\d+)", m[0]).group(1))
    items = [int(i) for i in re.findall(r"(\d+)", m[1])]
    expression = re.search(r"Operation: new = (.*)", m[2]).group(1)

    divisor = int(re.search(r"Test: divisible by (\d+)", m[3]).group(1))

    trueMonkey = int(re.search(r"If true: throw to monkey (\d+)", m[4]).group(1))
    falseMonkey = int(re.search(r"If false: throw to monkey (\d+)", m[5]).group(1))

    monkeys[number] = {
        "items": items,
        "expression": expression,
        "divisor": divisor,
        "true": trueMonkey,
        "false": falseMonkey,
        "counter": 0,
    }

for round in range(10000):
    print(f"\nRound {round}")
    for m in sorted(monkeys.keys()):
        while len(monkeys[m]["items"]):
            monkeys[m]["counter"] += 1

            old = monkeys[m]["items"].pop(0)

            new = eval(monkeys[m]["expression"])
            new = new % 9699690
            if new % monkeys[m]["divisor"] == 0:
                monkeys[monkeys[m]["true"]]["items"].append(new)
            else:
                monkeys[monkeys[m]["false"]]["items"].append(new)

counters = [m["counter"] for m in monkeys.values()]
sorted = sorted(counters, reverse=True)
print(sorted[0] * sorted[1])
