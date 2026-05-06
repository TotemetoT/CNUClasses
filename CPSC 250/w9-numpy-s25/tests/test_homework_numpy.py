
import unittest
import os
import numpy as np
from src import homework_numpy

class TestHomeworkNumpy(unittest.TestCase):

    def setUp(self):
        self.delta = 0.001
        self.data_x1 = np.array([0., 0.62831853, 1.25663706, 1.88495559, 2.51327412,
                                 3.14159265, 3.76991118, 4.39822972, 5.02654825, 5.65486678])
        self.data_y1 = np.array([0.00000000e+00, 5.87785252e-01, 9.51056516e-01, 9.51056516e-01,
                                 5.87785252e-01, 1.22464680e-16, -5.87785252e-01, -9.51056516e-01,
                                 -9.51056516e-01, -5.87785252e-01])
        self.data_y3 = np.array([0.00000000e+00, 1.38033235e+00, 1.04902073e+00, 4.61235473e-01,
                                 4.29275833e-01, 1.22464680e-16, -4.29275833e-01, -4.61235473e-01,
                                 -1.04902073e+00, -1.38033235e+00])
        self.data_y5 = np.array([0.00000000e+00, 1.52727866e+00, 8.11256596e-01, 6.98999602e-01,
                                 2.82329520e-01, 1.22464680e-16, -2.82329520e-01, -6.98999602e-01,
                                 -8.11256596e-01, -1.52727866e+00])
        self.var = 0
        self.test_x = np.array(
            [0., 0.11111111, 0.22222222, 0.33333333, 0.44444444, 0.55555556, 0.66666667, 0.77777778, 0.88888889, 1.])
        self.test_y = np.array(
            [2.34285480e-02, 8.74549035e-01, 2.33969285e-01, 4.48610489e-04, 6.16475597e-09, 6.07153145e-16,
             4.28564801e-25, 2.16805673e-36, 7.86069011e-50, 2.04261540e-65])
        self.test_y2 = np.array(
            [0.00215892, 0.01891025, 0.095689, 0.27972462, 0.47239293, 0.46087173, 0.2597531, 0.08457566, 0.01590868,
             0.00172873])

    def test_make_dataset_x(self):
        expected = self.data_x1
        actual, _ = homework_numpy.create_dataset(self.data_x1, 1)
        np.testing.assert_almost_equal(actual, expected, decimal=3,
                                       err_msg="The first value in the tuple is not the x values",
                                       verbose=True)


    def test_make_dataset_y(self):
        expected = self.data_y1
        _, actual = homework_numpy.create_dataset(self.data_x1, 1)
        np.testing.assert_almost_equal(actual, expected, decimal=3,
                                       err_msg="The calculated values where max_val=1 are incorrect",
                                       verbose=True)
        expected = self.data_y3
        _, actual = homework_numpy.create_dataset(self.data_x1, 3)
        np.testing.assert_almost_equal(actual, expected, decimal=3,
                                       err_msg="The calculated values where max_val=3 are incorrect",
                                       verbose=True)


    def test_make_dataset_y2(self):
        expected = self.data_y5
        _, actual = homework_numpy.create_dataset(self.data_x1, 5)
        np.testing.assert_almost_equal(actual, expected, decimal=3,
                                       err_msg="The calculated values where max_val=5 are incorrect",
                                       verbose=True)

    def test_type_and_tuple(self):
        tup = homework_numpy.generate_datasets(100, 1.0, .137, .05, .5, .495, .15)
        self.assertEqual(3, len(tup))
        x, y, y2 = tup
        self.assertEqual(type(x), np.ndarray)
        self.assertEqual(type(y), np.ndarray)
        self.assertEqual(type(y2), np.ndarray)

    def test_length(self):
        x, y, y2 = homework_numpy.generate_datasets(100, 1.0, .137, .05, .5, .495, .15)
        self.assertEqual(100, len(x))
        self.assertEqual(100, len(y))
        self.assertEqual(100, len(y2))
        x, y, y2 = homework_numpy.generate_datasets(10, 1.0, .137, .05, .5, .495, .15)
        self.assertEqual(10, len(x))
        self.assertEqual(10, len(y))
        self.assertEqual(10, len(y2))

    def test_exact_x(self):
        x, y, y2 = homework_numpy.generate_datasets(10, 1.0, .137, .05, .5, .495, .15)
        np.testing.assert_almost_equal(x, self.test_x, decimal=3,
                                       err_msg="The calculated values are incorrect",
                                       verbose=True)

    def test_exact_gaus1(self):
        x, y, y2 = homework_numpy.generate_datasets(10, 1.0, .137, .05, .5, .495, .15)
        np.testing.assert_almost_equal(y, self.test_y, decimal=3,
                                       err_msg="The calculated gaussian values are incorrect",
                                       verbose=True)

    def test_exact_gaus2(self):
        x, y, y2 = homework_numpy.generate_datasets(10, 1.0, .137, .05, .5, .495, .15)
        np.testing.assert_almost_equal(y2, self.test_y2, decimal=3,
                                       err_msg="The calculated gaussian values are incorrect",
                                       verbose=True)


if __name__ == '__main__':
    unittest.main()