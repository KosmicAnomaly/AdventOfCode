with open("input.txt", "r") as f:
    games = [i.removesuffix("\n") for i in f.readlines()]

score = 0

for game in games:
    match game.split(" ")[0]:
        case "A":
            match game.split(" ")[1]:
                case "X":
                    score += 3 + 0
                case "Y":
                    score += 1 + 3
                case "Z":
                    score += 2 + 6
        case "B":
            match game.split(" ")[1]:
                case "X":
                    score += 1 + 0
                case "Y":
                    score += 2 + 3
                case "Z":
                    score += 3 + 6
        case "C":
            match game.split(" ")[1]:
                case "X":
                    score += 2 + 0
                case "Y":
                    score += 3 + 3
                case "Z":
                    score += 1 + 6
print(score)
