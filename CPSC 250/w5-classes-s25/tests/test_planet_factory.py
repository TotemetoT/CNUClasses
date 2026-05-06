import unittest
import os
from src.planet_factory import generate_planet_list
from src.planet import Planet


class TestPlanetFactory(unittest.TestCase):
    def setUp(self):
        self.file = os.path.join("data", "planets.txt")
        self.radii = [2439700.0,6052000.0,6378000.0,3393500.0,71400000.0,60330000.0,25559000.0,24764000.0,1150000.0]
        self.gravity =[3.7002621692408253,8.87406347019377,9.811232382874616,3.720752044862373,24.874169275553363,10.433668252974847,8.867953706957188,11.100690371736883,0.6510066691871456]
        self.mass = [3.3e+23,4.87e+24,5.98e+24,6.42e+23,1.9e+27,5.69e+26,8.68e+25,1.02e+26,1.29e+22]
        self.volume = [6.082720874248266e+19,9.285073957982011e+20,1.0867812925428892e+21,1.6369377712975358e+20,1.5246959427448477e+24,9.19789791721867e+23,6.993912316937748e+22,6.361374964008203e+22,6.370626302704502e+18]
        self.density = [5425.203734024424,5244.977069690924,5502.487060674172,3921.9572744730062,1246.1500990023676,618.6196075679633,1241.079328229339,1603.426941142476,2024.9186480336482]
        self.__delta = .001

    def test_return_list(self):
        planets = generate_planet_list(self.file)
        self.assertIsInstance(planets, list, msg="generate_planet_list must return a list")

    def test_return_planets(self):
        planets = generate_planet_list(self.file)
        self.assertIsInstance(planets, list, msg="generate_planet_list must return a list")
        self.assertIsInstance(planets[0], Planet, msg="generate_planet_list must return a list of Planet objects")

    def test_return_9_planets(self):
        planets = generate_planet_list(self.file)
        self.assertIsInstance(planets, list, msg="generate_planet_list must return a list")
        self.assertIsInstance(planets[0], Planet, msg="generate_planet_list must return a list of Planet objects")
        self.assertEqual(len(planets), 9, msg="generate_planet_list must return a list of 9 Planet objects")

    def test_correct_radius(self):
        planets = generate_planet_list(self.file)
        for i, planet in enumerate(planets):
            item = "radius"
            expected = self.radii[i]
            actual = planet.get_radius()
            self.assertAlmostEqual(actual, expected,delta=self.__delta, msg = f"Planet {planet.get_name()} {item} is {actual} when {expected} was expected")

    def test_correct_gravitational_force(self):
        planets = generate_planet_list(self.file)
        for i, planet in enumerate(planets):
            item = "gravitational force"
            expected = self.gravity[i]
            actual = planet.get_gravity()
            self.assertAlmostEqual(actual, expected,delta=self.__delta,
                                   msg=f"Planet {planet.get_name()} {item} is {actual} when {expected} was expected")

    def test_correct_mass(self):
        planets = generate_planet_list(self.file)
        for i, planet in enumerate(planets):
            item = "gravitational force"
            expected = self.gravity[i]
            actual = planet.get_gravity()
            self.assertAlmostEqual(actual, expected,delta=self.__delta,
                                   msg=f"Planet {planet.get_name()} {item} is {actual} when {expected} was expected")

    def test_correct_density(self):
        planets = generate_planet_list(self.file)
        for i, planet in enumerate(planets):
            item = "density"
            expected = self.density[i]
            actual = planet.get_density()
            self.assertAlmostEqual(actual, expected,delta=self.__delta,
                                   msg=f"Planet {planet.get_name()} {item} is {actual} when {expected} was expected")

    def test_correct_volume(self):
        planets = generate_planet_list(self.file)
        for i, planet in enumerate(planets):
            item = "volume"
            expected = self.volume[i]
            actual = planet.get_volume()
            self.assertAlmostEqual(actual, expected,delta=self.__delta,
                                   msg=f"Planet {planet.get_name()} {item} is {actual} when {expected} was expected")


if __name__ == '__main__':
    unittest.main()
