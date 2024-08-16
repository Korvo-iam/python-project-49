import random

QUESTION = 'What is the result of the expression?'


def get_guestion():
    symbols = ('+', '-', '*')
    random_symbol = random.choice(symbols)
    num_1 = random.randint(0, 20)
    num_2 = random.randint(0, 20)
    symb_dicts = {
        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2}
    question = f'{num_1} {random_symbol} {num_2}'
    correct = symb_dicts[random_symbol]
    return question, correct
