import random


QUESTION = 'What is the result of the expression?'


def get_guestion():
    symbols = ['+', '-', '*']
    random_symbol = random.choice(symbols)
    num_1 = random.randint(0, 20)
    num_2 = random.randint(0, 20)
    question = (f'Question: {num_1} {random_symbol} {num_2}')
    if random_symbol == '+':
        correct = num_1 + num_2
    elif random_symbol == '-':
        correct = num_1 - num_2
    elif random_symbol == '*':
        correct = num_1 * num_2
    return question, correct
