import random
import prompt
from brain_games import default


GAME_NOMO = "brain_prime"
DEMANDO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate():
    global numero_1, korekta
    numero_1 = random.randint(1, 100)
    print(DEMANDO)
    print(f'Question: {numero_1}')
    i = 1
    listo = []
    while i != numero_1:
        if numero_1 % i == 0:
            listo.append(i)
        i = i + 1
    if len(listo) == 1 or numero_1 == 1:
        korekta = 'yes'
    else:
        korekta = 'no'


def check():
    global respondo
    respondo = prompt.string('Your answer: ')
    default.sub_check(respondo, korekta)


def main():
    generate()
    check()


if __name__ == '__main__':
    main()
