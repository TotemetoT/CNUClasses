import unittest

from src import homework_review
from inspect import signature


class TestHomeworkReview(unittest.TestCase):

    def setUp(self):
        self.__delta = 0.001
        self.__short_names_1 = ["Dwight Schrute", "Jim Halpert", "Angela Noelle Martin", "Michael Scott", "Pam Beesly"]
        self.__short_names_2 = ["Dwight Schrute", "Jim Halpert", "Angela Martin", "Michael Scott", "Pam Beesly"]
        self.__names_1 = ["Dwight Schrute", "Kevin Malone", "Stanley Hudson", "Jim Halpert", "Angela Martin",
                          "Toby Flenderson", "Michael Scott", "Pam Beesly", "Jan Levinson", "Ryan Howard"]
        self.__names_2 = ["Dwight Kurt Schrute", "Kevin Jaye Malone", "Stanley James Hudson", "Jim Halpert",
                          "Angela Noelle Martin", "Toby Wyatt Flenderson", "Michael Gary Scott", "Pam Morgan Beesly",
                          "Jan Levinson", "Ryan Bailey Howard"]

        self.initialize()

    def test_get_rectangle_perimeter_returns_number(self):
        results = homework_review.get_rectangle_perimeter(1, 1)
        is_int_or_float = False
        if type(results) is float or type(results) is int:
            is_int_or_float = True
        self.assertTrue(is_int_or_float, msg="The function get_rectangle_perimeter should return a float or int")

    def test_get_rectangle_perimeter_1(self):
        expected = 8.0
        actual = homework_review.get_rectangle_perimeter(2, 2)
        self.assertAlmostEqual(expected,actual,delta=self.__delta,
                               msg='The get_rectangle_perimeter function calculated incorrect perimeter: expected={} actual={}'.format(expected, actual))

    def test_get_rectangle_perimeter_2(self):
        expected = 12.0
        actual = homework_review.get_rectangle_perimeter(2, 4)
        self.assertAlmostEqual(expected,actual,delta=self.__delta,
                               msg='The get_rectangle_perimeter function calculated incorrect perimeter: expected={} actual={}'.format(expected, actual))

    def test_get_rectangle_perimeter_3(self):
        expected = 10
        actual = homework_review.get_rectangle_perimeter(4, 1)
        self.assertAlmostEqual(expected, actual, delta=self.__delta,
                               msg='The get_rectangle_perimeter function calculated incorrect perimeter: expected={} actual={}'.format(
                                   expected, actual))

    def test_get_rectangle_perimeter_4(self):
        expected = 10
        actual = homework_review.get_rectangle_perimeter(1, 4)
        self.assertAlmostEqual(expected, actual, delta=self.__delta,
                               msg='The get_rectangle_perimeter function calculated incorrect perimeter: expected={} actual={}'.format(
                                   expected, actual))

    def test_get_box_volume_area_returns_tuple(self):
        results = homework_review.get_box_volume_and_area(1, 1, 1)
        is_tuple = False
        if type(results) is tuple:
            is_tuple = True
        self.assertTrue(is_tuple, msg="The function get_box_volume_area should return a tuple")

    def test_get_box_volume_area_parameters(self):
        function = 'get_box_volume_and_area'
        expected = 3
        class_function = getattr(homework_review, function)
        actual = len(signature(class_function).parameters)
        self.assertAlmostEqual(expected, actual,
                         msg='{} in {} should take {} parameter(s) but it takes {}.'.format(
                             function, "program1", expected, actual)
                         )

    def test_get_box_volume_area_1(self):
        expected = (500,400)
        actual = homework_review.get_box_volume_and_area(5, 10, 10)
        self.assertTrue(isinstance(actual, tuple), msg="The function get_box_volume_area should return a tuple")
        self.assertEqual(2, len(actual), msg="The function get_box_volume_area should return a tuple with two elements")
        self.assertAlmostEqual(expected[0], actual[0], delta=self.__delta,
                               msg='The get_box_volume_and_area function calculated incorrect volume : expected={} actual={}'.format(
                                   expected, actual))
        self.assertAlmostEqual(expected[1], actual[1], delta=self.__delta,
                               msg='The get_box_volume_and_area function calculated incorrect area : expected={} actual={}'.format(
                                   expected, actual))

    def test_get_box_volume_area_2(self):
        expected = (350,310)
        actual = homework_review.get_box_volume_and_area(5, 7, 10)
        self.assertTrue(isinstance(actual, tuple), msg="The function get_box_volume_area should return a tuple")
        self.assertEqual(2, len(actual), msg="The function get_box_volume_area should return a tuple with two elements")
        self.assertAlmostEqual(expected[0], actual[0], delta=self.__delta,
                               msg='The get_box_volume_and_area function calculated incorrect volume : expected={} actual={}'.format(
                                   expected, actual))
        self.assertAlmostEqual(expected[1], actual[1], delta=self.__delta,
                               msg='The get_box_volume_and_area function calculated incorrect area : expected={} actual={}'.format(
                                   expected, actual))

    def test_get_box_volume_area_3(self):
        expected = (125,150)
        actual = homework_review.get_box_volume_and_area(5, 5, 5)
        self.assertTrue(isinstance(actual, tuple), msg="The function get_box_volume_area should return a tuple")
        self.assertEqual(2, len(actual), msg="The function get_box_volume_area should return a tuple with two elements")
        self.assertAlmostEqual(expected[0], actual[0], delta=self.__delta,
                               msg='The get_box_volume_and_area function calculated incorrect volume : expected={} actual={}'.format(
                                   expected, actual))
        self.assertAlmostEqual(expected[1], actual[1], delta=self.__delta,
                               msg='The get_box_volume_and_area function calculated incorrect area : expected={} actual={}'.format(
                                   expected, actual))

    def test_get_coulomb_force_parameters(self):
        function = 'get_coulomb_force'
        expected = 3
        class_function = getattr(homework_review, function)
        actual = len(signature(class_function).parameters)
        self.assertAlmostEqual(expected, actual,
                         msg='{} in {} should take {} parameter(s) but it takes {}.'.format(
                             function, "program1", expected, actual)
                         )

    def test_coulomb_force_returns_number(self):
        results = homework_review.get_coulomb_force(1, 1, 1)
        is_float = False
        if type(results) is float:
            is_float = True
        self.assertTrue(is_float, msg="The function get_coulomb_force should return a float")

    def test_coulomb_force_k(self):
        expected = 8.987E9
        actual = homework_review.get_coulomb_force(1, 1, 1)
        self.assertAlmostEqual(expected, actual, delta=self.__delta,
                               msg='The get_coulomb_force function calculated incorrect force: expected={} actual={} Wrong constant!!! Do not change k'.format(
                                   expected, actual))

    def test_coulomb_force_1(self):
        expected = 8.987E9/100
        actual = homework_review.get_coulomb_force(1, 1, 10)
        self.assertAlmostEqual(expected, actual, delta=self.__delta,
                               msg='The get_coulomb_force function calculated incorrect force: expected={} actual={}'.format(
                                   expected, actual))

    def test_coulomb_force_2(self):
        expected = 2*8.987E9/100
        actual = homework_review.get_coulomb_force(1, 2, 10)
        self.assertAlmostEqual(expected, actual, delta=self.__delta,
                               msg='The get_coulomb_force function calculated incorrect force: expected={} actual={}'.format(
                                   expected, actual))

    def test_coulomb_force_3(self):
        expected = 4*8.987E9/100
        actual = homework_review.get_coulomb_force(2, 2, 10)
        self.assertAlmostEqual(expected, actual, delta=self.__delta,
                               msg='The get_coulomb_force function calculated incorrect force: expected={} actual={}'.format(
                                   expected, actual))

    def test_get_last_names_is_list(self):
        self.assertEqual(type(homework_review.get_last_names(self.__short_names_1)), list,
                         msg="The function get_last_names should return a list")

    def test_get_last_names_1(self):
        expected = self.__short_last_names_1
        actual = homework_review.get_last_names(self.__short_names_1)
        self.assertListEqual(expected, actual,
                             msg='\nThe get_last_names function did not return last names:\nexpected = {} \nactual   = {}'.format(
                                 expected, actual))

    def test_get_last_names_2(self):
        expected = self.__short_last_names_2
        actual = homework_review.get_last_names(self.__short_names_2)
        self.assertListEqual(expected, actual,
                             msg='\nThe get_last_names function did not return last names:\nexpected = {} \nactual   = {}'.format(
                                 expected, actual))

    def test_get_last_names_3(self):
        expected = self.__last_names_1
        actual = homework_review.get_last_names(self.__names_1)
        self.assertListEqual(expected, actual,
                             msg='\nThe get_last_names function did not return last names:\nexpected = {} \nactual   = {}'.format(
                                 expected, actual))

    def test_get_last_names_4(self):
        expected = self.__last_names_1
        actual = homework_review.get_last_names(self.__names_2)
        self.assertListEqual(expected, actual,
                             msg='\nThe get_last_names function did not return last names:\nexpected = {} \nactual   = {}'.format(
                                 expected, actual))

    def test_get_initials_is_list(self):
        self.assertEqual(type(homework_review.get_initials(self.__short_names_1)), list,
                         msg="The function get_initials should return a list")

    def test_get_initials_1(self):
        expected = self.__short_initials_1
        actual = homework_review.get_initials(self.__short_names_1)
        self.assertListEqual(expected, actual,
                             msg='\nThe get_initials function did not return initials:\nexpected = {} \nactual   = {}'.format(
                                 expected, actual))

    def test_get_initials_2(self):
        expected = self.__short_initials_2
        actual = homework_review.get_initials(self.__short_names_2)
        self.assertListEqual(expected, actual,
                             msg='\nThe get_initials function did not return initials:\nexpected = {} \nactual   = {}'.format(
                                 expected, actual))

    def test_get_initials_3(self):
        expected = self.__initials_1
        actual = homework_review.get_initials(self.__names_1)
        self.assertListEqual(expected, actual,
                             msg='\nThe get_initials function did not return initials:\nexpected = {} \nactual   = {}'.format(
                                 expected, actual))

    def test_get_initials_4(self):
        expected = self.__initials_2
        actual = homework_review.get_initials(self.__names_2)
        self.assertListEqual(expected, actual,
                             msg='\nThe get_initials function did not return initials:\nexpected = {} \nactual   = {}'.format(
                                 expected, actual))

    def initialize(self):
        self.__short_last_names_1 = ["Schrute", "Halpert", "Martin", "Scott", "Beesly"]
        self.__short_last_names_2 = ["Schrute", "Halpert", "Martin", "Scott", "Beesly"]
        self.__last_names_1 = ['Schrute', 'Malone', 'Hudson', 'Halpert', 'Martin', 'Flenderson', 'Scott', 'Beesly',
                               'Levinson', 'Howard']
        self.__short_initials_1 = ["DS", "JH", "ANM", "MS", "PB"]
        self.__short_initials_2 = ["DS", "JH", "AM", "MS", "PB"]
        self.__initials_1 = ['DS', 'KM', 'SH', 'JH', 'AM', 'TF', 'MS', 'PB', 'JL', 'RH']
        self.__initials_2 = ['DKS', 'KJM', 'SJH', 'JH', 'ANM', 'TWF', 'MGS', 'PMB', 'JL', 'RBH']


if __name__ == '__main__':
    unittest.main()
