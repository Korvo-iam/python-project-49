import random
import prompt
ne = 'no'
jes = 'yes'

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
    respondo = input('Your answer: ')
    is_even = randoma % 2
    if is_even == 0 and respondo == "yes":
        print("Correct!!!")
        plus_poento()
    elif is_even != 0 and respondo == "no":
        print("Correct!!!")
        plus_poento()
    else:
        if respondo == jes:
            print(f"'{respondo}' is wrong answer ;(. Correct answer was '{ne}'")
        elif respondo == ne:
            print(f"'{respondo}' is wrong answer ;(. Correct answer was '{jes}'")
        print(f"Let's try again, {name}!")


def main():
    start()
    check()
    check()
    check()


if __name__ == '__main__':
    main()
