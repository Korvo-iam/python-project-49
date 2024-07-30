import prompt


MAX_ROUNDS = 3
WELCOME = "Welcome to the Brain Games!\n" + "May I have your name? "


def start_def(game):
    name = prompt.string(WELCOME)
    print(f'Hello, {name}!')
    for i in range(1, MAX_ROUNDS + 1):
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
        if i == MAX_ROUNDS:
            print(f'Congratulations, {name}!')
