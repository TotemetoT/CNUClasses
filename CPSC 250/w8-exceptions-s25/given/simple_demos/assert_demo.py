
def add_numbers(x, y):
    assert (type(x) is float or type(x) is int), "x must be an int or a float"
    assert (type(y) is float or type(y) is int), "y must be an int or a float"

    return x + y


z = add_numbers("a", 3.7)
