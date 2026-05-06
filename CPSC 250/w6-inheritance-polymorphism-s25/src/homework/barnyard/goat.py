"""
Create goat class as described in README
"""
from src.homework.barnyard.ruminant import Ruminant

class Goat(Ruminant):
    def make_sound(self):
        return super().make_sound() + " - baah"
    def can_lay_eggs(self):
        return False