import unittest

from src import list_methods


class TestListMethods(unittest.TestCase):
    """
        Test Class for list_methods.py
    """

    def setUp(self):
        self.list1 = ['A', 'B', 'C', 'D', 'E', 'F']
        self.list2 = [1, 2, 3, 4, 5, 6, 7]
        self.list3 = ['a', 2, 'c', 4, 'e', 6, 'f']

    def test_first_two(self):
        self.assertEqual(['A', 'B'], list_methods.first_two(self.list1[:]), msg="return first 2 items in list")
        self.assertEqual([1, 2], list_methods.first_two(self.list2[:]), msg="return first 2 items in list ")
        self.assertEqual(['a', 2], list_methods.first_two(self.list3[:]), msg="return first 2 items in list ")

    def test_exclude_first_lasy(self):
        self.assertEqual(['B', 'C', 'D', 'E'], list_methods.exclude_first_and_last(self.list1[:]),
                         msg="return list excluding first and last element")
        self.assertEqual([2, 3, 4, 5, 6], list_methods.exclude_first_and_last(self.list2[:]),
                         msg="return list excluding first and last element")
        self.assertEqual([2, 'c', 4, 'e', 6], list_methods.exclude_first_and_last(self.list3[:]),
                         msg="return list excluding first and last element")

    def test_every_other(self):
        self.assertEqual(['A', 'C', 'E'], list_methods.every_other(self.list1[:]), msg="return every other item")
        self.assertEqual([1, 3, 5, 7], list_methods.every_other(self.list2[:]), msg="return every other item")
        self.assertEqual(['a', 'c', 'e', 'f'], list_methods.every_other(self.list3[:]), msg="return every other item")


if __name__ == '__main__':
    unittest.main()
