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
    for providedData in passport:
        for data in requiredData:
            if data in providedData:
                validData += 1
    if validData >= len(requiredData):
        print('Passport Valid')
        validPassports += 1
    else:
        print('Passport Invalid')
    print('\n')

print(validPassports)
