import random
import prompt
from brain_games import default


GAME_NOMO = "brain_progression"
DEMANDO = 'What number is missing in the progression?'


def generate():
    global numeroj_str, korekta
    i = 0
    numero_1 = random.randint(0, 10)
    numero_2 = random.randint(1, 10)
    longo = 10
    numeroj = []
    while i != longo:
        i = i + 1
        numeroj.append(numero_1)
        numero_1 = numero_1 + numero_2
    cifero = random.randint(0, longo - 1)
    korekta = numeroj[cifero]
    numeroj[cifero] = '..'
    numeroj = [str(element) for element in numeroj]
    numeroj_str = " ".join(numeroj)
    print(DEMANDO)
    print(f'Question: {numeroj_str}')


def check():
    global respondo
    respondo = prompt.integer('Your answer: ')
    default.sub_check(respondo, korekta)


def main():
    generate()
    check()


if __name__ == '__main__':
    main()
