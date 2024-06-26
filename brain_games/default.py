import prompt


def welcome_user():
    global name, poento
    poento = 0
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def plus_poento():
    global poento
    poento = poento + 1