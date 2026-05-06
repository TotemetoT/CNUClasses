import csv
import os
from src.planet import Planet


def generate_planet_list(fpath):
    """
    Read in the data from data/planets.txt (ignoring comment lines)
    construct a list of Planet instances and return the list of planets.
    When reading in the file ignore lines that start with '#' as they are comment lines.

    :param fpath:
    :return planet_list: Return a list of planet objects
    """
    #pass  # @todo - fix this
    planet_list = []

    with open(fpath, "rt") as fin:
        reader = csv.reader(fin, delimiter=",")
        for line in reader:
            if line[0][0] == '#':
                continue
            name = line[0]
            radius = 1000.0 * float(line[1]) / 2.0  # Convert diameter in km to radius in meters
            mass = float(line[2])
            planet_list.append(Planet(name, radius, mass))
    return planet_list


if __name__ == '__main__':
    file_path = os.path.join("data", "planets.txt")
    planets = generate_planet_list(file_path)

    print("Look a list of planet objects: ")
    print(planets)

    print("\n\nPlanet data:")
    for planet in planets:
        print(planet.get_density(), end=",")
