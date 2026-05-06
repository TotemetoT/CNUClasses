
"""
This file will use your new class files and store data read from file!

"""

import csv
import os

from src.element import *


def load_element_data(file_path):
    """
    Load element data from given file path, and return a list of instances of
    new class that holds data
    :param file_path: relative path to file (from top level folder!)
    :return : list of class instances
    """
    instance_list = []
    with open(file_path, 'rt') as file_out:
        reader = csv.reader(file_out, delimiter=',')
        for line in reader:
            instance_list.append(Element(line))
    return instance_list


if __name__ == '__main__':

    # Set up your file path here !
    # I've given you the small file to start with.
    file_path = os.path.join("data", "big_elements.csv")

    element_data = load_element_data(file_path)


    # Call element_data.sort()) here if you can (required <)
    element_data.sort()

    for element in element_data:
        print(element)
