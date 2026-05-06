import unittest

from src import homework
from src.car import Car

from csv import reader as c
from os.path import join as opj
import math

from inspect import signature
import random


class TestHomework(unittest.TestCase):

    def setUp(self):
        self.full_path = opj("data", "small_cars.csv")
        with open(self.full_path, "rt") as fin:
            reader = c(fin, delimiter=",", lineterminator="\n")
            self.data = []
            for line in reader:
                self.data.append((int(line[0]), line[1], line[2], line[3]))

    def test_read_file_list(self):
        data = homework.read_cars(self.full_path)
        self.assertIsInstance(data, list, msg="must return a list")
        self.assertEqual(len(data), len(self.data), msg="must return a list")

    def test_create_car_instance(self):
        p1 = homework.create_car_instance()
        self.assertIsNotNone(p1, msg="must create something")
        self.assertIsInstance(p1, Car, msg="must create instance of Car")

    def test_create_car_instance_blue(self):
        p1 = homework.create_car_instance()
        self.assertIsNotNone(p1, msg="must create something")
        self.assertIsInstance(p1, Car, msg="must create instance of Car")
        self.assertEqual(p1.color, "Blue", msg="must be Blue color")



    def test_read_cars_1(self):
        data_test = homework.read_cars(self.full_path)
        self.assertIsInstance(data_test, list, msg="must return a list")
        self.assertEqual(len(data_test), len(self.data), msg="must return a list")
        for i, dat in enumerate(data_test):
            self.assertTrue(isinstance(dat,Car))

    def test_read_cars_2(self):
        data_test = homework.read_cars(self.full_path)
        self.assertIsInstance(data_test, list, msg="must return a list")
        self.assertEqual(len(data_test), len(self.data), msg="must return a list")
        for i, dat in enumerate(data_test):
            # self.assertIsInstance(dat, Polar, msg="should be list of Polar instances")
            self.assertAlmostEqual(dat.year, self.data[i][0],
                                   msg="year={} at i={} not equal {}".format(dat.year, i, self.data[i][0]))
            self.assertEqual(dat.make, self.data[i][1],
                                   msg="make={} at i={} not equal {}".format(dat.make, i, self.data[i][1]))
            self.assertEqual(dat.model, self.data[i][2],
                                   msg="model={} at i={} not equal {}".format(dat.model, i, self.data[i][2]))
            self.assertEqual(dat.color, self.data[i][3],
                                   msg="color={} at i={} not equal {}".format(dat.color, i, self.data[i][3]))


if __name__ == '__main__':
    unittest.main()
