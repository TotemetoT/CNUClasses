import unittest
import os
import numpy as np

from src import homework


class TestHomework(unittest.TestCase):
    def setUp(self):
        self.delta = 0.001
        self.file1 = os.path.join("data", "binary.dat")
        self.file2 = os.path.join("data", "binary2.dat")
        self.binary2 = [0, 1, 2, 3, 4, 5, 6, 7, 8], [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], [0.0, 1.0, 4.0, 9.0,
                                                                                                    16.0, 25.0, 36.0,
                                                                                                    49.0, 64.0], [0.0,
                                                                                                                  1.0,
                                                                                                                  8.0,
                                                                                                                  27.0,
                                                                                                                  64.0,
                                                                                                                  125.0,
                                                                                                                  216.0,
                                                                                                                  343.0,
                                                                                                                  512.0]
        self.binary1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0], [0.0,
                                                                                                                  1.0,
                                                                                                                  2.0,
                                                                                                                  3.0,
                                                                                                                  4.0,
                                                                                                                  5.0,
                                                                                                                  6.0,
                                                                                                                  7.0,
                                                                                                                  8.0,
                                                                                                                  9.0], [
                           0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0, 27.0]

        # Check to see if you are running from the right directory
        if os.getcwd().endswith("tests"):
            raise Exception("You must run this file from the project root directory")

    def test_chunk_size(self):
        fmt = ">iid"
        expected = 16
        _, actual = homework.read_attributes(self.file1, fmt)
        self.assertEqual(expected, actual, msg=f"Expected {expected} bytes for {fmt} format but it is {actual} bytes")
        fmt = ">id"
        expected = 12
        _, actual = homework.read_attributes(self.file2, fmt)
        self.assertEqual(expected, actual, msg=f"Expected {expected} bytes for {fmt} format but it is {actual} bytes")

    def test_file_size(self):
        expected = 252
        actual, _ = homework.read_attributes(self.file1, "i")
        self.assertEqual(expected, actual, msg=f"Expected {expected} bytes for {self.file1} but it is {actual} bytes")
        expected = 280
        actual, _ = homework.read_attributes(self.file2, "i")
        self.assertEqual(expected, actual, msg=f"Expected {expected} bytes for {self.file2} but it is {actual} bytes")

    def test_read_binary(self):
        expected = self.binary1[0]
        actual, _, _, _ = homework.read_binary_file(self.file2)
        np.testing.assert_almost_equal(actual, expected, decimal=5, err_msg="Column 1 of binary file incorrect",
                                       verbose=True)
        expected = self.binary1[1]
        _, actual, _, _ = homework.read_binary_file(self.file2)
        np.testing.assert_almost_equal(actual, expected, decimal=5, err_msg="Column 2 of binary file incorrect",
                                       verbose=True)
        expected = self.binary1[2]
        _, _, actual, _ = homework.read_binary_file(self.file2)
        np.testing.assert_almost_equal(actual, expected, decimal=5, err_msg="Column 3 of binary file incorrect",
                                       verbose=True)
        expected = self.binary1[3]
        _, _, _, actual = homework.read_binary_file(self.file2)
        np.testing.assert_almost_equal(actual, expected, decimal=5, err_msg="Column 4 of binary file incorrect",
                                       verbose=True)

        expected = self.binary2[0]
        actual, _, _, _ = homework.read_binary_file(self.file1)
        np.testing.assert_almost_equal(actual, expected, decimal=5, err_msg="Column 1 of binary file incorrect",
                                       verbose=True)
        expected = self.binary2[1]
        _, actual, _, _ = homework.read_binary_file(self.file1)
        np.testing.assert_almost_equal(actual, expected, decimal=5, err_msg="Column 2 of binary file incorrect",
                                       verbose=True)
        expected = self.binary2[2]
        _, _, actual, _ = homework.read_binary_file(self.file1)
        np.testing.assert_almost_equal(actual, expected, decimal=5, err_msg="Column 3 of binary file incorrect",
                                       verbose=True)
        expected = self.binary2[3]
        _, _, _, actual = homework.read_binary_file(self.file1)
        np.testing.assert_almost_equal(actual, expected, decimal=5, err_msg="Column 4 of binary file incorrect",
                                       verbose=True)


if __name__ == '__main__':
    unittest.main()
