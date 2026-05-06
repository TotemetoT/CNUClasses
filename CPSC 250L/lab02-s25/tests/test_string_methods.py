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

    def test_empty(self):
        self.assertEqual("",      string_methods.lower(""))
        self.assertEqual("",      string_methods.upper(""))

    def test_upper(self):
        self.assertEqual("LOWER", string_methods.upper("Lower"))
        self.assertEqual("UPPER", string_methods.upper("UPPER"))
        self.assertEqual("LOWER", string_methods.upper("loWeR"))


    def test_first_three(self):
        self.assertEqual("cat", string_methods.first_three("cat in the hat"), msg="return first 3 characters")
        self.assertEqual("The", string_methods.first_three("The quick brown fox"), msg="return first 3 characters")
        self.assertEqual("The", string_methods.first_three("The quick brown fox"), msg="return first 3 characters")


    def test_last_four(self):
        self.assertEqual(" hat", string_methods.last_four("cat in the hat"), msg="return last 4 characters")
        self.assertEqual("ouse", string_methods.last_four("The quick brown mouse"), msg="return last 4 characters")
        self.assertEqual("uffy", string_methods.last_four("Delci is very fluffy"), msg="return last 4 characters")

    def test_every_third(self):
        self.assertEqual("tnhh", string_methods.every_third("cat in the hat"), msg="return every third characters")
        self.assertEqual("eukrno", string_methods.every_third("The quick brown fox"), msg="return every third characters")
        self.assertEqual("l  rff", string_methods.every_third("Delci is very fluffy"), msg="return every third characters")

    def test_format_name_partial(self):
        self.assertTrue("Trible" in string_methods.format_name("Paul", "Trible"), msg="return formatted name")
        self.assertTrue("Paul" in string_methods.format_name("Paul", "Trible"), msg="return formatted name")

    def test_format_name_exact(self):
        self.assertEqual("Trible, Paul", string_methods.format_name("PAUL", "TriBle"), msg="return formatted name")

    def test_format_name_capitalized(self):
        self.assertTrue("Trible" in string_methods.format_name("paul", "trIble"), msg="return formatted name")
        self.assertTrue("Paul" in string_methods.format_name("pAul", "Trible"), msg="return formatted name")


if __name__ == '__main__':
    unittest.main()
