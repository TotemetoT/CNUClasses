
"""
This file works as given, but we need to change it to make the
separate_types.py work in the given folder

"""

import csv
import os

from given.element import Element

# You may add code here if needed
class Metal(Element):
    """
    Maked an instance of Element under the class Metal
    """
    def __init__(self, name, symbol, np, nn, ne):
        Element.__init__(self,name,symbol,np,nn,ne)
class Nonmetal(Element):
    """
    Maked an instance of Element under the class Non-Metal
    """
    def __init__(self, name, symbol, np, nn, ne):
        Element.__init__(self,name,symbol,np,nn,ne)
class Metalloid(Element):
    """
    Maked an instance of Element under the class Metalloid
    """
    def __init__(self, name, symbol, np, nn, ne):
        Element.__init__(self,name,symbol,np,nn,ne)


# Change this to choose which file to load
# Using ALL_CAPS style because treated as a constant
ELEMENT_FILE_PATH = os.path.join("data", "small_elements.csv")
# ELEMENT_FILE_PATH = os.path.join("data", "big_elements.csv")
# ELEMENT_FILE_PATH = os.path.join("data", "full_elements.csv")

def load_element_data(file_path):
    """
    Load element data from given file path, and return a list of instances of
    new class that holds data

    Most of the given code works, but you might want to change what you append to list

    :param file_path: relative path to file (from top level folder!)
    :return : dictionary of class instances
    """

    with open(file_path, 'rt', encoding="utf-8") as fin:
        reader = csv.reader(fin, delimiter=',')
        elements = []
        for line in reader:
            name, symbol, np, nn, ne, element_type = line
            if element_type == "Nonmetal":
                elements.append(Nonmetal(name, symbol, int(np),int(nn),int(ne)))
            if element_type == "Metal":
                elements.append(Metal(name, symbol, int(np),int(nn),int(ne)))
            if element_type == "Metalloid":
                elements.append(Metalloid(name, symbol, int(np),int(nn),int(ne)))
        return elements

def get_metals(element_list):
    """
    Return list of only metals
    @param element_list: list of element instances
    @return : list of only metal instances
    """
    metals = []
    for element in element_list:
        if isinstance(element, Metal):
            metals.append(element)
    return metals

def get_nonmetals(element_list):
    """
    Return list of only metals
    @param element_list: list of element instances
    @return : list of only metal instances
    """
    nonmetal = []
    for element in element_list:
        if isinstance(element, Nonmetal):
            nonmetal.append(element)
    return nonmetal

def get_metalloids(element_list):
    """
    Return list of only metals
    @param element_list: list of element instances
    @return : list of only metal instances
    """
    metalloid = []
    for element in element_list:
        if isinstance(element, Metalloid):
            metalloid.append(element)
    return metalloid


if __name__ == '__main__':
    # No need to change below here
    # Just given for basic testing

    element_data = load_element_data(ELEMENT_FILE_PATH)
    # print(element_data)
    # Call element_data.sort())
    element_data.sort()

    # Print the data for each instance here
    # allString = ""
    # for key in element_data:
    #     if key == "Nonmetal":
    #         allString += f'---- Non-Metals ----\n'
    #     else:
    #         allString += f'---- {key}s ----\n'
    #     for element in element_data[key]:
    #         allString += f'{element}\n'
    # print(allString)
