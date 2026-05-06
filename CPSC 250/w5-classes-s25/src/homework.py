"""
Homework - Class Practice

You should write a class as described in the file car.py



@author Ryan Schatzberg
 vvvvvvvvvvv you code below here vvvvvvvvvvvvvv
"""
# pylint: disable=C0103


from src.car import *
import csv


def create_car_instance():
    """
    Create and return an instance of a Car,
    the Car must be Blue in color
    (This is simple; don't overthink it.)

    :return: instance of Car
    """
    return Car(color_name="Blue")


def read_cars(full_path_name):
    """
    Read the data from csv file given full path file name (including directory)
    Return a list of Car instances.

    :param full_path_name: csv file
    :return: list of instances of the Car class
    """
    cars = []
    with open(full_path_name, 'r') as fin:
        reader = csv.reader(fin,delimiter=',',lineterminator='\n')
        for line in reader:
            make = line[1]
            model = line[2]
            year = line[0]  # This is the year from the CSV file
            color = line[3]
            if year.isdigit():
                year = int(year)
            cars.append(Car(make_name=make, model_name=model, model_year=year, color_name=color))

    return cars  # Now returns a list of Car instances


"""
^^^^^^^^^^^^^^^^^^ your code up here ^^^^^^^^^^^^^^^^^^^^
I'm giving you the below code as simple test.  Just leave as is
"""
if __name__ == '__main__':
    """
    Make sure you run this script from the project workspace, not the src1 folder
    """
    import os
    full_path_file_name = os.path.join("data", "small_cars.csv")
    print("full path=", full_path_file_name)
    data = read_cars(full_path_file_name)
    print(" Expect 10 ", len(data))
    for dat in data:
        if not isinstance(dat, Car):
            raise ValueError("Not a Car instance")
        print("   ", dat)
