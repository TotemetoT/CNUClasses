def add_numbers(x, y):
    if not (type(x) is float or type(x) is int):
        raise TypeError("x must be an int or a float")
    if not (type(y) is float or type(y) is int):
        raise TypeError("y must be an int or a float")

    return x + y


if __name__ == '__main__':
    try:
        add_numbers(5, "a")
    except Exception as e_with_another_name:
        print("handling the exception, e = ", e_with_another_name)
    finally:
        print("do some cleanup")
