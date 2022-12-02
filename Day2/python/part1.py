with open("input.txt", "r") as f:
    games = [i.removesuffix("\n") for i in f.readlines()]

score = 0

for game in games:
    match game.split(" ")[1]:
        case "X":
            score += 1
            match game.split(" ")[0]:
                case "A":
                    score += 3
                case "B":
                    score += 0
                case "C":
                    score += 6
        case "Y":
            score += 2
            match game.split(" ")[0]:
                case "A":
                    score += 6
                case "B":
                    score += 3
                case "C":
                    score += 0
        case "Z":
            score += 3
            match game.split(" ")[0]:
                case "A":
                    score += 0
                case "B":
                    score += 6
                case "C":
                    score += 3
print(score)
