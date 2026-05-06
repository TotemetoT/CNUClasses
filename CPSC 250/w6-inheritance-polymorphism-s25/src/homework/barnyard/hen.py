"""
Create hen class as described in README
"""


from src.homework.barnyard.chicken import Chicken

class Hen(Chicken):
    def make_sound(self):
        return super().make_sound() + " - squawk!"
    def can_lay_eggs(self):
        return True