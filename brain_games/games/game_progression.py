import random
import prompt


QUESTION = 'What number is missing in the progression?'


def get_guestion():
    i = 0
    num_1 = random.randint(0, 10)
    num_2 = random.randint(1, 10)
    length = 10
    numbers = []
    while i != length:
        i = i + 1
        numbers.append(num_1)
        num_1 = num_1 + num_2
    digit = random.randint(0, length - 1)
    correct = numbers[digit]
    numbers[digit] = '..'
    numbers = [str(element) for element in numbers]
    demand = " ".join(numbers)
    question = (f'Question: {demand}')
    return question, correct
