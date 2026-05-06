"""
Create cow class as described in README
"""

from src.homework.barnyard.ruminant import Ruminant

class Cow(Ruminant):
    def make_sound(self):
        return super().make_sound() + " - moo"
    def can_lay_eggs(self):
        return False