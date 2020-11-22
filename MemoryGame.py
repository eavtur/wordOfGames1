import random
from time import sleep
from Main import Main
from Utils import get_choice, clear


class MemoryGame(Main):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.randomList = self._generate_sequence()

    def __str__(self):
        return self.get_description()

    @staticmethod
    def get_description():
        return " Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"

    def _generate_sequence(self):
        return [random.randint(1, 101) for i in range(self.difficulty)]

    def get_guess_from_user(self):
        return [
            get_choice(1, 101, "Please enter {num} num: ".format(num=i + 1))
            for i in range(self.difficulty)
        ]

    def _is_list_equal(self, user_list):
        equal = True
        for i in range(self.difficulty):
            if self.randomList[i] != user_list[i]:
                equal = False
                break
        return equal

    def play(self):
        clear()
        print("Please remember those numbers:")
        for num in self.randomList:
            print(num)
        sleep(0.7)
        clear()
        user_list = self.get_guess_from_user()
        return self._is_list_equal(user_list)
