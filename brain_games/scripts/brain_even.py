import random
import prompt
from brain_games import default


def start():
    default.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')


def check():
    randoma = random.randint(0, 20)
    print(f'Question: {randoma}')
    respond = input('Your answer: ')
    is_even = randoma % 2
    if is_even == 0:
        korekta = 'yes'
    elif is_even != 0:
        korekta = 'no'
    if respond == korekta:
        print('Correct!')
        default.plus_poento()
    else:
        print(f"'{respond}' is wrong answer :(.Correct answer was '{korekta}'")
        print(f"Let's try again, {default.name}!")


def main():
    start()
    check()
    check()
    check()
    if default.poento == 3:
        print(f'Congratulations, {default.name}!')


if __name__ == '__main__':
    main()
