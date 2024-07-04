import random
import prompt
import math
from brain_games import default

GAME_NOMO = "brain_gcd"
DEMANDO = 'Find the greatest common divisor of given numbers.'

def start():
    default.welcome_user(DEMANDO)
    while default.poento != 3:
        generate()
        check()
        if respondo != korekta:
            break


def generate():
    global numero_1, numero_2
    numero_1 = random.randint(5, 50)
    numero_2 = random.randint(5, 50)
    print(DEMANDO)
    print(f'Question: {numero_1} {numero_2}')


def check():
    global respondo, korekta
    korekta = math.gcd(numero_1, numero_2)
    respondo = prompt.integer('Your answer: ')
    default.sub_check(respondo,korekta)


def main():
    start()
    if default.poento == 3:
        print(f'Congratulations, {default.name}!')


if __name__ == '__main__':
    main()
