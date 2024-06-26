import random
import prompt
import math
from brain_games import default


def start():
    default.welcome_user()
    print('Find the greatest common divisor of given numbers.')


def generate_num():
    global numero_1, numero_2
    numero_1 = random.randint(5, 50)
    numero_2 = random.randint(5, 50)
    demando = (f'{numero_1} {numero_2}')
    print(f'Question : {demando}')


def check():
    korekta = math.gcd(numero_1, numero_2)
    respondo = prompt.integer('Your answer : ')
    if respondo == korekta:
        print('Correct!')
        default.plus_poento()
    else:
        print(f"'{respondo}' is wrong answer :(.Correct answer was '{korekta}'")
        print(f"Let's try again, {default.name}!")


def sub_main():
    generate_num()
    check()


def main():
    start()
    sub_main()
    sub_main()
    sub_main()
    if default.poento == 3:
        print(f'Congratulations, {default.name}!')


if __name__ == '__main__':
    main()
