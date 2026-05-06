"""
In this file, read the element data from file.

Separate by type and print to screen sorted by atomic mass

You will need to fix src/get_elements.py so this works correctly!

"""

# Import all classes and functions required
from given.element import Element
from src.get_elements import ELEMENT_FILE_PATH
from src.get_elements import load_element_data
from src.get_elements import get_metals
from src.get_elements import get_nonmetals
from src.get_elements import get_metalloids


if __name__ == '__main__':

    element_data = load_element_data(ELEMENT_FILE_PATH)
    element_data.sort()

    for element in element_data:
        assert isinstance(element, Element)

    non_metals = get_nonmetals(element_data)
    metals = get_metals(element_data)
    metalloids = get_metalloids(element_data)

    print("---- Non-metals ----")
    for element in non_metals:
        print(element)

    print("---- Metals ----")
    for element in metals:
        print(element)

    print("---- Metalloids ----")
    for element in metalloids:
        print(element)
