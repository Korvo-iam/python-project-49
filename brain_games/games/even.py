import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_guestion():
    random_num = random.randint(0, 20)
    is_even = random_num % 2
    question = f'{random_num}'
    correct = 'yes' if is_even == 0 else 'no'
    return question, correct
