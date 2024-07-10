import random
import prompt


DEMANDO = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate():
    global respondo, korekta
    randoma = random.randint(0, 20)
    print(DEMANDO)
    print(f'Question: {randoma}')
    is_even = randoma % 2
    respondo = prompt.string('Your answer: ')
    if is_even == 0:
        korekta = 'yes'
    elif is_even != 0:
        korekta = 'no'


def main():
    generate()


if __name__ == '__main__':
    main()
