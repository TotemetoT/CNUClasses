import unittest
from src.homework import Homework


class TestHomework(unittest.TestCase):
    def setUp(self):
        self.__delta = 0.000001
        self.exp = [1 ,2 ,5 ,13 ,34 ,89 ,233]
        self.expc = [1 ,1 ,3 ,5 ,9 ,15 ,25]

        self.exp2 = [1 ,2 ,5 ,13 ,34 ,89 ,233 ,610 ,1597 ,4181 ,10946 ,28657 ,75025 ,196418 ,514229 ,1346269 ,3524578 ,9227465 ,24157817 ,63245986]
        self.exp2c = [1 ,1 ,3 ,5 ,9 ,15 ,25 ,41 ,67 ,109 ,177 ,287 ,465 ,753 ,1219 ,1973 ,3193 ,5167 ,8361 ,13529]

    def test_start_cases1(self):
        for i in range(2):
            p = Homework()
            v = p.recursive_sequence(i)
            self.assertEqual(v, self.exp[i], msg='base case failed')
            self.assertEqual(p.counter1, self.expc[i], msg='invalid recursion counter for base case (should be 1)')

    def test_n_2(self):
        n = 2
        p = Homework()
        v = p.recursive_sequence(n)
        self.assertEqual(v, self.exp[n], msg='f({:d}) failed'.format(n))
        # self.assertEqual(p.counter2, self.expc[n], msg='Check to make sure you do not have extra base cases')

    def test_recursive_sequence_exact1(self):

        for i in range(len(self.exp)):
            p = Homework()
            v = p.recursive_sequence(i)
            self.assertEqual(v, self.exp[i], msg='incorrect recursion_sequence value')
            self.assertEqual(p.counter1, self.expc[i], msg='invalid recursion counter, make sure you have the minimum number of base cases')

    def test_recursive_sequence_exact2(self):

        for i in range(len(self.exp2)):
            p = Homework()
            v = p.recursive_sequence(i)
            self.assertEqual(v, self.exp2[i], msg='incorrect recursion_sequence value')
            self.assertEqual(p.counter1, self.exp2c[i], msg='invalid recursion counter, make sure you have the minimum number of base cases')

    def test_n_neg(self):
        n = -3
        try:
            p = Homework()
            v = p.recursive_sequence(n)
            self.fail(msg=" raise IndexError for negative index")
        except IndexError as e:
            pass
        except Exception as e:
            self.fail(msg=" raise IndexError for negative index")

    def test_vowels_1(self):
        p = Homework()
        n_vowels = p.count_vowels("e")
        self.assertEqual(n_vowels, 1, msg='incorrect number of vowels')

    def test_vowels_2(self):
        p = Homework()
        n_vowels = p.count_vowels("pineapple")
        self.assertEqual(n_vowels, 4, msg='incorrect number of vowels')
        self.assertEqual(p.counter2, 10, msg='incorrect number recursive calls')

    def test_vowels_exact(self):
        p = Homework()
        n_vowels = p.count_vowels("pineapple")
        self.assertEqual(n_vowels, 4, msg='incorrect number of vowels')
        self.assertEqual(p.counter2, 10, msg='incorrect number recursive calls')
        n_vowels = p.count_vowels("pineapple")
        self.assertEqual(p.counter2, 20, msg='incorrect number recursive calls')




if __name__ == '__main__':
    unittest.main()
