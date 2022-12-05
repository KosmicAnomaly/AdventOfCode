with open("input.txt", "r") as f:
    lanternfish = [int(i) for i in f.read().split(",")]


def run_day():
    for i in range(len(lanternfish)):
        lanternfish[i] -= 1

        if lanternfish[i] < 0:
            lanternfish[i] = 6
            lanternfish.append(8)


for i in range(80):
    run_day()

print(len(lanternfish))
