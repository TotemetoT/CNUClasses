from src.homework.barnyard.farm_animal import FarmAnimal
from src.homework.barnyard.hen import Hen
from src.homework.barnyard.rooster import Rooster
from src.homework.barnyard.duck import Duck
from src.homework.barnyard.goat import Goat
from src.homework.barnyard.cow import Cow


def get_barnyard():
    """
    Return a list of animals as described in README
    :return : list of animal instances
    """
    animals = []
    hen = [0.25,0.6,1.0,8]
    rooster = [0.25,0.6,1.0]
    duck = [0.5]
    cow = [0.87]
    goat = [1.5]
    for i in hen:
        animals.append(Hen(i))
    for i in rooster:
        animals.append(Rooster(i))
    for i in duck:
        animals.append(Duck(i))
    for i in cow:
        animals.append(Cow(i))
    for i in goat:
        animals.append(Goat(i))
    return animals


def get_layers(animals):
    """
    Given list of animals, return ones that can lay eggs
    :param animals: list of animal instances
    :return : list of "layers"
    """
    layers = []
    for animal in animals:
        if isinstance(animal, (Hen, Duck)) and 0.5 <= animal.age <= 7:  # Only Hens and Ducks are considered layers
            layers.append(animal)
    return layers

def get_roosters(animals):
    """
    Given list of animals, return ones that are roosters
    :param animals: list of animal instances
    :return : list of rooster instances
    """
    roosters = []
    for animal in animals:
        if isinstance(animal, Rooster):
            roosters.append(animal)
    return roosters

def listen(animals):
    """
    Given list of animals, return list of sounds they make
    :param animals: list of animal instances
    :return : list of sounds
    """
    sounds = []
    for animal in animals:
        if isinstance(animal, FarmAnimal):  # Ensure it's a valid FarmAnimal instance
            sounds.append(animal.make_sound())
        else:
            print(f"Warning: Found an unexpected object in animals list: {animal}")
    return sounds



if __name__ == '__main__':

    animals = get_barnyard()
    print("All animals:",[str(ani) for ani in animals])
    # print(" listen: ",listen(animals))
    print(" Laying hens:", [str(ani) for ani in get_layers(animals)])
    print(" Roosters: ",[str(ani) for ani in get_roosters(animals)])
