import random
from turtle import clear
import requests
from Main import Main
from Utils import get_choice


class CurrencyRouletteGame(Main):
    _api_url = "https://api.exchangeratesapi.io/latest?symbols=ILS&base=USD"

    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.interval = self.get_money_interval()

    def __str__(self):
        return self.get_description()

    @staticmethod
    def get_description():
        return " Currency Roulette - try and guess the value of a random amount of USD in ILS"

    def get_money_interval(self):
        total = random.randint(1, 100)
        response = requests.get(self._api_url).json()
        ils_usd_rate = response['rates']['ILS']
        return {"min": ils_usd_rate * (total - (5 - self.difficulty)),
                "max": ils_usd_rate * (total + (5 - self.difficulty))}

    def get_guess_from_user(self):
        message = "Please input the value of USD in ILS? "
        return get_choice(min=1, max=1000, message=message, type=float)

    def compare_results(self, guess):
        if guess >= self.interval['min'] and guess <= self.interval['max']:
            return True
        return False

    def play(self):
        clear()
        user_guess = self.get_guess_from_user()
        return self.compare_results(user_guess)
