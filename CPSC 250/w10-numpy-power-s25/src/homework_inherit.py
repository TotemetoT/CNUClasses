"""
Homework Inherit

This program is based on the grocery items.

You have Grocery, Dairy, and Bread as defined classes in the given folder.

Dairy is-a Grocery item
Bread is-a Grocery item

Write the methods as described below.

    For full credit, you need to write 1 additional class that inherits from
    any of the classes in given folder.

    You choose the name.

    The new class needs to be in its own file in the src folder


    Write the two methods below.
    NOTE: You can write the methods without your new class if that is causing issues.


@author <your name here>
 vvvvvvvvvvv you code below here vvvvvvvvvvvvvv
"""
# pylint: disable=C0103

# I'll give you these imports
from given.grocery import Grocery
from given.dairy import Dairy
from given.bread import Bread


def make_grocery_list():
    """
    Create a grocery list with :
        1 dairy, 2 bread, 1 your new class
        Make up your own prices

    :return: a list of four grocery items
    """
    pass  # @todo - fix this code



def total_bread(grocery_list):
    """
    Given list of grocery items, return
    the total cost of Bread items
    :param grocery_list:
    :return: total cost of Bread items
    """
    return 0.0  # @todo - fix this code


"""
^^^^^^^^^^^^^^^^^^ your code up here ^^^^^^^^^^^^^^^^^^^^
I'm giving you the below code as simple test.  Just leave as is
"""
if __name__ == "__main__":
    groceries = make_grocery_list()
    print("grocery list (as string): ", [str(item) for item in groceries])

    print("total cost of bread = ${:.2f}".format(total_bread(groceries)))
