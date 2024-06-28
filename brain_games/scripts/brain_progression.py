import random
import prompt
from brain_games import default


def start():
    default.welcome_user()
    print('What number is missing in the progression?')
    while default.poento != 3:
        generate_num()
        check()
        if respondo != korekta:
            break


def generate_num():
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
    print(f'Question: {numeroj_str}')


def check():
    global respondo
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
