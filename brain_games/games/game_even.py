import random
import prompt


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_guestion():
    random_num = random.randint(0, 20)
    question = (f'Question: {random_num}')
    is_even = random_num % 2
    if is_even == 0:
        correct = 'yes'
    else:
        correct = 'no'
    return question, correct
