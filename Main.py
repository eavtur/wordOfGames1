from abc import ABC, abstractmethod


class Main(ABC):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        super().__init__()

    def __str__(self):
        pass

    @abstractmethod
    def get_guess_from_user(self):
        pass

    @abstractmethod
    def play(self):
        pass
