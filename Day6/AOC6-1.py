import json

CustomsAnswers = open ('Day6\CustomsAnswers.json','r').read().split('\n\n')

letters = 'abcdefghijklmnopqrstuvwxyz'
yesCount = 0

for group in range(len(CustomsAnswers)):
    answers = CustomsAnswers[group].replace('\n','')


    for letter in letters:
        if letter in answers:
            yesCount += 1

print(yesCount)
