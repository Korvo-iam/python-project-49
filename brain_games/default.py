import prompt


max_rounds = 3


def start_def(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for i in range(1, max_rounds + 1):
        print(game.DEMANDO)
        respondo, korekta = game.generate()
        if respondo == korekta:
            print('Correct!')
        else:
            g_r = respondo
            g_k = korekta  # flake8 жаловался на длинну следующей строки
            print(f"'{g_r}' is wrong answer :(.Correct answer was '{g_k}'")
            print(f"Let's try again, {name}!")
            break
        if i == max_rounds:
            print(f'Congratulations, {name}!')
