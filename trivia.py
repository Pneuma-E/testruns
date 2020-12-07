import random
class Questions:
    def __init__(self, quest, ans):
        self.quest = quest
        self.ans = ans


print('WELCOME TO THE TRIVIA')

print('This trivia contains five sections:\n 1. Ancient history \n 2. The Middle Ages\n 3. Modern history\n '
      '4. mythology questions\n')

choice = float(input('Select option: \n'))

questions1 = ['By what name were the Egyptian kings/rulers known as?\n', 'How many Pyramids of Giza were made?\n',
              'Who which queen was Julius Caesar involved with?\n']
# answers1 = ['Pharaohs', 'Three', 'Cleopatra']

question2 = ['Where did the Franks settle after defeating the Romans?\n', ' How long did the Middle Ages last?\n',
             'Which religion dominated the Middle Ages?\n']
# answers2 = ['Gaul\n', 'About 1000 years\n', 'Catholicism\n']

question3 = [' In which year World War I begin?\n', 'In which country Adolph Hitler was born?\n',
             'John F. Kennedy was assassinated in which city?\n',
             'On Sunday 18th June 1815, which famous battle took place?\n']
# answer3 = ['1914\n', 'Austria\n', 'Dallas\n', 'The Battle of Waterloo\n']

questions4 = ['What is the name of the home of the Greek Gods?\n', 'Which warrior’s weakness was their heel?\n',
              'Thor was the son of which God?\n', 'The Roman God of War inspired the name of which planet?\n']
# answers4 = ['Olympus\n', 'Achilles\n', 'Odin\n', 'Mars\n']

ques1 = [
    Questions(questions1[0], 'Pharaohs'),
    Questions(questions1[1], 'Three'),
    Questions(questions1[2], 'Cleopatra')
]

ques2 = [Questions(question2[0], 'Gaul'),
         Questions(question2[1], 'About 1000 years'),
         Questions(question2[2], 'Catholicism')]

ques3 = [Questions(question3[0], '1914'),
         Questions(question3[1], 'Austria'),
         Questions(question3[2], 'Dallas'),
         Questions(question3[3], 'The Battle of Waterloo')]

ques4 = [Questions(questions4[0], 'Olympus'),
         Questions(questions4[1], 'Achilles'),
         Questions(questions4[2], 'Odin'),
         Questions(questions4[3], 'Mars')]


def run_quiz1(ques):
    score = 0
    random.shuffle(ques)
    for i in ques:
        answer = input(i.quest)
        if answer == i.ans:
            score += 1
        else:
            print(i.ans)
    print(f'Your final score in Ancient history is {score}\n')


def run_quiz2(quesx):
    score = 0
    random.shuffle(quesx)
    for i in quesx:
        answer = input(i.quest)
        if answer == i.ans:
            score += 1
        else:
            print(i.ans)
    print(f'Your final score in The Middle Ages is {score}\n')


def run_quiz3(quesy):
    score = 0
    random.shuffle(quesy)
    for i in quesy:
        answer = input(i.quest)
        if answer == i.ans:
            score += 1
        else:
            print(i.ans)
    print(f'Your final score in Modern history is {score}\n')


def run_quiz4(quesz):
    score = 0
    random.shuffle(quesz)
    for i in quesz:
        answer = input(i.quest)
        if answer == i.ans:
            score += 1
        else:
            print(i.ans)
    print(f'Your final score in mythology questions is {score}\n')


def choices(v):
    if v == 1:
        run_quiz1(ques1)
    if v == 2:
        run_quiz2(ques2)
    if v == 3:
        run_quiz3(ques3)
    if v == 4:
        run_quiz4(ques4)


def troll():
    x = float(input('Enter section: '))
    choices(x)


if choice == 1:
    run_quiz1(ques1)
    troll()
    troll()
    troll()

if choice == 2:
    run_quiz2(ques2)
    troll()
    troll()
    troll()

if choice == 3:
    run_quiz3(ques3)
    troll()
    troll()
    troll()

if choice == 4:
    run_quiz4(ques4)
    troll()
    troll()
    troll()

# tscore = score
#
# print(f'Your total score is {tscore}')