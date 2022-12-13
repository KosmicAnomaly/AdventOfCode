import ast

with open("input.txt", "r") as f:
    input = f.read()

input = [i.split("\n") for i in input.split("\n\n")]
pairs = [[ast.literal_eval(i) for i in p] for p in input]


def compare(left, right) -> int:
    print(f"- Compare {left} vs {right}")

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print("- Left side is smaller, so inputs are in the right order")
            return 1
        if left > right:
            print("- Right side is smaller, so inputs are not in the right order")
            return 0
        return -1

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for i in range(min(len(left), len(right))):
        result = compare(left[i], right[i])
        match result:
            case 0:
                return False
            case 1:
                return True
            case -1:
                continue

    if len(left) < len(right):
        print("- Left side ran out of items, so inputs are in the right order")
        return 1

    if len(left) > len(right):
        print("- Right side ran out of items, so inputs are not in the right order")
        return 0

    return -1


correctPairs = []

for i in range(len(pairs)):
    print(f"== Pair {i + 1} ==")
    pair = pairs[i]

    if compare(pair[0], pair[1]) == 1:
        correctPairs.append(i + 1)

print(sum(correctPairs))
