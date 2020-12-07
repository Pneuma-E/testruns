ques1 = ''
ques2 = ''
ques3 = ''
ques4 = ''


def run_quiz1(ques):
    score = 0
    for i in ques:
        answer = input(i.quest)
        if answer == i.ans:
            score += 1
        else:
            print(i.ans)
    print(f'Your final score in Ancient history is {score}\n')


def run_quiz2(quesx):
    score = 0
    for i in quesx:
        answer = input(i.quest)
        if answer == i.ans:
            score += 1
        else:
            print(i.ans)
    print(f'Your final score in The Middle Ages is {score}\n')


def run_quiz3(quesy):
    score = 0
    for i in quesy:
        answer = input(i.quest)
        if answer == i.ans:
            score += 1
        else:
            print(i.ans)
    print(f'Your final score in Modern history is {score}\n')


def run_quiz4(quesz):
    score = 0
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
