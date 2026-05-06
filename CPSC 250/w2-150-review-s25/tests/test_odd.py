import unittest

# Import our module
from src import odd

class TestOdd(unittest.TestCase):
    """
        Test Class for odd.py

        This appears to work great, but needs some work.
    """

    def test_is_1_odd(self):
        self.assertTrue(odd.is_odd(1),
                        msg='The number 1 is odd!')

    def test_is_2_odd(self):
        self.assertFalse(odd.is_odd(2),
                        msg='The number 2 is NOT odd!')

    def test_is_111_odd(self):
        self.assertTrue(odd.is_odd(111),
                        msg='The number 111 is odd!')

    def test_is_42_odd(self):
        self.assertFalse(odd.is_odd(42),
                        msg='The number 42 is NOT odd!')

    def test_is_41_odd(self):
        # GIGO warning!!!!!!!!!! (fix this)
        self.assertTrue(odd.is_odd(41),
                         msg='The number 41 is odd!')


    # We will add some unit tests



if __name__ == '__main__':
    unittest.main()
