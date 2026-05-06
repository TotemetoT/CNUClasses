import unittest

from src import homework
import os

class TestHomework(unittest.TestCase):

    def setUp(self):
        self.__universities_1 = ["Christopher Newport University", "Virginia Tech", "James Madison University", "Old Dominion University"]
        self.__universities_2 = ["George Washington University", "Ohio State University", "Florida State University"]

        self.initialize()

    def test_edit_university_names_is_list(self):
        self.assertEqual(type(homework.dictionary_from_names(self.__universities_1)), dict, msg="The function dictionary_from_names should return a dictionary")

    def test_edit_university_names_1(self):
        expected = self.__formatted_universities_1
        actual = homework.dictionary_from_names(self.__universities_1)
        self.assertDictEqual(expected, actual,
                               msg='\nThe dictionary_from_names function did not return formatted strings as expected:\nexpected = {} \nactual   = {}'.format(expected, actual))

    def test_university_lookup_2(self):
        expected = self.__formatted_universities_2
        actual = homework.dictionary_from_names(self.__universities_2)
        self.assertDictEqual(expected,actual,
                               msg='\nThe dictionary_from_names function did not return formatted strings as expected:\nexpected = {} \nactual   = {}'.format(expected, actual))

    def equality_test(self, input, expected):
        self.assertEqual(expected, homework.login_from_name(input), msg='output should be {}!'.format(expected))

        # Check to see if the basics are in order, but allow some errors (e.g. capitalization)

    def partial_equality_test(self, input, year, expected):
        usernames = homework.login_from_name(input)
        for i, names in enumerate(input):
            last, first = names.split(names)
            last = last.lower()
            first = first.lower()

            username_test = usernames[i].lower()
            self.assertTrue(first in username_test)
            self.assertTrue(last in username_test)
            self.assertTrue(str(year) in username_test)

    def test_username_one(self):
        input = ["Chris, Captain"]
        expected = ["cchri21"]
        self.equality_test(input, expected)

    def test_username_two(self):
        input = ["Chris, Captain", "Trible, Paul"]
        expected = ["cchri21", "ptrib21"]
        self.equality_test(input, expected)

    def test_username_three(self):
        # -----------------------------------------------------
        # Arrange
        # -----------------------------------------------------
        input = ["Chris, Captain", "Trible, Paul", "Curry, Steph"]
        expected = ["cchri21", "ptrib21", "scurr21"]
        self.equality_test(input, expected)

    def test_make_usernames_none(self):
        actual = homework.login_from_name(None)
        self.assertIsNone(actual, msg="If string list is None, then return None")

    def initialize(self):
        self.__formatted_universities_1 = {'CNU': 'Christopher Newport University', 'VT': 'Virginia Tech', 'JMU':'James Madison University', 'ODU':'Old Dominion University'}
        self.__formatted_universities_2 = {'GWU':'George Washington University', 'OSU':'Ohio State University', 'FSU':'Florida State University'}

if __name__ == '__main__':
    unittest.main()
