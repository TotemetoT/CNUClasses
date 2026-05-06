
import unittest
import os
import numpy as np
from src.game import *
from src.read_characters import read_characters_from_file

class TestHomeworkNumpy(unittest.TestCase):

    def setUp(self):

        self.data = [
            ['Stranger','Human',14,10,10,14,16],
            ['Galadriel','Elf',12,18,15,17,17],
            ['Arondir','Elf',17,15,15,17,16],
            ['Durin','Dwarf',15,12,10,12,12],
            ['Nori','Harfoot',7,12,16,14,10],
            ['Sadoc','Harfoot',10,12,17,15,15],
            ['Elendil','Human',15,12,10,13,14],
            ['Bronwyn','Human',10,12,12,13,15]]

        self.sorted = [
            ['Arondir','Elf',17,15,15,17,16],
            ['Bronwyn','Human',10,12,12,13,15],
            ['Durin','Dwarf',15,12,10,12,12],
            ['Elendil','Human',15,12,10,13,14],
            ['Galadriel','Elf',12,18,15,17,17],
            ['Nori','Harfoot',7,12,16,14,10],
            ['Sadoc','Harfoot',10,12,17,15,15],
            ['Stranger','Human',14,10,10,14,16]
        ]

    def test_humanoids_loaded_count(self):

        file_path = os.path.join("data", "characters.csv")
        characters = read_characters_from_file(file_path)

        self.assertEqual(8, len(characters))

    def test_humanoids_loaded(self):

        file_path = os.path.join("data", "characters.csv")
        characters = read_characters_from_file(file_path)

        self.assertEqual(8, len(characters))
        for char in characters:
            self.assertTrue(isinstance(char, Humanoid), msg="Must be instance of Humanoid")


    def test_humanoids_loaded_class_types(self):

        file_path = os.path.join("data", "characters.csv")
        characters = read_characters_from_file(file_path)

        self.assertEqual(8, len(characters))
        for ndx, char in enumerate(characters):
            self.assertTrue(isinstance(char, Humanoid), msg="Must be instance of Humanoid")
            self.assertEqual(char.__class__.__name__, self.data[ndx][1], msg=f"Class instance must be of type {self.data[ndx][1]} not {char.__class__.__name__}")

    def test_humanoids_loaded_names(self):

        file_path = os.path.join("data", "characters.csv")
        characters = read_characters_from_file(file_path)

        self.assertEqual(8, len(characters))
        for ndx, char in enumerate(characters):
            self.assertTrue(isinstance(char, Humanoid), msg="Must be instance of Humanoid")
            self.assertEqual(char.name, self.data[ndx][0], msg=f"Instance name should be {self.data[ndx][0]} not {char.name}")

    def test_humanoids_loaded_agility(self):

        file_path = os.path.join("data", "characters.csv")
        characters = read_characters_from_file(file_path)

        self.assertEqual(8, len(characters))
        for ndx, char in enumerate(characters):
            self.assertTrue(isinstance(char, Humanoid), msg="Must be instance of Humanoid")
            self.assertEqual(char.name, self.data[ndx][0], msg=f"Instance agility should be {self.data[ndx][2]} not {char.agility}")

    def test_humanoids_loaded_wisdom(self):

        file_path = os.path.join("data", "characters.csv")
        characters = read_characters_from_file(file_path)

        self.assertEqual(8, len(characters))
        for ndx, char in enumerate(characters):
            self.assertTrue(isinstance(char, Humanoid), msg="Must be instance of Humanoid")
            self.assertEqual(char.name, self.data[ndx][0], msg=f"Instance wisdom should be {self.data[ndx][-1]} not {char.agility}")


    def test_humanoids_loaded_wisdom_sorted(self):

        file_path = os.path.join("data", "characters.csv")
        characters = read_characters_from_file(file_path)
        characters.sort() # Will need less than operator for Humanoid

        self.assertEqual(8, len(characters))
        for ndx, char in enumerate(characters):
            self.assertTrue(isinstance(char, Humanoid), msg="Must be instance of Humanoid")
            self.assertEqual(char.name, self.sorted[ndx][0], msg=f"Instance wisdom should be {self.data[ndx][-1]} not {char.agility}")

    def test_humanoids_loaded_names_sorted(self):

        file_path = os.path.join("data", "characters.csv")
        characters = read_characters_from_file(file_path)
        characters.sort()

        self.assertEqual(8, len(characters))
        for ndx, char in enumerate(characters):
            self.assertTrue(isinstance(char, Humanoid), msg="Must be instance of Humanoid")
            self.assertEqual(char.name, self.sorted[ndx][0], msg=f"Instance name should be {self.data[ndx][0]} not {char.name}")



if __name__ == '__main__':
    unittest.main()
