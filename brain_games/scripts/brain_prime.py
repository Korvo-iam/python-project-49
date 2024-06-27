import random
import prompt
from brain_games import default


def start():
    default.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def generate_num():
    global numero_1
    global korekta
    numero_1 = random.randint(1, 100)
    global korekta
    print(f'Question : {numero_1}')
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
    respondo = prompt.string('Your answer : ')
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
