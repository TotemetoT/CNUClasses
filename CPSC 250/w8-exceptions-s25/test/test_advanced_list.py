import unittest
from src.advanced_list import AdvancedList


class TestAdvancedList(unittest.TestCase):

    def setUp(self):
        self.__delta = 0.001

    def test_add_scalar(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        al = al + 1
        for i in range(n_elements):
            self.assertEqual(al[i], i+1)

    def test_add_two_lists(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        al2 = AdvancedList([i*2 for i in range(n_elements)])
        test_list = al + al2
        for i in range(n_elements):
            self.assertEqual(test_list[i], i+i*2)

    def test_add_raises_value_error(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        al2 = AdvancedList([i for i in range(n_elements*2)])
        with self.assertRaises(ValueError):
            al + al2

    def test_add_raises_type_error(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        with self.assertRaises(TypeError):
            al + "a"

    def test_mul_scalar(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        al2 = al * 2
        for i in range(n_elements):
            self.assertEqual(al[i]*2, al2[i])

    def test_mul_two_lists(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        al2 = AdvancedList([i*3 for i in range(n_elements)])
        test_list = al * al2
        for i in range(n_elements):
            self.assertEqual(test_list[i], i*i*3)

    def test_mul_raises_value_error(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        al2 = AdvancedList([i for i in range(n_elements*2)])
        with self.assertRaises(ValueError):
            al * al2

    def test_mul_raises_type_error(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        with self.assertRaises(TypeError):
            al * "a"

    def test_lt_scalar(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        al2 = al < 3
        for i in range(n_elements):
            self.assertEqual(al[i] < 3, al2[i])

    def test_lt_scalar_2(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        al2 = al < 6
        for i in range(n_elements):
            self.assertEqual(al[i] < 6, al2[i])

    def test_lt_raises_type_error(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        with self.assertRaises(TypeError):
            al < "a"

    def test_get_item_boolean_lt_3(self):
        n_elements = 10
        al = AdvancedList([i for i in range(n_elements)])
        al2 = al < 3
        for i in range(n_elements):
            self.assertEqual(al[al2], [i for i in range(n_elements) if i < 3])

    def test_get_item_index(self):
        n_elements = 20
        al = AdvancedList([i for i in range(n_elements)])
        al2 = al[5:10]
        for i in range(5, 10):
            self.assertEqual(al2[i-5], al[i])


if __name__ == '__main__':
    unittest.main()