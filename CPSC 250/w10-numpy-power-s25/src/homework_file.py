"""
Write code to create class instances based on data files.

20 points

    For 5 points, your code must handle "short_data.csv" file,
    for additional 5 points you code must work with "long_data.csv" file,

        If the price data is invalid, just replace with 0.0
        to flag it as bad data, but create the instance.

        If the type name (e.g. class name) is invalid,
        e.g. Not one of the given classes,
        then print a warning and skip the data.
        Do NOT create an instance in this case.

    If the bad data is causing you issues, or if short on time,
    then just go for the "short_data.csv" file

    For 5 points, the instances must be the correct type to match given name

    For 5 points, modify the main method to show the total cost of bread items

     I will NOT be strictly enforcing PyLint style though.
     However, I will adjust points based on unprofessional style choices
     or poorly written code even if functionally correct.

"""

# I'll give you these imports
import csv
import os

from given.grocery import Grocery
from given.dairy import Dairy
from given.bread import Bread
from src.homework_inherit import total_bread


def read_grocery_list(file_path):
    """
    @param: path to the data file
    @return: list of instances of Grocery items.

    """
    itemDict = {}
    breadList,dairyList = [],[]
    breadCost = []
    with open(file_path, 'rt') as fin:
        reader = csv.reader(fin, delimiter=',')
        for data in reader:
            if data[1][0].isnumeric():
                if data[0] in itemDict:
                    itemDict[data[0]].append(data[1])
                else:
                    itemDict[data[0]] = [data[1]]
    for item in itemDict:
        if item == "Bread":
            for price in itemDict[item]:
                breadList.append(Bread(price))
        elif item == "Dairy":
            for price in itemDict[item]:
                dairyList.append(Dairy(price))
    for bread in breadList:
        breadCost.append(Grocery.cost(bread))
    return breadCost

if __name__ == '__main__':

    # DATA_FILE_NAME = os.path.join("data", "short_data.csv")
    DATA_FILE_NAME = os.path.join("data", "long_data.csv")

    # read data from file and create instances of class as in program2
    items = read_grocery_list(DATA_FILE_NAME)
    total_bread_cost = 0.0
    for bread in items:
        total_bread_cost += float(bread)
    print(f"Total number of items in list = {len(items)}")
    print(f"Total cost of bread ${total_bread_cost:.2f}")

    # I got 10 items with bread cost of $39.63 when I ran my code with short_data.csv
    # I got 4742 items with bread cost of $16898.75 when I ran my code with long_data.csv

