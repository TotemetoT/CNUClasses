"""
Homework - Review

NOTE: First, fix the function names as described below

@author Ryan Schatzberg
@version 1/26/2025
"""


def get_rectangle_perimeter(length, width):
    """
    Return the perimeter of a rectangle

    Note: you can assume that length and width are valid numbers
    (either an int or a float)

    :param length:
    :param width:
    :return: perimeter of a rectangle - perimeter = 2*length + 2*width
    """
    return int(2*length + 2*width)


def get_box_volume_and_area(length,width,height):
    """
    Using standard Python naming conventions,
    create a function to "Get Box Volume and Area"


    Note: you can assume that length, width, and height are valid numbers
    (either an int or a float)

    volume of a rectangular box volume = length*width*height
    surface area of a rectangular box (Add up the area of each of the 6 sides)

    :param length:
    :param width:
    :param height:
    :return: a tuple with (volume, area)
    """
    volume = float(length*width*height)
    if volume%1 == 0:
        volume = int(volume)
    area = float(2*length*width+2*length*height+2*height*width)
    if area%1 == 0:
        area = int(area)
    return volume,area
def get_coulomb_force(q1,q2,radius):
    """
    Using standard Python naming conventions,
    create a function to "Get Coulomb Force"

    The order of the arguments matters here.
    The correct order is: charge1, charge2, with the radius last.

    Use 8.987E9 for coulomb's constant, k.

    :param q1: charge1
    :param q2: charge2
    :param radius:
    :return: coulomb force F=k*(q1*q2)/r^2
    """
    k = 8.987E9
    coulomb = float(k*(((q1)*(q2))/radius**2))
    return coulomb


def get_last_names(names):
    """
    Given a list of strings, return a new list with only the last name
    Important: Name strings may contain middle names,
    so be sure you are returning the last name

    e.g. given ["Dwight Schrute", "Michael Scott", "Pam Beesly",
                "Jim Halpert", "Angela Noelle Martin"]
         return ["Schrute", "Scott", "Beesly", "Halpert", "Martin"]

    :param names:
    :return: a list of last names
    """
    last_name = []
    for i in range(len(names)):
        for j in range(len(names[i])):
            if names[i][j] == ' ':
                num = j+1
        last_name.append(names[i][num:])
    return last_name

def get_initials(names):
    """
    Given a list of strings, return a new list with the person's initials
    Important: Name strings may contain middle names. Middle names should be
    included in initials as shown in the example below

    e.g. given ["Dwight Schrute", "Michael Scott", "Pam Beesly",
                "Jim Halpert", "Angela Noelle Martin"]
         return ["DS", "MS", "PB", "JH", "ANM"]

    :param names:
    :return: a list of initials
    """
    initial = []
    for i in range(len(names)):
        init = ""
        for j in range(len(names[i])):
            if names[i][j].isupper():
                init = init + names[i][j]
        initial.append(init)
    return initial



if __name__ == '__main__':
    print("rectangle perimeter:", get_rectangle_perimeter(5,10)," Should be 30")

    # These are commented out until you properly define the functions above!
    # print("box volume/area:", get_box_volume_and_area(5,10,10),
    #       " Should be (500,400)") # Be sure to check when width != height
    # print("coloumb's force:",
    #       get_coulomb_force(1.60217662E-19,1.60217662E-19,1E-10)," Should be ~2.3069E-08")

    sample_names = ["Dwight Schrute", "Michael Scott", "Pam Beesly",
                    "Jim Halpert", "Angela Noelle Martin"]

    last_names = get_last_names(sample_names)
    print("Actual:  ", last_names)
    print("Expected:", ["Schrute", "Scott", "Beesly", "Halpert", "Martin"])

    initials = get_initials(sample_names)
    print("Actual:  ", initials)
    print("Expected:", ["DS", "MS", "PB", "JH", "ANM"])