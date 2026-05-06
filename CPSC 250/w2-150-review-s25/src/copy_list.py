"""
Illustrate copying of lists

@author Ryan Schatzberg
@version 1/25/2025
"""
import copy

def same_reference(old_list):
    """
    Returns the same reference
    :param old_list:
    :return: reference to the same object
    """
    return old_list


def slice_list(old_list):
    """
    Uses slicing to create a new list with same data
    :param old_list:
    :return: new_list with same data as old
    """
    new_list = old_list[0:]
    return new_list

def copy_list(old_list):
    """
    Uses copy.copy to create new list with same data
    :param old_list:
    :return: new_list with same data as old
    """
    new_list = old_list.copy()
    return new_list

def deepcopy_list(old_list):
    """
    Uses copy.deepcopy create a new list with same data
    :param old_list:
    :return: new_list with same data as old
    """
    new_list = copy.deepcopy(old_list)
    return new_list



def print_list(new_list, original_list=None):
    """
    Print list data, with list ID, and then all data in list with id of each item in list

    :param new_list: list we are printing out
    :param original_list: list we are comparing to
    :return:  None
    """

    print(new_list)
    print(" Prints ID and whether it is the same as the original list")
    if original_list is not None:
        print(" ID:", id(new_list), new_list is original_list)
        for item, value in enumerate(new_list):
            print("      {} : {} : {} : {}".format(item, value, id(value),
                  value is original_list[item]))
    else:
        print(" ID:", id(new_list))
        for item, value in enumerate(new_list):
            print("      {} : {} : {}".format(item, value, id(value)))


def demo_list(my_list, index=None, replacement=None, element_index=None, element_value=None):
    """
     Do the copy, print, then modify and print
    :param my_list: the original list we are working with
    :param index: optional index of item we want to modify
    :param replacement:  option to replace entire item
    :param element_index: option to modify element of item at index
    :param element_value: option of value to modify with
    :return: None
    """
    a_r = same_reference(my_list)
    a_sl = slice_list(my_list)
    a_c = copy_list(my_list)
    a_d = deepcopy_list(my_list)


    print(30*"v")
    print(30*"-")
    print("My original list:")
    print_list(my_list)
    print()
    print("Same reference:")
    print_list(a_r, my_list)

    print()
    print("Slice List:")
    print_list(a_sl, my_list)

    print()
    print("Copy List :")
    print_list(a_c, my_list)

    print()
    print("Deep Copy:")
    print_list(a_d, my_list)

    if index is not None and element_index is None:
        print(" Modifying item ", index)
        my_list[index] = replacement

    if element_index is not None:
        print(" Modifying element ", element_index, " of  item", index,
              " with ", element_value)
        my_list[index][element_index] = element_value


    if index is not None:
        print("My modified list:")
        print_list(my_list)

        print()
        print("Same reference:")
        print_list(a_r, my_list)

        print()
        print("Slice List:")
        print_list(a_sl, my_list)

        print()
        print("Copy List :")
        print_list(a_c, my_list)

        print()
        print("Deep Copy:")
        print_list(a_d, my_list)
    print(30*"^")
    print(30*"-")


if __name__ == "__main__":

    print(" Demo what it means to copy lists - and dangers of modifying copies")
    # List with just primitive types
    A = [1, 2, 3]  # Use UPPER_CASE since A is used as a constant here
    demo_list(A, 1, 4)

    # List with objects (lists) - list of lists
    #B = [[1], [2,], [3]]
    #demo_list(B, 1, [4])


    # List with objects (lists) - list of lists and change element in one list
    #C = [[1], [2,], [3]]
    #demo_list(C, index=2, element_index=0, element_value=42)
