"""
Script to test for odd numbers

We may be able to improve

WARNING: This works in Python, but in Java you'll learn
some subtle differences

@author Ryan Schatzberg
@version 1/22/2025

"""

def is_odd(value):
    """
    Tests if the value is odd
    @return Boolean
    """
    if value % 2 == 0:
        return False
    else:
        return True


if __name__ == '__main__':

    for i in range(-3, 6):
        print(f"  is_odd({i:2d})= {is_odd(i)}")  # f-string style formatting
