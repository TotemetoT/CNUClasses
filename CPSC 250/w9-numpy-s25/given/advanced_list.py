class AdvancedList(list):

    def __init__(self, *args):
        super().__init__(*args)

    def __add__(self, other):
        """
        Override the + operator. You should implement the following functionality:
        if the other object is a list and is of equal size to self.
            1. Add each element to each element of the list and return a new AdvancedList object.
            2. if other not of equal size to self raise a ValueError.
        if other is a number, add that number to each element of the list and return a new AdvancedList object.
        if other is not a number or list, raise a TypeError.

        Note: Do not modify the original list (self)!

        :param other: Can be an AdvancedList object, int, or float.
        :return: new AdvancedList object
        """
        if isinstance(other, AdvancedList):
            if len(self) == len(other):
                return AdvancedList([self[i] + other[i] for i in range(len(self))])
            else:
                raise ValueError("Lists must be of equal size")
        elif isinstance(other, (int, float)):
            return AdvancedList([self[i] + other for i in range(len(self))])
        else:
            raise TypeError("Only lists and numbers can be added")

    def __mul__(self, other):
        """
        Override the multiplication operator as in __add__ above.

        Notes:
            1. if other is a list and is not of equal size to self raise a ValueError.
            2. if other is not a number or list, raise a TypeError.

        :param other: Can be an AdvancedList object, int, or float.
        :return: new AdvancedList object
        """
        if isinstance(other, AdvancedList):
            if len(self) == len(other):
                return AdvancedList([self[i] * other[i] for i in range(len(self))])
            else:
                raise ValueError("Lists must be of equal size")
        elif isinstance(other, (int, float)):
            return AdvancedList([self[i] * other for i in range(len(self))])
        else:
            raise TypeError("Only lists and numbers can be multiplied")

    def __lt__(self, other):
        """
        Override the < operator to return a new AdvancedList of boolean values. Other can be a number (float or int) or an AdvancedList.
        For each element in the list you should compare the element to the other object and return an AdvancedList of booleans.

        Notes:
            1. if other is a list and is not of equal size to self raise a ValueError.
            2. if other is not a number or list, raise a TypeError.

        :param other: Can be an AdvancedList object, int, or float.
        :return: new AdvancedList object
        """
        if isinstance(other, AdvancedList):
            if len(self) == len(other):
                return AdvancedList([self[i] < other[i] for i in range(len(self))])
        elif isinstance(other, (int, float)):
            return AdvancedList([self[i] < other for i in range(len(self))])
        else:
            raise TypeError("Only numbers can be compared to lists")

    def __getitem__(self, index):
        """
        Override the getitem operator. You should implement the following functionality:
            1. If the index is a slice, return a new AdvancedList object after calling the getitem method of super().
            2. If the index is an int, return a number by calling the getitem method of super().
            3. If the index is a list, return a new AdvancedList object returning only the elements that correspond to the elements that are true in the list.

        Notes:
            1. If index is a list and has non-boolean elements, raise a TypeError.
            2. If index is not a list, int, or slice, raise a TypeError.

        :param index: Can be an AdvancedList object, int, or slice.
        :return: new AdvancedList object or number
        """
        if isinstance(index, slice):
            return AdvancedList(super().__getitem__(index))
        elif isinstance(index, int):
            return super().__getitem__(index)
        elif isinstance(index, list):
            if len(index) == len(self):
                # Check each element of other to see if it is boolean
                for i in index:
                    if not isinstance(i, bool):
                        raise TypeError("Index must be a boolean")
                return AdvancedList([self[i] for i, val in enumerate(index) if val])
        else:
            raise TypeError("Only lists, ints, and slices can be used as indices")


if __name__ == '__main__':
    list1 = AdvancedList([1, 2, 3])
    list2 = AdvancedList([4, 5, 6])

    print("type(list1)", type(list1))
    print("isinstance(list1, list):", isinstance(list1, list))

    print(list1)
    print(list2)

    list3 = list1 + list2
    print(list3)

    print("-" * 20, "Addition", "-" * 20)
    print(list1 + list2)
    print(list1 + 5)

    print("-" * 20, "Built-in list methods", "-" * 20)
    # All of the built-in list methods should work on AdvancedList objects
    list1.append(7)
    print(list1)
    print(list1[1:])

    print("-" * 20, "Multiplication", "-" * 20)
    # Test the __mul__ method
    list1 = AdvancedList([1, 2, 3])
    list2 = AdvancedList([4, 5, 6])

    print(list1 * list2)
    print(list1 * 2)

    #print(list1 * "hello")

    print("-" * 20, "Comparison", "-" * 20)
    # Test the __lt__ method
    list1 = AdvancedList([1, 2, 3, 4, 5])
    print(list1 < 3)

    print("-" * 20, "Boolean indexing", "-" * 20)
    print(list1[list1 < 3])
