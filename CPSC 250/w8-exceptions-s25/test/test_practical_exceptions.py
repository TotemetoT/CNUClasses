import unittest
from inspect import signature
from src import practical_exceptions
import os
from given.person import Person
from given.cnu_person import CNUPerson
from given.student import Student


class TestPracticalExceptions(unittest.TestCase):

    def setUp(self):
        self.file1 = os.path.join("data", "people.txt")
        self.file2 = os.path.join("data", "survey_data.txt")
        self.sample_data = [1, 5, 7, "9", "eleven", 13, "fifteen"]
        self.expected = [1, 5, 7, 9, 13]
        self.file3 = os.path.join("data", "test_data.txt")

    def test_read_in_people_list(self):
        actual = practical_exceptions.read_in_people(self.file1)
        self.assertIsInstance(actual, list, msg="read_in_people must return a list")

    def test_read_in_people_instances_person(self):
        actual = practical_exceptions.read_in_people(self.file1)
        for person in actual:
            self.assertIsInstance(person, Person, msg="read_in_people must return a list of Person/CNUPerson/Student instances")

    def test_read_in_people_correct_n_instances(self):
        expected_person = 5
        expected_cnu_person = 3
        expected_student = 1
        tmp_per, tmp_stu, tmp_cnu = 0, 0, 0
        actual = practical_exceptions.read_in_people(self.file1)
        for person in actual:
            self.assertIsInstance(person, Person, msg="read_in_people must return a list of Person/CNUPerson/Student instances")
            if isinstance(person,Person):
                tmp_per += 1
            if isinstance(person, CNUPerson):
                tmp_cnu += 1
            if isinstance(person, Student):
                tmp_stu += 1

        self.assertEqual(expected_person, tmp_per, msg=f"Expected {expected_person} instances of Person")
        self.assertEqual(expected_cnu_person, tmp_cnu, msg=f"Expected {expected_cnu_person} instances of CNUPerson")
        self.assertEqual(expected_student, tmp_stu, msg=f"Expected {expected_student} instances of Student")

    def test_read_in_people_correct_n_instances_exception(self):
        expected_person = 4
        expected_cnu_person = 3
        expected_student = 1
        tmp_per, tmp_stu, tmp_cnu = 0, 0, 0
        actual = practical_exceptions.read_in_people(self.file2)
        for person in actual:
            self.assertIsInstance(person, Person, msg="read_in_people must return a list of Person/CNUPerson/Student instances")
            if isinstance(person,Person):
                tmp_per += 1
            if isinstance(person, CNUPerson):
                tmp_cnu += 1
            if isinstance(person, Student):
                tmp_stu += 1

        self.assertEqual(expected_person, tmp_per, msg=f"Expected {expected_person} instances of Person")
        self.assertEqual(expected_cnu_person, tmp_cnu, msg=f"Expected {expected_cnu_person} instances of CNUPerson")
        self.assertEqual(expected_student, tmp_stu, msg=f"Expected {expected_student} instances of Student")

    def test_convert_data_list(self):
        actual = practical_exceptions.convert_data(self.sample_data)
        self.assertIsInstance(actual, list, msg="convert_data must return a list")

    def test_convert_data_exact(self):
        actual = practical_exceptions.convert_data(self.sample_data)
        for i, val in enumerate(self.expected):
            self.assertEqual(actual[i], val, msg=f"Expected {self.expected[i]} instead received {actual[i]}")

    def test_safe_open_text_file(self):
        import io
        if os.path.exists(self.file3):
            os.remove(self.file3)
        try:
            file = practical_exceptions.safe_open_text(self.file3)
            print(type(file))
            self.assertIsInstance(file, io.TextIOWrapper, msg="safe_open_text must return file handle if the file does not exist! (class TextIOWrapper)")
            file.close()
        except Exception:
            self.assertTrue(False, msg="You should not raise an exception for a valid file that does not exist!")
        finally:
            if os.path.exists(self.file3):
                os.remove(self.file3)

    def test_safe_open_text_file_exception(self):
        import io
        with open(self.file3, "wt") as file:
            file.write("Test file!")
        try:
            file = practical_exceptions.safe_open_text(self.file3)
            self.assertIsNotNone(file, msg="safe_open_text must return file handle if the file does not exist! (class TextIOWrapper)")
        except Exception as e:
            self.assertIsInstance(e, FileExistsError, msg=f"You should raise a FileExistsError not a {type(e)}")
        finally:
            if os.path.exists(self.file3):
                os.remove(self.file3)


if __name__ == '__main__':
    unittest.main()
