import random
from Main import Main
from Utils import get_choice


class GuessGame(Main):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self._generate_number()

    def __str__(self):
        return self.get_description()

    @staticmethod
    def get_description():
        return " Guess Game - guess a number and see if you chose like the computer"

    def _generate_number(self):
        self.secret = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        return get_choice(min=1, max=self.difficulty, message="Please insert your guess: ")

    def compare_results(self, guess):
        return guess == self.secret

    def play(self):
        guess = self.get_guess_from_user()
        return self.compare_results(guess)


