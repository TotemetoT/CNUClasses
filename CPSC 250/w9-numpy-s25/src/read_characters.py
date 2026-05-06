import csv
from src.game import *


def read_characters_from_file(file_path):
    """
    Read characters from file and return a list of Humanoid instances
    """

    classes = {}

    for class_def in Humanoid.__subclasses__():
        classes[class_def.__name__] = class_def
    # print(classes)

    characters = []
    with open(file_path, "rt") as fin:
        reader = csv.reader(fin, delimiter=",")

        for line in reader:
            if line[0][0] == '#':
                continue
            characters.append(classes[line[1]](line[0], *[int(val) for val in line[2:]]))
    return characters


if __name__ == '__main__':

    characters = read_characters_from_file("data/characters.csv")
    for char in characters:
        print(char)
