import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    i = 1
    list = []
    while i != num:
        if num < i:
            break
        if num % i == 0:
            list.append(i)
        i = i + 1
    return True if len(list) == 1 and num != 1 else False


def get_guestion():
    question = random.randint(1, 100)
    correct = 'yes' if is_prime(question) else 'no'
    return question, correct
