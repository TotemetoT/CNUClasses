"""
Create winged_animal class as described in README
"""

from src.homework.barnyard.farm_animal import FarmAnimal

class WingedAnimal(FarmAnimal):
    def make_sound(self):
        return "flap, flap"