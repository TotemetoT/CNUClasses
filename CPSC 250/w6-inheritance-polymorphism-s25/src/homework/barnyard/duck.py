"""
Create duck class as described in README
"""
from src.homework.barnyard.winged_animal import WingedAnimal

# class WingedAnimal(FarmAnimal):
#     def make_sound(self):
#         return "flap, flap"

class Duck(WingedAnimal):
    def make_sound(self):
        return super().make_sound() + " - quack, quack"
    def can_lay_eggs(self):
        return True