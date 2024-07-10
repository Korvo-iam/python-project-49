import random
import prompt
import math


DEMANDO = 'Find the greatest common divisor of given numbers.'


def generate():
    global respondo, korekta
    numero_1 = random.randint(5, 50)
    numero_2 = random.randint(5, 50)
    print(DEMANDO)
    print(f'Question: {numero_1} {numero_2}')
    korekta = math.gcd(numero_1, numero_2)
    respondo = prompt.integer('Your answer: ')


def main():
    generate()


if __name__ == '__main__':
    main()
