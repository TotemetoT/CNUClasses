
"""
Define a function called cnu_captains that takes no arguments.

Create a string that has one line per integer from 1 to 100 inclusive
(Remember, range starts at 0, so be careful)

    if the number is divisible by 2 the line should be "CNU"
    if the number is divisible by 5 the line should be "CAPTAINS"
    if the number is divisible by 2 and 5 the line should be "CNUCAPTAINS"
    Otherwise, you should have the integer on the line.

    Use a newline character "\n" to separate each line in the string that you return.

NOTES:  1) You can add print statements to help you debug,
           but you must return a single string!

        2) Make sure that you have a newline character at the end of each line!


First few lines should look like this:
1
CNU
3
CNU
CAPTAINS
CNU
7
CNU
9
CNUCAPTAINS
11

:return: String that is described above
"""

# Fix this by defining function called cnu_captains
# Ideally, your function definition will be above the
# triple quoted lines above, which will then be indented to
# make them a `doc-string`.  You'll learn more about doc-strings later.
# Write the body of your code below the doc-string.
def cnu_captains():
    rtr = ""
    for i in range(100):
        if (i+1) % 2 == 0:
            if (i+1) % 5 == 0:
                rtr = rtr + ('CNUCAPTAINS')
            else:
                rtr = rtr + ('CNU')
        elif (i+1) % 5 == 0:
            rtr = rtr + ('CAPTAINS')
        else:
            rtr = rtr + str(i+1)
        rtr = rtr + '\n'
    return rtr

if __name__ == '__main__':
    print(cnu_captains())