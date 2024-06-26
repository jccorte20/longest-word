import string
import random
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        url = f'https://dictionary.lewagon.com/{word}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            return data.get('found')
        else :
            return False

