import random
import prompt


def welcome_user():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def plus_poento():
    global poento
    poento = poento + 1


def start():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    global poento
    poento = 0


def check():
    randoma = random.randint(0, 20)
    print(f'Question: {randoma}')
    respond = prompt.string('Your answer: ')
    is_even = randoma % 2
    if is_even == 0:
        korekta = 'yes'
    elif is_even != 0:
        korekta = 'no'
    if respond == korekta:
        print('Correct!')
        plus_poento()
    else:
        print(f"'{respond}' is wrong answer :(. Correct answer was '{korekta}'")
        print(f"Let's try again, {name}!")


def main():
    start()
    check()
    check()
    check()
    if poento == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
