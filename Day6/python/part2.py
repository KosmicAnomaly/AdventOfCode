with open("input.txt", "r") as f:
    stream = [*f.read()]

for i in range(len(stream) - 13):
    print(stream[i : i + 14])
    if sorted(list(set(stream[i : i + 14]))) == sorted(stream[i : i + 14]):
        print(i + 14)
        break
