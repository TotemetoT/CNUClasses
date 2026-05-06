import unittest
import copy
from src import copy_list


class TestCopyList(unittest.TestCase):
    """
        Test Class for copy_list.py

        No need to change this, just giving to your here so you don't have to write
        tests for webcat as required for odd.py and bad_code.py

    """

    def setUp(self):
        self._input = [[1], [2], [3]]
        self._expected = copy.deepcopy(self._input)

    def test_same_reference(self):
        a = [1, 2, 3]
        b = copy_list.same_reference(a)

        self.assertIs(a, b,
                        msg='same_reference should return id of the same object!')

    def test_slice_list(self):
        a = [1, 2, 3]
        b = copy_list.slice_list(a)
        self.assertIsNot(a, b,
                        msg='slice_list should return new object!')

        self.assertEqual(a, b,
                        msg='slice_list should return copy of list!')


    def test_copy_list(self):
        a = [1, 2, 3]
        b = copy_list.copy_list(a)
        self.assertIsNot(a, b,
                        msg='slice_list should return new object!')

        self.assertEqual(a, b,
                        msg='slice_list should return copy of list!')


    def test_deepcopy_list(self):
        a = [1, 2, 3]
        b = copy_list.copy_list(a)
        self.assertIsNot(a, b,
                        msg='slice_list should return new object!')

        self.assertEqual(a, b,
                        msg='slice_list should return copy of list!')


    def test_same_reference_modified(self):
        a = copy.deepcopy(self._input) # Get a local copy we can modify
        b = copy_list.same_reference(a)
        a[1] = [4]

        self.assertIs(a, b,
                        msg='same_reference should return id of the same object!')
        self.assertEqual(a, b,
                        msg='same_reference should return copy of list!')

    def test_slice_list_modified(self):
        a = copy.deepcopy(self._input) # Get a local copy we can modify
        b = copy_list.slice_list(a)
        a[1] = [4]  # Modify original list
        self.assertIsNot(a, b,
                        msg='slice_list should return new object!')

        self.assertEqual(self._expected, b,
                        msg='slice_list should return copy of list!')


    def test_copy_list_modified(self):
        a = copy.deepcopy(self._input) # Get a local copy we can modify
        b = copy_list.copy_list(a)
        a[1] = [4]  # Modify original list
        self.assertIsNot(a, b,
                        msg='copy_list should return new object!')

        self.assertEqual(self._expected, b,
                        msg='copy_list should return copy of list!')


    def test_deepcopy_list_modified(self):
        a = copy.deepcopy(self._input) # Get a local copy we can modify
        b = copy_list.copy_list(a)
        a[1] = [4]  # Modify original list
        self.assertIsNot(self._expected, b,
                        msg='deep_copy should return new object!')

        self.assertEqual(self._expected, b,
                        msg='deep_copy should return copy of list!')

    def test_copy_list_element_modified(self):
        a = copy.deepcopy(self._input) # Get a local copy we can modify
        b = copy_list.copy_list(a)
        a[1][0] = [42]  # Modify original list
        self.assertIsNot(a, b,
                        msg='copy_list should return new object!')

        self.assertEqual(a, b,
                        msg='copy_list should return copy of list!')


    def test_deepcopy_list_element_modified(self):
        a = copy.deepcopy(self._input) # Get a local copy we can modify
        b = copy_list.copy_list(a)
        a[1][0] = [42]  # Modify original list
        self.assertIsNot(a, b,
                        msg='deep_copy should return new object!')

        self.assertEqual(a, b,
                        msg='deep_copy should return copy of list, but can still modify elements!')


if __name__ == '__main__':
    unittest.main()
