"""
We will practice with a few list methods

Many of these only require one line of code for base case,
plus protection from None

@author Ryan
@version Schatzberg

"""


def modify_list_inplace(input_list):
    input_list[2] = "CPSC"
    # return input_list
"""
    Given a valid list of at least 3 items, replace the 3rd item with 'CPSC'

    @param input valid list of at least 3 items
    @return None
"""




def concatenate_lists(input_list0, input_list1):
    return input_list0 + input_list1
"""
    Given two lists, merge into a new list with input0 elements followed
    by input1 elements

    Example:   input0=['A', 'B', 'C'] , input1 = [1, 2, 3]

            return ['A', 'B', 'C', 1, 2, 3]


    Hint:  There is a trivial way to do this in one line of code.

    @param input0 valid list
    @param input1 valid list
    @return new list with combined elements
"""




def strings_list(input_list):
    for i in range(len(input_list)):
        input_list[i] = str(input_list[i])
    return input_list
"""
    Given input list of numbers, return a list of strings

    Example:  input= [1, 2, 3.14]

              return ['1', '2', '3.14']

    @param input valid list
    @return new list with string representations
"""



def merge_lists_same_size(input_list0, input_list1):
    ListI = []
    for i in range(len(input_list0)):
        ListI.append(input_list0[i])
        ListI.append(input_list1[i])
    return ListI
"""
    Given two lists of the same size, merge into a new list with alternating
    elements.

    Example:   input0=['A', 'B', 'C'] , input1 = [1, 2, 3]

            return ['A', 1, 'B', 2, 'C', 3]

    Hint: You'll need to use range( ) or enumerate( ) and use indices

    @param input0 valid list
    @param input1 valid list same size as input0
    @return new list with combined elements
"""




if __name__ == '__main__':
    # Here is simple test - no need to modify below
    input0 = ['A', 'B', 'C']
    input1 = [1, 2, 3.14]

    in_place = input0[:] # Create a copy to modify
    modify_list_inplace(in_place)
    print("modify_list_inplace result = ", in_place)

    print("concatenate_lists result: ", concatenate_lists(input0, input1))

    print("string_lists result: ", strings_list(input1))

    print("merge_lists_same_size result: ", merge_lists_same_size(input0, input1))
