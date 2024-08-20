import random


QUESTION = 'What number is missing in the progression?'


def get_guestion():
    length = 10
    start = random.randint(1,10)
    step = random.randint(1,10)
    stop = start + (length * step)
    numbers = list(range(start, stop, step))
    digit = random.randint(0, length - 1)
    correct = numbers[digit]
    numbers[digit] = '..'
    numbers = [str(element) for element in numbers]
    question = f'{" ".join(numbers)}'
    return question, correct
