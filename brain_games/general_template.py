import prompt


roundsCount = 3


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    for i in range(1, roundsCount + 1):
        print(game.QUESTION)
        question, correct = game.get_guestion()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == str(correct):
            print('Correct!')
        else:
            g_a = answer
            g_c = correct  # flake8 жаловался на длинну следующей строки
            print(f"'{g_a}' is wrong answer :(.Correct answer was '{g_c}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
