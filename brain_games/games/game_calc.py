import random
import prompt


DEMANDO = 'What is the result of the expression?'


def generate():
    simboloj = ['+', '-', '*']
    randoma_simbolo = random.choice(simboloj)
    numero_1 = random.randint(0, 20)
    numero_2 = random.randint(0, 20)
    demando = (f'Question: {numero_1} {randoma_simbolo} {numero_2}')
    print(demando)
    if randoma_simbolo == '+':
        korekta = numero_1 + numero_2
    elif randoma_simbolo == '-':
        korekta = numero_1 - numero_2
    elif randoma_simbolo == '*':
        korekta = numero_1 * numero_2
    respondo = prompt.integer('Your answer: ')
    return respondo, korekta
