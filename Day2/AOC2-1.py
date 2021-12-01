import json
import re

with open('Day2/PasswordPolicies.json', 'r') as p:
    validPasswords = 0
    for line in p:
        print(line)
        splittedLine = re.split('-| |: |\n', line)
        print(splittedLine)

        min = int(splittedLine[0])
        max = int(splittedLine[1])
        letter = splittedLine[2]
        string = splittedLine[3]

        occurances = string.count(letter)
        if occurances <= max and occurances >= min:
            validPasswords += 1
    print(validPasswords)
