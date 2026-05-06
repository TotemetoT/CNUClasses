"""
Create chicken class as described in README
"""
from src.homework.barnyard.winged_animal import WingedAnimal

class Chicken(WingedAnimal):
    def make_sound(self):
        return super().make_sound() + " - cluck, cluck"