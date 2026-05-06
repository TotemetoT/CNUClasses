"""
Create farm_animal class as described in README
"""
class FarmAnimal:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'{self.__class__.__name__}, Age: {self.age}'

    def make_sound(self):
        return ""

    def __eq__(self,other):
        return isinstance(other, self.__class__) and self.age == other.age