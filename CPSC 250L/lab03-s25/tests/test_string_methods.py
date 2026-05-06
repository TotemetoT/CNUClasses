import unittest

from src import string_methods


class TestStringMethods(unittest.TestCase):
    """
        Test Class for string_methods.py
    """

    def test_lower(self):
        self.assertEqual("lower", string_methods.lower("Lower"))
        self.assertEqual("upper", string_methods.lower("UPPER"))
        self.assertEqual("lower", string_methods.lower("LoWeR"))
        self.assertEqual("",      string_methods.lower(""))

    def test_upper(self):
        self.assertEqual("LOWER", string_methods.upper("Lower"))
        self.assertEqual("UPPER", string_methods.upper("UPPER"))
        self.assertEqual("LOWER", string_methods.upper("LoWeR"))
        self.assertEqual("",      string_methods.upper(""))

    def test_with_none(self):
        self.assertEqual(None, string_methods.lower(None), msg="protect against None reference")
        self.assertEqual(None, string_methods.upper(None), msg="protect against None reference")
        self.assertEqual(None, string_methods.first_three(None), msg="protect against None reference")


    def test_first_three(self):
        self.assertEqual("cat", string_methods.first_three("cat in the hat"), msg="return first 3 characters")
        self.assertEqual("The", string_methods.first_three("The quick brown fox"), msg="return first 3 characters")


    def test_last_four(self):
        self.assertEqual(" hat", string_methods.last_four("cat in the hat"), msg="return last 4 characters")
        self.assertEqual(" fox", string_methods.last_four("The quick brown fox"), msg="return last 4 characters")
        self.assertEqual("uffy", string_methods.last_four("Delci is very fluffy"), msg="return last 4 characters")

    def test_every_other(self):
        self.assertEqual("cti h a", string_methods.every_other("cat in the hat"), msg="return every other characters")
        self.assertEqual("Teqikbonfx", string_methods.every_other("The quick brown fox"), msg="return every other characters")
        self.assertEqual("Dlii eyfuf", string_methods.every_other("Delci is very fluffy"), msg="return every other characters")

    def test_format_price_exact(self):
        self.assertEqual("$  3.14", string_methods.format_price(3.1415927), msg="format price with $")
        self.assertEqual("$999.37", string_methods.format_price(999.370),   msg="format price with $")
        self.assertEqual("$ 50.00", string_methods.format_price(50),        msg="format price with $")

    def test_format_price_contains(self):
        self.assertTrue("3.14" in string_methods.format_price(3.1415927), msg="format price with $")
        self.assertTrue("999" in string_methods.format_price(999.370),   msg="format price with $")
        self.assertTrue("40" in string_methods.format_price(40),        msg="format price with $")

    def test_format_price_contains_dollar_sign(self):
        self.assertTrue("$" in string_methods.format_price(3.1415927), msg="format price with $")
        self.assertTrue("$" in string_methods.format_price(999.370),   msg="format price with $")
        self.assertTrue("$" in string_methods.format_price(40),        msg="format price with $")

    def test_with_none(self):
        self.assertEqual(None, string_methods.lower(None), msg="protect against None reference")
        self.assertEqual(None, string_methods.upper(None), msg="protect against None reference")
        self.assertEqual(None, string_methods.first_three(None), msg="protect against None reference")
        self.assertEqual(None, string_methods.last_four(None), msg="protect against None reference")
        self.assertEqual(None, string_methods.every_other(None), msg="protect against None reference")


if __name__ == '__main__':
    unittest.main()
