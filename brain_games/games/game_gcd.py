import random
import prompt
import math


DEMANDO = 'Find the greatest common divisor of given numbers.'


def generate():
    numero_1 = random.randint(5, 50)
    numero_2 = random.randint(5, 50)
    print(f'Question: {numero_1} {numero_2}')
    korekta = math.gcd(numero_1, numero_2)
    respondo = prompt.integer('Your answer: ')
    return respondo, korekta
