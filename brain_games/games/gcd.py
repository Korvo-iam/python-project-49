import random
import math

QUESTION = 'Find the greatest common divisor of given numbers.'


def get_guestion():
    num_1 = random.randint(5, 50)
    num_2 = random.randint(5, 50)
    question = f'{num_1} {num_2}'
    correct = math.gcd(num_1, num_2)
    return question, correct
