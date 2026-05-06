"""
We will practice with a few string string_methods

You may assume that the input is a valid string, therefore
the solutions only require one line of code at the return statement

If you take more than 1-line of code, review your string methods:
https://docs.python.org/3/library/stdtypes.html#str
https://docs.python.org/3/library/stdtypes.html#str.format


@author Ryan
@version Schatzberg

"""


def lower(input_str):
    return input_str.lower()
"""
    @param input_str a valid reference to a str instance
    @return String with every letter lowercase
"""


def upper(input_str):
    return input_str.upper()
"""
    @param input_str a valid reference to a str instance
    @return String with all upper case string
"""

def first_three(input_str):
    return input_str[:3]
"""
    Get the first three characters of a string of at least 3 characters
    @param input_str a valid reference to a str instance
    @return String of three letters or None
"""


def last_four(input_str):
    return input_str[-4:]
"""
Get the last four characters of a string
@param input_str a valid reference to a str instance of at least 4 characters
@return String of four letters
"""


def every_third(input_str):
    return input_str[2::3]
"""
    Given 'abcdefghijk'
    return 'cfi'
    @param input_str a valid reference to a str instance of at least 6 characters
    @return String containing every three letters of input starting at 3rd
"""


def format_name(first, last):
    return (f'{last.capitalize()}, {first.capitalize()}')
"""
    Given first and last names, return a single "Last, First" with proper
    capitalization

    Do this in one line of code!

    @param first - a valid str type first name with undetermined capitalization
    @param last - a valid str type first name with undetermined capitalization

    @return String formatted as "Last, First" with Initial-capital style
"""


if __name__ == '__main__':
    # Here is simple test - no need to modify below
    print(" lower('aBcDef') = ", lower('aBcDef'))
    print(" upper('aBcDef') = ", upper('aBcDef'))
    print(" first_three('abcdefghijk') = ", first_three('abcdefghijk'))
    print(" last_five('abcdefghijk') = ", last_four('abcdefghijk'))
    print(" every_third('abcdefghijk') = ", every_third('abcdefghijk'))
    print(" format_name:", format_name("paul", "trible"))
