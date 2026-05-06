"""
We will practice with a few list methods

Many of these only require one line of code for base case,
plus protection from None

@author Ryan
@version Schatzberg

"""
def first_two(input_list):
    """
    Get the first two items in a list
    @param input a valid list with at least 2 items
    @return list of 2 items
    """
    return input_list[:2]

def exclude_first_and_last(input_list):
    """
        Get all of the list excluding the first and last item
        @param input  a valid list of at least 3 items
        @return list of items, excluding the first and last item
    """
    return input_list[1:-1]
def every_other(input_list):
    """
        Given ['A','b', 'c','d'] return ['A','c']
        @param input  a list of at least 3 items
        @return list containing every other item starting with first
    """
    return input_list[0::2]
if __name__ == '__main__':
    # Here is simple test - no need to modify below
    input0 = ['A', 'B', 'C', 'd', 'e', 'f']
    input1 = [1, 2, 3.14, 4, 5, 6]

    print("first_two result = ", first_two(input0))

    print("exclude_first_and_last result = ", exclude_first_and_last(input0))

    print("every_other result = ", every_other(input1))
