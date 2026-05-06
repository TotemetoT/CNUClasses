import unittest

import os

from src import small_data


class TestSmallDataMethods(unittest.TestCase):
    """
        Test Class for small_data.py
    """

    def setUp(self):
        self.small_data_file = os.path.join("data", "small_data.txt")
        self.small_data_file2 = os.path.join("data", "small_data2.txt")
        self.small_data_tmp_file = os.path.join("data", "small_data_tmp.txt")

    def write_data(self,fpath, c0, c1, c2):
        with open(fpath, 'wt') as file:
            data = []
            for i in range(len(c0)):
                data.append("{}|{}|{}\n".format(c0[i], c1[i], c2[i]))
            file.writelines(data)

    def read_data(self, fpath):
        with open(fpath, 'rt') as file:
            lines = file.readlines()
            c0 = []
            c1 = []
            c2 = []
            for line in lines:
                data = line.split("|")
                c0.append(int(data[0]))
                c1.append(int(data[1]))
                c2.append(int(data[2]))
            return c0, c1, c2
        return None

    def test_read_data_1(self):
        exp_c0,exp_c1,exp_c2 = self.read_data(self.small_data_file)
        act_c0,act_c1,act_c2 = small_data.read_data(self.small_data_file)

        self.assertEqual(exp_c0, act_c0, msg="Column 0 doesn't match ")
        self.assertEqual(exp_c1, act_c1, msg="Column 1 doesn't match ")
        self.assertEqual(exp_c2, act_c2, msg="Column 2 doesn't match ")

    def test_read_data_2(self):
        exp_c0,exp_c1,exp_c2 = self.read_data(self.small_data_file2)
        act_c0,act_c1,act_c2 = small_data.read_data(self.small_data_file2)

        self.assertEqual(exp_c0, act_c0, msg="Column 0 doesn't match ")
        self.assertEqual(exp_c1, act_c1, msg="Column 1 doesn't match ")
        self.assertEqual(exp_c2, act_c2, msg="Column 2 doesn't match ")


    def test_read_data_tmp(self):
        exp_c0 = [i for i in range(10)]
        exp_c1 = [2*i for i in exp_c0]
        exp_c2 = [2*i*i for i in exp_c0]
        self.write_data(self.small_data_tmp_file, exp_c0, exp_c1, exp_c2)

        # Test the metho
        act_c0,act_c1,act_c2 = small_data.read_data(self.small_data_tmp_file)

        self.assertEqual(exp_c0, act_c0, msg="Column 0 doesn't match ")
        self.assertEqual(exp_c1, act_c1, msg="Column 1 doesn't match ")
        self.assertEqual(exp_c2, act_c2, msg="Column 2 doesn't match ")

    def test_read_data_tmp2(self):
        exp_c0 = [i*i*i for i in range(10)]
        exp_c1 = [i for i in range(len(exp_c0))]
        exp_c2 = [5 * i * i for i in exp_c1]
        self.write_data(self.small_data_tmp_file, exp_c0, exp_c1, exp_c2)

        # Test the metho
        act_c0, act_c1, act_c2 = small_data.read_data(self.small_data_tmp_file)

        self.assertEqual(exp_c0, act_c0, msg="Column 0 doesn't match ")
        self.assertEqual(exp_c1, act_c1, msg="Column 1 doesn't match ")
        self.assertEqual(exp_c2, act_c2, msg="Column 2 doesn't match ")

    def test_append_data_tmp(self):
        exp_c0 = [i for i in range(10)]
        exp_c1 = [i*i for i in exp_c0]
        exp_c2 = [i * i * i for i in exp_c0]
        prev_val = exp_c0[-1]
        max_val = 32
        self.write_data(self.small_data_tmp_file, exp_c0, exp_c1, exp_c2)
        exp_c0 = [i for i in range(max_val+1)] # include the max value
        exp_c1 = [i*i for i in exp_c0]
        exp_c2 = [i * i * i for i in exp_c0]

        # Test the metho
        new_lines = small_data.append_data(self.small_data_tmp_file, max_val)
        self.assertEqual(max_val-prev_val, new_lines, msg="Should have written %d "%(max_val-prev_val))

        # Read the written file back into memory for testing
        act_c0,act_c1,act_c2 = self.read_data(self.small_data_tmp_file)

        self.assertEqual(exp_c0, act_c0, msg="Column 0 doesn't match ")
        self.assertEqual(exp_c1, act_c1, msg="Column 1 doesn't match ")
        self.assertEqual(exp_c2, act_c2, msg="Column 2 doesn't match ")

    def test_append_data_tmp2(self):
        exp_c0 = [i for i in range(3)]
        exp_c1 = [i*i for i in exp_c0]
        exp_c2 = [i * i * i for i in exp_c0]
        prev_val = exp_c0[-1]
        max_val = 50
        self.write_data(self.small_data_tmp_file, exp_c0, exp_c1, exp_c2)
        exp_c0 = [i for i in range(max_val+1)] # include the max value
        exp_c1 = [i*i for i in exp_c0]
        exp_c2 = [i * i * i for i in exp_c0]

        # Test the metho
        new_lines = small_data.append_data(self.small_data_tmp_file, max_val)
        self.assertEqual(max_val-prev_val, new_lines, msg="Should have written %d "%(max_val-prev_val))

        # Read the written file back into memory for testing
        act_c0,act_c1,act_c2 = self.read_data(self.small_data_tmp_file)

        self.assertEqual(exp_c0, act_c0, msg="Column 0 doesn't match ")
        self.assertEqual(exp_c1, act_c1, msg="Column 1 doesn't match ")
        self.assertEqual(exp_c2, act_c2, msg="Column 2 doesn't match ")


if __name__ == '__main__':
    unittest.main()
