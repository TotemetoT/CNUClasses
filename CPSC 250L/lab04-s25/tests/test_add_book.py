import unittest
import copy
from src.add_book import add_book



class TestAddBook(unittest.TestCase):
    """
        Test Class for add_book.py method

    """

    def setUp(self):
        self._list = []
        self._book = add_book("title", "author", 2024, self._list)

    def test_book_valid(self):
        self.assertIsNotNone(self._book, msg='add_book must return valid dictionary, not None!')
        self.assertTrue(type(self._book) == dict, msg='add_book must return valid dictionary, not None!')


    def test_has_some_required_keys(self):
        self.assertIsNotNone(self._book, msg='add_book must return valid dictionary, not None!')
        self.assertTrue(type(self._book) == dict, msg='add_book must return valid dictionary, not None!')
        if "title" not in self._book:
            self.fail(msg="Book dictionary must contain title key !")
        if "author" not in self._book:
            self.fail(msg="Book dictionary must contain author key!")

    def test_has_all_required_keys(self):
        self.assertIsNotNone(self._book, msg='add_book must return valid dictionary, not None!')
        self.assertTrue(type(self._book) == dict, msg='add_book must return valid dictionary, not None!')
        if "title" not in self._book:
            self.fail(msg="Book dictionary must contain title key !")
        if "author" not in self._book:
            self.fail(msg="Book dictionary must contain author key!")
        if "year" not in self._book:
            self.fail(msg="Book dictionary must contain year key!")

    def test_has_all_required_data(self):
        self.assertIsNotNone(self._book, msg='add_book must return valid dictionary, not None!')
        self.assertTrue(type(self._book) == dict, msg='add_book must return valid dictionary, not None!')
        if "title" not in self._book:
            self.fail(msg="Book dictionary must contain title key !")
        if "author" not in self._book:
            self.fail(msg="Book dictionary must contain author key!")
        if "year" not in self._book:
            self.fail(msg="Book dictionary must contain year key!")

        self.assertTrue(isinstance(self._book["title"], str))
        self.assertTrue(isinstance(self._book["author"], str))
        self.assertTrue(isinstance(self._book["year"], int))

    def test_added_to_list(self):
        self.assertTrue(len(self._list) == 1, msg="must add book to list")

    def test_added_book_to_list(self):
        self.assertTrue(len(self._list) == 1, msg="must add book to list")
        book = self._list[0]
        self.assertIs(book, self._book, msg="add book instance to list")

    def test_handle_invalid_year(self):

        # First check valid handling
        self.assertTrue(len(self._list) == 1, msg="must add book to list")
        book = self._list[0]
        self.assertIs(book, self._book, msg="add book instance to list")

        book = add_book("title", "author", "not an int", "fiction")
        self.assertIsNone(book, "year not integer should return none")
        self.assertTrue(len(self._list) == 1, msg="must not add invalid book to list")

    def test_handle_invalid_title(self):

        # First check valid handling
        self.assertTrue(len(self._list) == 1, msg="must add book to list")
        book = self._list[0]
        self.assertIs(book, self._book, msg="add book instance to list")

        book = add_book(1984, "author", 1984, "fiction")
        self.assertIsNone(book, "title must be string type")
        self.assertTrue(len(self._list) == 1, msg="must not add invalid book to list")

        book = add_book("", "author", 1984, "fiction")
        self.assertIsNone(book, "title must be non-empty string type")
        self.assertTrue(len(self._list) == 1, msg="must not add invalid book to list")

    def test_handle_invalid_author(self):

        # First check valid handling
        self.assertTrue(len(self._list) == 1, msg="must add book to list")
        book = self._list[0]
        self.assertIs(book, self._book, msg="add book instance to list")

        book = add_book("title", 1984, 1984, "fiction")
        self.assertIsNone(book, "author must be string type")
        self.assertTrue(len(self._list) == 1, msg="must not add invalid book to list")

        book = add_book("1984", "", 1984, "fiction")
        self.assertIsNone(book, "author must be non-empty string type")
        self.assertTrue(len(self._list) == 1, msg="must not add invalid book to list")

if __name__ == '__main__':
    unittest.main()
