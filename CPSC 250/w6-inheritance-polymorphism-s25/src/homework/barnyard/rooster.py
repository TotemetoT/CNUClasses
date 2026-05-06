"""
Create rooster class as described in README
"""

from src.homework.barnyard.chicken import Chicken

class Rooster(Chicken):
    def make_sound(self):
        return "flap, flap - cock-a-doodle doo!"
    def can_lay_eggs(self):
        return False
