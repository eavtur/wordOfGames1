from os import name, system

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 500


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def get_choice(min=1, max=3, message="Please enter your choice: ", type=int):
    try:
        choice = type(input(message))
        if choice > max or choice < min:
            raise ValueError
        return choice
    except ValueError:
        print("Incorrect number choice, please try again")
        return get_choice(min, max)