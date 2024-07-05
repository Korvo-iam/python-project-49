import random
import prompt
from brain_games import default


GAME_NOMO = "brain_calc"
DEMANDO = 'What is the result of the expression?'


def generate():
    global randoma_simbolo, numero_1, numero_2
    simboloj = ['+', '-', '*']
    randoma_simbolo = random.choice(simboloj)
    numero_1 = random.randint(0, 20)
    numero_2 = random.randint(0, 20)
    print(DEMANDO)
    demando = (f'Question: {numero_1} {randoma_simbolo} {numero_2}')
    print(demando)


def check():
    global respondo, korekta
    if randoma_simbolo == '+':
        korekta = numero_1 + numero_2
    elif randoma_simbolo == '-':
        korekta = numero_1 - numero_2
    elif randoma_simbolo == '*':
        korekta = numero_1 * numero_2
    respondo = prompt.integer('Your answer: ')
    default.sub_check(respondo, korekta)


def main():
    generate()
    check()


if __name__ == '__main__':
    main()
