"""
All associated files are copyright 2022 by Christopher Newport University.

Posting publicly or sharing files is expressly forbidden.
"""

import unittest
from inspect import signature

from src.person import Person


class TestPerson(unittest.TestCase):

    def test_person(self):
        person = Person(first_name="Joe", middle_name="Bob", last_name="Fred")

        self.assertIsNotNone(person)
        self.assertTrue(isinstance(person,Person))
        self.assertEqual("Joe Bob Fred", str(person))

    def test_person_second(self):
        person = Person(first_name="Joe", middle_name="Bob", last_name="Fred", second_last_name="John")

        self.assertIsNotNone(person)
        self.assertEqual("Joe Bob Fred-John", str(person))

    def test_invalid_person_first(self):
        try:
            person = Person(first_name="", middle_name="Bob", last_name="Fred", second_last_name="John")

            self.fail("empty first name is invalid!")
        except Exception:
            # This is expected!
            pass

        try:
            person = Person(first_name=1, middle_name="Bob", last_name="Fred", second_last_name="John")

            self.fail("non-string first name is invalid!")
        except Exception:
            # This is expected!
            pass

        try:
            person = Person(first_name="1", middle_name="Bob", last_name="Fred", second_last_name="John")

            self.fail("string first name is invalid! Must have alphabetic characters.")
        except Exception:
            # This is expected!
            pass

    def test_invalid_person_last(self):
        try:
            person = Person(first_name="Joe", middle_name="Bob", last_name="", second_last_name="John")

            self.fail("empty last name is invalid!")
        except Exception:
            # This is expected!
            pass

        try:
            person = Person(first_name="Joe", middle_name="Bob", last_name=1, second_last_name="John")

            self.fail("non-string last name is invalid!")
        except Exception:
            # This is expected!
            pass

        try:
            person = Person(first_name="Joe", middle_name="Bob", last_name="\t", second_last_name="John")

            self.fail("string last name is invalid! Must have alphabetic characters")
        except Exception:
            # This is expected!
            pass

    def test_invalid_person_second_last(self):
        try:
            person = Person(first_name="Joe", middle_name="Bob", last_name="Fred", second_last_name=1)

            self.fail("non-string second last name is invalid!")
        except Exception:
            # This is expected!
            pass

    def test_person_equal(self):
        person1 = Person(first_name="Joe", middle_name="Bob", last_name="Fred", second_last_name="Squirrel")
        person2 = Person(first_name="Joe", middle_name="Bob", last_name="Fred", second_last_name="Squirrel")
        person3 = Person(first_name="Tina", middle_name="Bob", last_name="Fred", second_last_name="Squirrel")
        person4 = Person(first_name="Joe", middle_name="Sally", last_name="Fred", second_last_name="Squirrel")
        person5 = Person(first_name="Joe", middle_name="Bob", last_name="Barbara", second_last_name="Squirrel")

        self.assertTrue(person1 == person2, msg="These should be equal")
        self.assertFalse(person1 == person3, msg="These should be not equal")
        self.assertFalse(person1 == person4, msg="These should be not equal")
        self.assertFalse(person1 == person5, msg="These should be not equal")

    def test_person_lt(self):
        person1 = Person(first_name="Joe", middle_name="Bob", last_name="Fred", second_last_name="Squirrel")
        person2 = Person(first_name="Joe", middle_name="Bob", last_name="Fred", second_last_name="Squirrel")
        person3 = Person(first_name="Tina", middle_name="Bob", last_name="Fred", second_last_name="Squirrel")
        person4 = Person(first_name="Joe", middle_name="Sally", last_name="Fred", second_last_name="Squirrel")
        person5 = Person(first_name="Joe", middle_name="Bob", last_name="Barbara", second_last_name="Squirrel")

        self.assertFalse(person1 < person2, msg="These are equal")
        self.assertTrue(person1 < person3, msg="These should be less than")
        self.assertTrue(person1 < person4, msg="These should be less than")
        self.assertFalse(person1 < person5, msg="These should not be less than")


if __name__ == '__main__':
    unittest.main()
