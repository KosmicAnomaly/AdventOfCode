import ast

with open("input.txt", "r") as f:
    input = f.read()

input = input.splitlines()
packets = [ast.literal_eval(i) for i in input if len(i)]
packets.extend([[[2]], [[6]]])


def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if left > right:
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
        return 1

    if len(left) > len(right):
        return 0

    return -1


def sort(input):
    for i in range(len(input)):
        sorted = True

        for j in range(len(input) - i - 1):
            if not compare(input[j], input[j + 1]):
                input[j], input[j + 1] = input[j + 1], input[j]
                sorted = False

        if sorted:
            break

    return input


sortedPackets = sort(packets)
print((sortedPackets.index([[2]]) + 1) * (sortedPackets.index([[6]]) + 1))
