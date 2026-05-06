import unittest

from src import int_calc

class TestIntCalc(unittest.TestCase):
    """
        Test Class for int_calc.py
    """

    def test_int_calc_1(self):
        self.assertEqual(100001, int_calc.int_calc(1))


    # Do we have enough tests?


if __name__ == '__main__':
    unittest.main()
