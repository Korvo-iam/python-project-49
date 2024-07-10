import random
import prompt


DEMANDO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate():
    global respondo, korekta
    demando = random.randint(1, 100)
    print(DEMANDO)
    print(f'Question: {demando}')
    i = 1
    listo = []
    while i != demando:
        if demando % i == 0:
            listo.append(i)
        i = i + 1
    if len(listo) == 1 or demando == 1:
        korekta = 'yes'
    else:
        korekta = 'no'
    respondo = prompt.string('Your answer: ')


def main():
    generate()


if __name__ == '__main__':
    main()
