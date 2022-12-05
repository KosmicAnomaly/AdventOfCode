with open("input.txt", "r") as f:
    lanternfish = [int(i) for i in f.read().split(",")]


def empty_states():
    return dict([(s, 0) for s in range(0, 9)])


states = empty_states()

for fish in lanternfish:
    states[fish] += 1


def run_day(states):
    newStates = empty_states()

    newStates[8] = states[0]
    newStates[6] = states[0]

    for state in range(1, 9):
        newStates[state - 1] += states[state]
    print(newStates)
    return newStates


for i in range(256):
    states = run_day(states)

print(sum(states.values()))
