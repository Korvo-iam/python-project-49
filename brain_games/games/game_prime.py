import random
import prompt


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_guestion():
    demand = random.randint(1, 100)
    i = 1
    list = []
    question = (f'Question: {demand}')
    while i != demand:
        if demand % i == 0:
            list.append(i)
        i = i + 1
    if len(list) == 1 or demand == 1:
        correct = 'yes'
    else:
        correct = 'no'
    return question, correct
