"""
Read element data from file, and then process list to store a mapping
from symbol to instance.

You'll need this to calculate the total atomic weight for given molecule.

Then read the molecular data file.
Start with "small", then work your way up to "full" data


You can write your class to hold molecule data in this file to save time if you want


"""

import os
import csv
from xml.etree.ElementTree import ElementTree

from given.element import Element
from src.get_elements import load_element_data


# You may need more imports!


# You can choose to create a new file or write your class to hold molecule data here
class Molecule:
    """
    Makes an instance of a molecule that shows it's:
    > name
    > compound
    > atomic mass

    Takes input from a broken down version of the molecule CSV files
    """
    def __init__(self, name="", compound=""):
        self.name = name
        self.compound = compound
        self.filepath = "data/full_elements.csv"
        self.broken = self.breakdown()
        self.all_elements = self.element_dict()
        self.atomic_mass = self.molecule_atomic_mass()

    def breakdown(self):
        """

        Returns: dictionary containing how many of what element is in the molecule

        """
        item_dict = {}
        temp_string = ""
        temp_int = ""
        compound = self.compound
        for char in compound:
            if char.isupper():
                if temp_string:
                    if temp_int:
                        item_dict[temp_string] = temp_int
                    else:
                        item_dict[temp_string] = 1
                    temp_string, temp_int = "", ""
                temp_string = char
            elif char.islower():
                temp_string += char
            else:
                temp_int += char
        if temp_string:
            if temp_int:
                item_dict[temp_string] = temp_int
            else:
                item_dict[temp_string] = 1
        return item_dict

    def molecule_atomic_mass(self):
        """

        Returns: float total mass of the given molecule

        """
        e_dict = self.all_elements
        b_dict = self.broken
        total_mass = 0
        for key in b_dict:
            amount = float(b_dict[key])
            mass = float(e_dict[key])
            total_mass += float(amount*mass)
        return round(total_mass, 5)

    def element_dict(self):
        """

        Returns: dictionary of all possible elements and their atomic mass

        """
        e_dict = {}
        fpath = self.filepath
        with open(fpath, 'r', newline='') as file:
            lines = csv.reader(file, delimiter=',')
            for line in lines:
                element = Element(line[1], line[0], int(line[2]), int(line[3]), int(line[4]))
                symbol = element.get_symbol()
                mass = element.atomic_mass()
                e_dict[symbol] = mass
        return e_dict

    def __str__(self):
        return f'{self.name}, {self.compound}, {self.molecule_atomic_mass()} kg/mol'

def read_molecule_data(file_path):
    """

    Args:
        file_path: full molecule data filepath

    Returns: list of instances of molecules

    """
    molecule_list = []
    super_molecule_list = []
    with open(file_path,'rt') as fin:
        reader = csv.reader(fin, delimiter=',')
        for read in reader:
            if read[0][0] != '#':
                molecule_list.append([read[0],read[1]])
    for molecule in molecule_list:
        super_molecule_list.append(Molecule(molecule[0],molecule[1]))
    return super_molecule_list


if __name__ == '__main__':
    # Read the element data (using method from get_elements)
    # I'll get you started here
    ELEMENT_FILE_PATH = os.path.join("data", "full_elements.csv")
    element_data = load_element_data(ELEMENT_FILE_PATH)
    element_data.sort()
    print(element_data)
    print(40 * "=")
    print("    Element Data")
    for element in element_data:
        print(element)
    print(40 * "=")

    # Create a dictionary for use by molecule.  Map the element symbol name
    # to instance of element data for that symbol (*instance* not class definition here!)
    #
    # Hint: You may want to store the dictionary as a class attribute to simplify code
    # @todo - fix this


    # Change this to choose which file to load
    # Using ALL_CAPS style because treated as a constant
    # MOLECULE_FILE_PATH = os.path.join("data", "small_molecules.csv")
    # MOLECULE_FILE_PATH = os.path.join("data", "big_molecules.csv")
    MOLECULE_FILE_PATH = os.path.join("data", "full_molecules.csv")
    molecule_data = read_molecule_data(MOLECULE_FILE_PATH)
    molecule_data.sort(key=lambda m: m.atomic_mass)

    # print the data for each instance here as described in README
    print(40*"=")
    print("    Molecule Data")
    for molecule in molecule_data:
        print(molecule)
    print(40*"=")

    path = os.path.join("data", "saved_molecules")
    # Clear File
    with open(path, "w") as file:
        file.write("")
    with open(path, "a") as file:
        for i in molecule_data:
            file.write(f'{i}\n')

