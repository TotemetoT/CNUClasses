import unittest
import copy
from src import list_methods


class TestListMethods(unittest.TestCase):
    """
        Test Class for list_methods.py

        No need to change this

    """

    def setUp(self):
        self._list0 = [1, 2, 3]
        self._list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self._list2 = [[1], [2], [3]]
        self._list3 = ['A', 'B', 'C']
        self._list4 = ['A', 'B', 'C', 'D']
        self._lists = [self._list0, self._list1, self._list2, self._list3, self._list4 ]


    def test_append_item_in_place(self):
        for given in self._lists:
            for item in self._lists:
                # Test with all combinations of given lists
                original = given[:]
                list_methods.append_item_in_place(original, item)


                self.assertEqual(len(given)+1, len(original),
                                msg='Append should only add 1 item to list')

                self.assertEqual(given, original[:-1],
                                msg='First items should remain the same')

                self.assertIs(type(item), type(original[-1]), msg='appended item has type')

                self.assertEqual(item, original[-1],
                                msg='Given item is inserted to end of original list')

    def test_append_item_to_new_list(self):
        for given in self._lists:
            for item in self._lists:
                # Test with all combinations of given lists
                original = given[:]
                new_list = list_methods.append_item_to_new_list(original, item)


                self.assertIsNot(original, new_list,
                                msg='New list should be created!')

                self.assertEqual(len(given)+1, len(new_list),
                                msg='Append should only add 1 item to list')

                self.assertEqual(len(given), len(original),
                                msg='New list should not change original list')

                self.assertEqual(given, original,
                                msg='Original list should remain the same')

                self.assertEqual(given, new_list[:-1],
                                msg='First items should remain the same')


                self.assertIs(type(item), type(new_list[-1]), msg='appended item has type')

                self.assertEqual(item, new_list[-1],
                                msg='Given item is inserted to end of original list')


    def test_extend_item_in_place(self):
        for given in self._lists:
            for item in self._lists:
                # Test with all combinations of given lists
                original = given[:]
                list_methods.extend_item_in_place(original, item)

                self.assertEqual(len(given)+len(item), len(original),
                                msg='Extend should create one list with both values')

                self.assertEqual(given, original[:len(given)],
                                msg='First items should remain the same as original list')

                self.assertEqual(item, original[len(given):],
                                msg='Last items should remain the same as extended item')


    def test_extend_item_to_new_list(self):
        for given in self._lists:
            for item in self._lists:
                # Test with all combinations of given lists
                original = given[:]
                new_list = list_methods.extend_item_to_new_list(original, item)


                self.assertEqual(len(given)+len(item), len(new_list),
                                msg='Extend should create one list with both values')
                self.assertEqual(len(given), len(original),
                                msg='Extend to new list should NOT modify original list!')

                self.assertEqual(given, original,
                                msg='Extend to new list should NOT modify original list!')

                self.assertEqual(given, new_list[:len(given)],
                                msg='First items should remain the same as original list')

                self.assertEqual(item, new_list[len(given):],
                                msg='Last items should remain the same as extended item')


if __name__ == '__main__':
    unittest.main()
