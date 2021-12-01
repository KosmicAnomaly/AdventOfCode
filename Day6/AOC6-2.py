import json

CustomsAnswers = open ('Day6\CustomsAnswers.json','r').read().split('\n\n')


letters = 'abcdefghijklmnopqrstuvwxyz'
yesCount = 0

for group in range(len(CustomsAnswers)):
    groupAnswers = CustomsAnswers[group].split('\n')
    print(groupAnswers)

    members = len(groupAnswers)

    if len(groupAnswers[members-1]) == 0:
        groupAnswers.pop()
        members -= 1
        print('last item too short')

    groupYesCount = 0

    print(groupAnswers[0])

    for yes in groupAnswers[0]:
        groupSharedYesCount = 0
        for answer in groupAnswers:
            if yes in answer:
                groupSharedYesCount += 1
        if groupSharedYesCount == members:
            groupYesCount += 1
        print(f'{yes}: {groupSharedYesCount}/{members}')

    yesCount += groupYesCount
    print(groupYesCount)
    print(f'======= {yesCount} =======')
