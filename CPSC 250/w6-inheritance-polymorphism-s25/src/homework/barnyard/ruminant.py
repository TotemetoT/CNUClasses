"""
Create ruminant class as described in README
"""

from src.homework.barnyard.farm_animal import FarmAnimal

class Ruminant(FarmAnimal):
    def make_sound(self):
        return "burp"