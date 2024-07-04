import prompt


poento = 0


def welcome_user():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def plus_poento():
    global poento
    poento = poento + 1


def sub_check(rspnd, prava):
    if rspnd == prava:
        print('Correct!')
        plus_poento()
    else:
        print(f"'{rspnd}' is wrong answer :(.Correct answer was '{prava}'")
        print(f"Let's try again, {name}!")


def start_def(game):
    print (type(game))
    print('succcesss')
    from brain_games.scripts import game
    global poento
    welcome_user()
    while poento != 3:
        game.generate()
        game.check()
        if game.respondo != game.korekta:   
            break
    if poento == 3:
        print(f'Congratulations, {name}!')