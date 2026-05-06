import unittest
import os

from src import homework_file_io


class TestFileIO(unittest.TestCase):

    def setUp(self):
        self.file1 = os.path.join("data", "short_pattern.txt")
        self.file2 = os.path.join("data", "long_pattern.txt")
        self.file3 = os.path.join("data", "fourier_dataset.txt")
        self.file4 = os.path.join("data", "fellowship.txt")

    def test_text_attributes_lines_1(self):
        expected_lines = 100
        _, actual_lines = homework_file_io.text_attributes(self.file3)
        self.assertEqual(expected_lines, actual_lines,
                         msg=f"The number of lines is incorrect. Expected {expected_lines} but received {actual_lines}")
        expected_lines = 9
        _, actual_lines = homework_file_io.text_attributes(self.file4)
        self.assertEqual(expected_lines, actual_lines,
                         msg=f"The number of lines is incorrect. Expected {expected_lines} but received {actual_lines}")

    def test_text_attributes_chars_2(self):
        expected_chars = 7521
        actual_chars, _ = homework_file_io.text_attributes(self.file3)
        self.assertEqual(expected_chars, actual_chars,
                         msg=f"The number of characters is incorrect. Expected {expected_chars} but received {actual_chars}")
        expected_chars = 71
        actual_chars, _ = homework_file_io.text_attributes(self.file4)
        self.assertEqual(expected_chars, actual_chars,
                         msg=f"The number of characters is incorrect. Expected {expected_chars} but received {actual_chars}")

    def test_make_pattern_end(self):
        homework_file_io.write_file(self.file1, 5)
        expected = "*****"
        with open(self.file1) as file:
            actual = file.readlines()[-1].strip()
            self.assertEqual(expected, actual,
                             msg=f"The last line is incorrect. Expected {expected} but it is {actual})")

        homework_file_io.write_file(self.file1, 4)
        expected = "####"
        with open(self.file1) as file:
            actual = file.readlines()[-1].strip()
            self.assertEqual(expected, actual,
                             msg=f"The last line is incorrect. Expected {expected} but it is {actual})")

    def test_make_pattern_start(self):
        homework_file_io.write_file(self.file1, 5)
        expected = "*"
        with open(self.file1) as file:
            actual = file.readlines()[0].strip()
            self.assertEqual(expected, actual,
                             msg=f"The first line is incorrect. Expected {expected} but it is {actual})")

        homework_file_io.write_file(self.file1, 4)
        expected = "*"
        with open(self.file1) as file:
            actual = file.readlines()[0].strip()
            self.assertEqual(expected, actual,
                             msg=f"The first line is incorrect. Expected {expected} but it is {actual})")

    def test_correct_n_lines(self):
        homework_file_io.write_file(self.file1, 100)
        expected = 100
        with open(self.file1) as file:
            actual = len(file.readlines())
            self.assertEqual(expected, actual,
                             msg=f"The total number of lines is incorrect. Expected {expected} but it is {actual})")

    def test_append_nlines(self):
        with open(self.file1, "wt") as file:
            file.write("*****\n")
        expected = "#" * 6
        homework_file_io.append_file(self.file1, 6)
        with open(self.file1) as file:
            actual = file.readlines()[1].strip()
            self.assertEqual(expected, actual,
                             msg=f"Expected {expected} but it is {actual})")


if __name__ == '__main__':
    unittest.main()