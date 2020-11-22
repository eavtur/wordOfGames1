from CurrencyRouletteGame import CurrencyRouletteGame
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from Score import add_score
from Utils import get_choice


def welcome(name):
    return "Hello " + name + " and welcome to the World of Games (WoG)." + '\n' + "Here you can find many cool games " \
                                                                                  "to play. "


def load_game():
    games = [MemoryGame, GuessGame, CurrencyRouletteGame]
    for i, game in enumerate(games):
        print("{num}: {description}".format(
            num=i + 1, description=game.get_description()))
    choice = get_choice(1, len(games))
    difficulty = get_choice(
        min=1, max=5, message="Please choose game difficulty from 1 to 5: ")
    result = games[choice - 1](difficulty).play()
    if result:
        add_score(difficulty)
        print("You Won!")
    else:
        print("You lose, please try again")