import unittest
import math

from src import planet

from inspect import signature


class TestPlanet(unittest.TestCase):

    ## Need to write basic tests
    ## Is __init__ valid
    ## Are functions named correctly, with correct arguments

    def setUp(self):
        self.__delta = 0.000001

    def test_has_get_volume(self):
        method = 'get_volume'
        self.assertTrue(hasattr(planet.Planet, method),
                        msg='The {} method in the Planet class in {} does not exist'.format(method, "planet.py"))
        expected = 1
        class_method = getattr(planet.Planet, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='Planet.{} should take {} parameter(s) but it takes {}. Does it have "self"?'.format(
                             method, expected, actual)
                         )

    def test_has_get_density(self):
        method = 'get_density'
        self.assertTrue(hasattr(planet.Planet, method),
                        msg='The {} method in the Planet class in {} does not exist'.format(method, "planet.py"))
        expected = 1
        class_method = getattr(planet.Planet, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='Planet.{} should take {} parameter(s) but it takes {}. Does it have "self"?'.format(
                             method, expected, actual)
                         )

    def test_has_get_surface_area(self):
        method = 'get_surface_area'
        self.assertTrue(hasattr(planet.Planet, method),
                        msg='The {} method in the Planet class in {} does not exist'.format(method, "planet.py"))
        expected = 1
        class_method = getattr(planet.Planet, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='Planet.{} should take {} parameter(s) but it takes {}. Does it have "self"?'.format(
                             method, expected, actual)
                         )

    def test_has_get_gravity(self):
        method = 'get_gravity'
        self.assertTrue(hasattr(planet.Planet, method),
                        msg='The {} method in the Planet class in {} does not exist'.format(method, "planet.py"))
        expected = 1
        class_method = getattr(planet.Planet, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='Planet.{} should take {} parameter(s) but it takes {}. Does it have "self"?'.format(
                             method, expected, actual)
                         )

    def test_has_get_name(self):
        method = 'get_name'
        self.assertTrue(hasattr(planet.Planet, method),
                        msg='The {} method in the Planet class in {} does not exist'.format(method, "planet.py"))
        expected = 1
        class_method = getattr(planet.Planet, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='Planet.{} should take {} parameter(s) but it takes {}. Does it have "self"?'.format(
                             method, expected, actual)
                         )
    def test_has_get_radius(self):
        method = 'get_radius'
        self.assertTrue(hasattr(planet.Planet, method),
                        msg='The {} method in the Planet class in {} does not exist'.format(method, "planet.py"))
        expected = 1
        class_method = getattr(planet.Planet, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='Planet.{} should take {} parameter(s) but it takes {}. Does it have "self"?'.format(
                             method, expected, actual)
                         )

    def test_has_get_mass(self):
        method = 'get_mass'
        self.assertTrue(hasattr(planet.Planet, method),
                        msg='The {} method in the Planet class in {} does not exist'.format(method, "planet.py"))
        expected = 1
        class_method = getattr(planet.Planet, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='Planet.{} should take {} parameter(s) but it takes {}. Does it have "self"?'.format(
                             method, expected, actual)
                         )


    def test_get_volume(self):

        earth = planet.Planet("Earth",6.371e6, 5.97237e24)

        expected = 4/3*math.pi*math.pow(6.371e6,3)
        actual   = earth.get_volume()
        self.assertAlmostEqual(expected,actual,delta=self.__delta*expected,
                               msg='The {} has a volume of {} given radius={}'.format(earth.get_name(), expected, 6.3781e6))



    def test_get_surface_area(self):

        earth = planet.Planet("Earth",6.371e6, 5.97237e24)

        expected = 4*math.pi*math.pow(6.371e6,2)
        actual   = earth.get_surface_area()
        self.assertAlmostEqual(expected,actual,delta=self.__delta*expected,
                               msg='The {} has a surface area of {} given radius={}'.format(earth.get_name(), expected, 6.371e6))


    def test_get_gravity(self):

        earth = planet.Planet("Earth",6.371e6, 5.97237e24)

        expected = 9.8202581
        actual   = earth.get_gravity()
        self.assertAlmostEqual(expected,actual,delta=self.__delta*expected,
                               msg='The {} has a acceleration due to gravity of {} given radius={} and mass={}'.format(earth.get_name(), expected,6.371e6, 5.97237e24))

    def test_G_value(self):

        earth = planet.Planet("Earth",6.371e6, 5.97237e24)

        expected = 6.67408e-11 #m^3 kg^(-1) s^(-2) https://en.wikipedia.org/wiki/Gravitational_constant
        actual   = earth._Planet__G # Using the mangled form directly (see it's not private)
        self.assertAlmostEqual(expected,actual,delta=self.__delta*expected,
                               msg='The {} has a acceleration due to gravity of {} given radius={} and mass={}'.format(earth.get_name(), expected,6.371e6, 5.97237e24))


    def test_str(self):

        expected = "Earth radius = 6378100.0 m; mass = 5.97219e+24 kg; density = 5495.042229512322 kg / m ^ 3;" + \
                    " surface area = 511201962310544.9 m ^ 2; g = 9.798111466947612 m / s ^ 2"
        earth = planet.Planet("Earth",6.371e6, 5.97237e24)
        actual = earth.__str__()

        self.__string_contains_check(actual, "Earth")
        self.__string_contains_check(actual.lower(), "radius")
        self.__string_contains_check(actual.lower(), "mass")
        self.__string_contains_check(actual.lower(), "density")
        self.__string_contains_check(actual.lower(), "volume")
        self.__string_contains_check(actual.lower(), "g")
        self.__string_contains_check(actual.lower(), "surface")
        self.__string_contains_check(actual.lower(), "area")
        self.__string_contains_check(actual.lower(), "kg")
        self.__string_contains_check(actual.lower(), "m")
        self.__string_contains_check(actual.lower(), "^")
        self.__string_contains_check(actual.lower(), "2")
        self.__string_contains_check(actual.lower(), "3")
        self.__string_contains_check(actual.lower(), "5")
        self.__string_contains_check(actual.lower(), "9")
        self.__string_contains_check(actual.lower(), "e+24")

    def __string_contains_check(self, string, test):
        self.assertTrue(test in string, msg="expected to see {} in Planet string".format(test))


    def test_get_gravity_mars(self):

        earth = planet.Planet("Mars",3.3895e6, 6.4171e23)

        expected = 3.72785437
        actual   = earth.get_gravity()
        self.assertAlmostEqual(expected,actual,delta=self.__delta*expected,
                               msg='The {} has a acceleration due to gravity of {} given radius={} and mass={}'.format(earth.get_name(), expected,3.3895e6, 6.4171e23))

    def test_get_density_mars(self):

        earth = planet.Planet("Mars",3.3895e6, 6.4171e23)

        expected = 3934.08087
        actual   = earth.get_density()
        self.assertAlmostEqual(expected,actual,delta=self.__delta*expected,
                               msg='The planet {} has a average density of {} given radius={} and mass={}'.format(earth.get_name(), expected,3.3895e6, 6.4171e23))


if __name__ == '__main__':
    unittest.main()
