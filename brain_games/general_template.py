import prompt


roundsCount = 3


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    for i in range(1, roundsCount + 1):
        print(game.QUESTION)
        question, correct = game.get_guestion()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != str(correct):
            print(f"'{answer}' is wrong answer :(."
                  f" Correct answer was '{correct}'\n"
                  f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
