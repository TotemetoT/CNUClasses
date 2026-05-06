"""
We will demo so debugging techniques, and highlight some issues
with style, and testing.

Please follow along, commit as I do, and don't rush ahead if you
see the errors of my ways as we plan to demonstrate debugging.

@author Ryan Schatzberg
@version 1/26/2025
"""

def int_calc(x):
    """

    Warning - this method was written by an under caffeinated 150 student

    Calculate an integer value as follows:
    Given integer value as input,
    calculate the product of all values from 1 up to AND including the value.

    If the input value is odd, then add 100,000 to calculated product;
    if input value is even, then add 1,000 to the calculated product.
    So if value is 1, then output is 100,001
    if value is 2, then output is 1,002
    if value is 4, then value is 1,024  (4*3*2*1 + 1000)

    @param x - integer input
    @return integer value

    """

    ## CORRECT AS WE GO IN CLASS TO PRACTICE DEBUGGING
    ## Do NOT rush ahead and fix because you see the errors!

    # x = 3
    prod = 0
    for i in range(x):
        prod = i + 1
        if prod % 2 == 0:
            # Even add 1000
            prod += 1000
        else:
            prod += 100000
    return prod

if __name__ == '__main__':

    print("int_calc(1)=", int_calc(1))
    print("int_calc(2)=", int_calc(2))
    print("int_calc(4)=", int_calc(4))
