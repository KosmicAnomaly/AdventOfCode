with open("input.txt", "r") as f:
    stream = [*f.read()]

for i in range(len(stream) - 3):
    print(stream[i : i + 4])
    if sorted(list(set(stream[i : i + 4]))) == sorted(stream[i : i + 4]):
        print(i + 4)
        break
