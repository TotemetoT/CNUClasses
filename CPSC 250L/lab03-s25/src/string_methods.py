"""
We will practice with a few string methods
(yes, several of these should look familiar)

Many of these only require one line of code for base case,
plus protection from None references.

Make sure the string is valid before attempting.

Just return None if invald input.

There are a few style/naming issues to fix along the way.

E.g. I called the parameter 'input', which "shadows" a Python function.
Change that name!

Fix theses style/formatting issues first!
The tests assume the names are correct!

@author Ryan Schatzberg
@version 1/30/2025

"""
# pylint: disable-msg=C0103

def lower(string):
    """
    @param input either a valid string or None reference
    @return String with all lower case string or None
    """
    if string is None:
        return string
    return string.lower()


def upper(string):
    """
    @param input either a valid string or None reference
    @return String with all upper case string or None
    """
    if string is None:
        return string
    return str(string.upper())

def first_three(string):
    """
    Get the first three characters of a string
    @param input either a valid string of at least 3 characters or None reference
    @return String of three letters or None
    """
    if string is None:
        return string
    return string[:3]

def last_four(string):
    """
    Get the last for characters of a string
    @param input either a valid string of at least 4 characters or None reference
    @return String of four letters or None
    """
    if string is None:
        return string

    return string[-4:]

def every_other(string):
    """
    @param input either a valid string of at least 3 characters or None reference
    @return String containing every other letter of input or None
    """
    if string is None:
        return string

    return string[::2]

def format_price(price):
    """
    Formatted price with up to 3 whole digits.  For example,
    given 3.141  formatted string is "$  3.14"

    Hint:  Review your string formatting as discussed in CPSC 150/250 lecture
           and ZyBooks

    @param price - a valid number (float or int)
    @return String formatted with $ and .
    """
    if input is None:
        return input

    return f'${price:6.2f}'
