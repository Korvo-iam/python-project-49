import random
import prompt
import math
from brain_games import default


def start():
    default.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    while default.poento != 3:
        generate_num()
        check()
        if respondo != korekta:
            break


def generate_num():
    global numero_1, numero_2
    numero_1 = random.randint(5, 50)
    numero_2 = random.randint(5, 50)
    print(f'Question: {numero_1} {numero_2}')


def check():
    global respondo, korekta
    korekta = math.gcd(numero_1, numero_2)
    respondo = prompt.integer('Your answer : ')
    if respondo == korekta:
        print('Correct!')
        default.plus_poento()
    else:
        print(f"'{respondo}' is wrong answer :(.Correct answer was '{korekta}'")
        print(f"Let's try again, {default.name}!")


def main():
    start()
    if default.poento == 3:
        print(f'Congratulations, {default.name}!')


if __name__ == '__main__':
    main()
