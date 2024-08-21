import random
import operator

QUESTION = 'What is the result of the expression?'


def get_guestion():
    symb_dicts = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    num_1 = random.randint(0, 20)
    num_2 = random.randint(0, 20)
    random_operator = random.choice(list(symb_dicts.keys()))
    correct = symb_dicts[random_operator](num_1, num_2)
    question = f'{num_1} {random_operator} {num_2}'
    return question, correct
