import random
import prompt
from brain_games import default


def start():
    default.welcome_user()
    print('What is the result of the expression?')
    while default.poento != 3:
        generate_calc()
        check()
        if respondo != korekta:
            break


def generate_calc():
    global randoma_simbolo, numero_1, numero_2
    simboloj = ['+', '-', '*']
    randoma_simbolo = random.choice(simboloj)
    numero_1 = random.randint(0, 20)
    numero_2 = random.randint(0, 20)
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
