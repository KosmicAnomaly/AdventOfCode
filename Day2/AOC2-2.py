import json
import re

with open ('Day2/PasswordPolicies.json','r') as p:
    validPasswords = 0
    for line in p:
        print(line)
        splittedLine = re.split('-| |: |\n',line)
        print(splittedLine)

        validPos1 = int(splittedLine[0])-1
        validPos2 = int(splittedLine[1])-1
        letter = splittedLine[2]
        string = splittedLine[3]
        pos1 = string[validPos1]
        pos2 = string[validPos2]
        correctPositions = 0
        if pos1 == letter:
            correctPositions += 1
        if pos2 == letter:
            correctPositions += 1
        if correctPositions == 1:
            validPasswords += 1
    print(validPasswords)
