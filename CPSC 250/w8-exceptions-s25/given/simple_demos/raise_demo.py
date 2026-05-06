def add_numbers(x, y):
    if not (type(x) is float or type(x) is int):
        raise TypeError("x must be an int or a float")
    if not (type(y) is float or type(y) is int):
        raise TypeError("y must be an int or a float")

    return x + y


z = add_numbers(1.2, "t")
