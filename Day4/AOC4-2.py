import json
import re

requiredData = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

passportList = open ('Day4/Passports.json','r').read().split('\n\n')
print(passportList)

validPassports = 0

for passport in passportList:

    passport = passport.replace('\n', ' ').split(' ')
    print(passport)

    validData = 0

    for data in requiredData:
        for providedData in passport:
            if data in providedData:
                splittedPassportData = re.split(':',providedData)
                print(splittedPassportData)
                value = splittedPassportData[1]

                if data == "byr":
                    year = int(value)
                    if year <= 2002 and year >= 1920:
                        validData += 1
                        print('Birth Year Valid')

                elif data == "iyr":
                    year = int(value)
                    if year <= 2020 and year >= 2010:
                        validData += 1
                        print('Issue Year Valid')

                elif data == "eyr":
                    year = int(value)
                    if year <= 2030 and year >= 2020:
                        validData += 1
                        print('Expiration Year Valid')

                elif data == "hgt":
                    height = value
                    if 'cm' in height:
                        cm = int(height.strip('cm'))
                        if cm <= 193 and cm >= 150:
                            validData += 1
                            print('Height Valid')
                    elif 'in' in height:
                        inches = int(height.strip('in'))
                        if inches <= 76 and inches >= 59:
                            validData += 1
                            print('Height Valid')

                elif data == "hcl":
                    color = value
                    if color[0] == '#' and len(color) == 7:
                        string = color.strip('#')
                        goodCharacters = '0123456789abcdef'
                        validCharacters = 0
                        for character in string:
                            if character in goodCharacters:
                                validCharacters += 1
                        if validCharacters == 6:
                            validData += 1
                            print('Hair Color Valid')

                elif data == "ecl":
                    color = value
                    goodColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    if color in goodColors:
                        validData += 1
                        print('Eye Color Valid')

                elif data == "pid":
                    ID = value
                    goodCharacters = '0123456789'
                    validCharacters = 0
                    for character in ID:
                        if character in goodCharacters:
                            validCharacters += 1
                    if validCharacters == 9:
                        validData += 1
                        print('Passport ID Valid')

    if validData >= len(requiredData):
        print('Passport Valid')
        validPassports += 1
    else:
        print('Passport Invalid')

    print('\n')

print(validPassports)
