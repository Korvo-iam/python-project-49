import random
import prompt


DEMANDO = 'What number is missing in the progression?'


def generate():
    global respondo, korekta
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
    demando = " ".join(numeroj)
    print(DEMANDO)
    print(f'Question: {demando}')
    respondo = prompt.integer('Your answer: ')


def main():
    generate()


if __name__ == '__main__':
    main()
