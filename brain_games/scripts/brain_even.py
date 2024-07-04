import random
import prompt
from brain_games import default


GAME_NOMO = "brain_even"
DEMANDO = 'Answer "yes" if the number is even, otherwise answer "no".'

def start():
    default.welcome_user(DEMANDO)
    while default.poento != 3:
        generate()
        check()
        if respondo != korekta:
            break


def generate():
    global is_even
    randoma = random.randint(0, 20)
    print(DEMANDO)
    print(f'Question: {randoma}')
    is_even = randoma % 2


def check():
    global respondo, korekta
    respondo = prompt.string('Your answer: ')
    if is_even == 0:
        korekta = 'yes'
    elif is_even != 0:
        korekta = 'no'
    default.sub_check(respondo,korekta)


def main():
    start()
    if default.poento == 3:
        print(f'Congratulations, {default.name}!')


if __name__ == '__main__':
    main()
