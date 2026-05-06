"""
Practice with lists

@author Ryan Schatzberg
@version 2.3.2025
"""


def append_item_in_place(list0, item):
    """
    Add item to existing list in place
    @param list0 - list to add to
    @param item  - item to add (could be another list)
    @return None - Nothing to return here, we're modifying list0
    """
    list0.append(item.copy())
    pass


def append_item_to_new_list(list0, item):
    """
    Add item to existing list in place
    @param list0 - list to copy then add
    @param item  - item to add (could be another list)
    @return new list
    """
    new_list = list0.copy()
    new_list.append(item.copy())
    return new_list


def extend_item_in_place(list0, list1):
    """
    Extend list by another list to existing list in place
    @param list0 - list to add to
    @param list1 - item to add (could be another list)
    @return None - Nothing to return here, we're modifying list0
    """
    list0.extend(list1)
    pass


def extend_item_to_new_list(list0, list1):
    """
    Extend list by another list to existing list in place
    @param list0 - list to add to
    @param list1 - item to add (could be another list)
    @return new list
    """
    print(list0,list1)
    new_list = list0.copy()
    new_list.extend(list1.copy())
    return new_list

def get_every_other(list0):
    """
    Return a new list with every other item from first list
    @param list0
    @return new list
    """
    new_list = list0[::2]
    return new_list


if __name__ == '__main__':

    A = [1, 2, 3]
    B = ['A', 'B']
    c_list = A[:]
    print("A =", A)
    print("B =", B)
    print("C0=", c_list)
    append_item_in_place(c_list, B)  # Returns None!
    print("C1=", c_list, '   4th item is-a list!')

    d_list = append_item_to_new_list(A, B)
    print("D =", d_list, '   4th item is-a list!')
    print("A =", A, "  Should be no change!")
    print("B =", B, "  Should be no change!")

    e_list = A[:]
    extend_item_in_place(e_list, B)  # Returns None!
    print("E1=", e_list, '  longer list!')


    f_list = extend_item_to_new_list(A, B)
    print("F =", f_list, '  longer list!')
    print("A =", A, "  No change!")
    print("B =", B, "  No change!\n\n")


    # Setup to test every other
    g_list = A[:]
    g_list.extend(B)
    g_list.extend(g_list)
    h_list = get_every_other(g_list)
    print(" Given ", g_list)
    print(" Every other ", h_list)