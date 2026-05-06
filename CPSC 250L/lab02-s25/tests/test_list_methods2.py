import unittest

from src import list_methods2


class TestListMethods2(unittest.TestCase):
    """
        Test Class for list_methods.py
    """

    def setUp(self):

        self.list1_5  = ['A', 'B', 'C', 'D', 'E']
        self.list2_5  = [ 1 ,  2,   3.14,   4,   5 ]
        self.list3_10 = [ 'A', 1,  'B',  2,  'C',  3.14, 'D',  4, 'E',  5]

    def test_modify_list_inplace(self):
        input = self.list1_5[:3]
        list_methods2.modify_list_inplace(input)
        self.assertEqual(['A', 'B', 'CPSC'], input, msg="modify list in place failed")

        input = self.list2_5[:3]
        list_methods2.modify_list_inplace(input)
        self.assertEqual([1, 2, 'CPSC'], input, msg="modify list in place failed")

    def test_modify_list_inplace2(self):
        input = self.list1_5[:3]
        list_methods2.modify_list_inplace(input)
        self.assertEqual(['A', 'B', 'CPSC'], input, msg="modify list in place failed")

        input = self.list2_5[:3]
        list_methods2.modify_list_inplace(input)
        self.assertEqual([1, 2, 'CPSC'], input, msg="modify list in place failed")

    def test_concatenate_lists(self):
        output = list_methods2.concatenate_lists(self.list1_5, self.list2_5)
        self.assertEqual(self.list1_5+self.list2_5, output, msg="Concatenate lists failed")

    def test_concatenate_lists2(self):
        output = list_methods2.concatenate_lists(self.list1_5, [])
        self.assertEqual(self.list1_5, output, msg="Concatenate list with empty failed")

    def test_concatenate_empty_lists(self):
        output = list_methods2.concatenate_lists([], [])
        self.assertEqual([], output, msg="Concatenate empty lists failed")

    def test_string_lists(self):
        output = list_methods2.strings_list(self.list2_5)
        self.assertEqual([str(val) for val in self.list2_5], output, msg="Conversion to string list failed")

    def test_string_lists2(self):
        output = list_methods2.strings_list(self.list2_5[1:3])
        self.assertEqual([str(val) for val in self.list2_5[1:3]], output, msg="Conversion to string list failed")

    def test_merge_lists_same_size(self):
        output = list_methods2.merge_lists_same_size(self.list1_5, self.list2_5)
        self.assertEqual(self.list3_10, output, msg="merge same size list failed")

    def test_merge_lists_same_size2(self):
        output = list_methods2.merge_lists_same_size(self.list1_5[1:3], self.list2_5[1:3])
        self.assertEqual(self.list3_10[2:6], output, msg="merge same size list failed")



if __name__ == '__main__':
    unittest.main()
