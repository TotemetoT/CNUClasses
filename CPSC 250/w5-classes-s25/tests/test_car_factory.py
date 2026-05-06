import unittest
from src.car import Car
from src import car_factory


class TestCarFactory(unittest.TestCase):
    def test_returns_cars(self):
        data = car_factory.dealership_inventory()
        self.assertIsInstance(data, list, msg="must return a list")
        self.assertGreaterEqual(len(data), 5, msg="must return a list with at least 5 cars")
        if len(data) > 0:
            self.assertIsInstance(data[0], Car, msg="List must contain Car instances")

    def test_return_car(self):
        data = car_factory.create_car()
        self.assertIsInstance(data, Car, msg="must return an instance of Car")

    def test_return_car_blue(self):
        data = car_factory.create_car()
        color = data.color
        color = color.strip().capitalize()
        self.assertEquals(color, "Blue", msg="Car color must be Blue!")

    def test_return_car_year(self):
        data = car_factory.create_car()
        year = int(data.year)
        self.assertGreaterEqual(year, 1886, msg="The first car was made in 1886, please choose a more accurate model year")

if __name__ == '__main__':
    unittest.main()
