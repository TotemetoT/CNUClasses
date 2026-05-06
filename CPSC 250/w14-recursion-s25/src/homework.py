"""
Homework - Recursion




@author Ryan Schatzberg
 vvvvvvvvvvv you code below here vvvvvvvvvvvvvv
"""
# pylint: disable=C0103


class Homework:

    def __init__(self):
        self.counter2 = 0
        self.counter1 = 0
        self.vowel = 0

    def recursive_sequence(self, n):
        """
        Calculate a sequence where the value is 3 times the previous value minus the second value prior in the sequence.

        For values less than 0 raise an IndexError

        n    0   1   2   3   4  ...
        f(n) 1   2   5  13  34

        Note: Do not use unnecessary/extra base cases as they will interfere with unit tests.

        :param n:
        :return: sequence value
        """
        # Do not modify this incrementing of the counter.
        self.counter1 += 1
        if n < 0:
            raise IndexError("Number cannot be less than 0")
        elif n == 0:
            return 1
        elif n == 1:
            return 2
        else:
            return 3 * self.recursive_sequence(n - 1) - self.recursive_sequence(n - 2)


    def count_vowels(self, a_string):
        """
        Given a string, count the number of vowels one character at a time, recursively.

        Note: Do not use unnecessary/extra base cases as they will interfere with unit tests.
            vowels include a,e,i,o,u

        :param a_string:
        :return: number of vowels
        """

        # Do not modify this incrementing of the counter.
        self.counter2 += 1
        vowel_list = ['a','e','i','o','u']
        if a_string == "": return self.vowel
        if a_string[0] in vowel_list:
            self.vowel += 1
        return self.count_vowels(a_string[1:])


if __name__ == '__main__':
    print("\n"+"*"*25)
    program1 = Homework()
    actual = program1.count_vowels("Hello World!")
    print("Expected:", 3)
    print("Actual:  ", actual)

    print("\n"+"*"*25)
    print("n    expected  actual")
    expected = [1, 2, 5, 13, 34]
    for i in range(20):
        print(program1.recursive_sequence(i),",",end = "")
    print()
    for i in range(20):
        program1 = Homework()
        program1.recursive_sequence(i)
        print(program1.counter1, ",", end ="")
    print()
    for i, val in enumerate(expected):
        print(f"{i}     {val:4d}     {program1.recursive_sequence(i):4d}")
