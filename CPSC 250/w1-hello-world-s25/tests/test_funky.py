import unittest
from src.funky import funky_factor

class TestFunky(unittest.TestCase):

    def test_negative_input(self):
        # Test with a negative input
        self.assertIsNone(funky_factor(-5), "Negative input should return None")

    def test_odd_input(self):
        # Test with an odd input
        self.assertEqual(funky_factor(3), 300, "Odd input should return 100 times the input")

    def test_even_input(self):
        # Test with an even input
        self.assertEqual(funky_factor(4), 24, "Even input should return the factorial of the input")

    def test_zero_input(self):
        # Test with zero as input
        self.assertEqual(funky_factor(0), 1, "Input of zero should return 1 (0! = 1)")

    def test_small_even_input(self):
        # Test with a small even number (e.g., 2)
        self.assertEqual(funky_factor(2), 2, "Even input of 2 should return the factorial 2! = 2")

    def test_large_odd_input(self):
        # Test with a larger odd input
        self.assertEqual(funky_factor(7), 700, "Odd input should return 100 times the input")

if __name__ == "__main__":
    unittest.main()
