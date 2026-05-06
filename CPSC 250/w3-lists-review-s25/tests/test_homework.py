"""
Test for Week 3 homework - Do this individually

"""
import unittest
from src import homework

class TestHomework(unittest.TestCase):
    """
        Test Class for homework.py
    """

    def setUp(self):
        self._list0 = [1, 2, 3]
        self._list1 = ['A', 'B', 'C']
        self._list2 = [[1], [2], [3]]
        self._list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self._list4 = ['A', 'B', 'C', 'D']
        self._lists = [self._list0, self._list1, self._list2, self._list3, self._list4 ]

    def test_intermingle_same(self):

        expected = (len(self._list0) + len(self._list1))*[0]  # Create empty lists
        expected[::2] = self._list0[:]
        expected[1::2] = self._list1[:]

        mingled_list =  homework.intermingle_lists(self._list0, self._list1)

        self.assertEqual(len(expected), len(mingled_list), msg="Returned list is not expected length")
        self.assertEqual(expected, mingled_list, msg="Returned list does not have expected values")


    def test_intermingle_same_2(self):

        expected = (len(self._list2) + len(self._list1))*[None]  # Create empty lists
        expected[::2] = self._list2[:]
        expected[1::2] = self._list1[:]

        mingled_list =  homework.intermingle_lists(self._list2, self._list1)

        self.assertEqual(len(expected), len(mingled_list), msg="Returned list is not expected length")
        self.assertEqual(expected, mingled_list, msg="Returned list does not have expected values")


    def test_intermingle_different_first_short(self):

        # This solution code is specific to this problem, not the correct way to do
        expected = (len(self._list0) + len(self._list4))*[0]  # Create empty lists
        expected[0:2*len(self._list0):2] = self._list0[:]
        expected[1:2*len(self._list0):2] = self._list4[:len(self._list0)]
        expected[2*len(self._list0)::2] = self._list4[len(self._list0):]

        mingled_list =  homework.intermingle_lists(self._list0, self._list4)

        self.assertEqual(len(expected), len(mingled_list), msg="Returned list is not expected length")
        self.assertEqual(expected, mingled_list, msg="Returned list does not have expected values")

    def test_intermingle_first_empty(self):

        mingled_list =  homework.intermingle_lists([], self._list4[:])

        self.assertEqual(len(self._list4), len(mingled_list), msg="Returned list is not expected length")
        self.assertEqual(self._list4, mingled_list, msg="Returned list does not have expected values")

    def test_intermingle_second_empty(self):

        mingled_list = homework.intermingle_lists(self._list4[:], [])

        self.assertEqual(len(self._list4), len(mingled_list), msg="Returned list is not expected length")
        self.assertEqual(self._list4, mingled_list, msg="Returned list does not have expected values")

    def test_intermingle_first_none(self):

        mingled_list = homework.intermingle_lists(None, self._list4[:])

        self.assertEqual(len(self._list4), len(mingled_list), msg="Returned list is not expected length")
        self.assertEqual(self._list4, mingled_list, msg="Returned list does not have expected values")

    def test_intermingle_second_none(self):

        mingled_list = homework.intermingle_lists(self._list3[:], None)

        self.assertEqual(len(self._list3), len(mingled_list), msg="Returned list is not expected length")
        self.assertEqual(self._list3, mingled_list, msg="Returned list does not have expected values")

    def test_intermingle_both_none(self):

        mingled_list = homework.intermingle_lists(None, None)

        self.assertIsNone(mingled_list, msg="Returned list is None if both are None")

    def test_intermingle_different_second_short(self):

        # This solution code is specific to this problem, not the correct way to do
        expected = (len(self._list4) + len(self._list1))*[0]  # Create empty lists
        expected[:2*len(self._list1):2] = self._list4[:len(self._list1)]
        expected[1:2*len(self._list1):2] = self._list1[:len(self._list1)]
        expected[2*len(self._list1)::2] = self._list4[len(self._list1):]

        mingled_list =  homework.intermingle_lists(self._list4, self._list1)

        self.assertEqual(len(expected), len(mingled_list), msg="Returned list is not expected length")
        self.assertEqual(expected, mingled_list, msg="Returned list does not have expected values")

    def test_intermingle_mega_test(self):
        for given in self._lists:
            for item in self._lists:
                # Test with all combinations of given lists
                list0 = given[:]
                list1 = item[:]
                mingled_list = homework.intermingle_lists(list0, list1)

                #print("mega:")
                #print(list0)
                #print(list1)
                #print(mingled_list)

                self.assertEqual(len(given)+len(item), len(mingled_list), msg='Mingled is incorrect size')
                self.assertEqual(given, list0, msg='Mingling should NOT change original first list')
                self.assertEqual(item, list1, msg='Mingling should NOT change original second list')

                for i in range(len(given)):
                    if i < len(item):
                        self.assertEqual(given[i], mingled_list[0+2*i])
                    else:
                        self.assertEqual(given[i], mingled_list[len(item) + i], msg=f'mingled list is not correct for {i}th item in first list')
                for i in range(len(item)):
                    if i < len(given):
                        self.assertEqual(item[i], mingled_list[1+2*i])
                    else:
                        self.assertEqual(item[i], mingled_list[len(given) + i], msg=f'mingled list is not correct for {i}th item in second list')



if __name__ == '__main__':
    unittest.main()
