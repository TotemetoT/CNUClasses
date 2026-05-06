def max_list_recursive(lst):
    """
    recursive method to find maximum in a list
    :param: lst - list with > operator defined
    :return: max value
    """
    if len(lst) == 0: return None
    if len(lst) == 1: return lst[0]
    elif lst[0] < lst[1]:
        lst.pop(0)
    else:
        lst.pop(1)
    return max_list_recursive(lst)



def sum_list_recursive(lst):
    """
    recursive method to find sum of a list
    :param lst:
    :return: sum of list, 0 if empty
    """
    if len(lst) == 0: return 0
    elif len(lst) == 1: return lst[0]
    else:
        lst[0] = lst[0] + lst[1]
        lst.pop(1)
        return sum_list_recursive(lst)





def calc_seq(index):
    """
    Write a function `calc_seq` that returns the value of a sequence at a
    given index. The sequence is defined as the prior element minus the
    second and third prior elements .

    The 0th element returns 0, element 1 returns 1, and element 2 returns 2.
    The calculation for element 3 returns 1 (i.e. 2-1-0=1)

    The first seven elements are:

    element: 0 1 2 3  4  5  6 7 ...
    value  : 0 1 2 1 -2 -5 -4 3 ...

    :param index:
    :return: value:
    """
    if index < 0:
        raise IndexError("Index cannot be negative")
    if index == 0:
        return 0
    elif index == 1:
        return 1
    elif index == 2:
        return 2

    seq = [0, 1, 2]

    for i in range(3, index + 1):
        next_val = seq[i - 1] - seq[i - 2] - seq[i - 3]
        seq.append(next_val)

    return seq[index]

# print(max_list_recursive([1,2,3,4,5,6,7,0]))
# print(sum_list_recursive([1,2,3,4,5,6,7,0]))