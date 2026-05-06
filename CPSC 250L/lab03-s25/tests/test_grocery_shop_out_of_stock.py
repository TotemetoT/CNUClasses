import unittest
import copy
from src import grocery_store



class TestGroceryOutOfStock(unittest.TestCase):
    """
        Test Class for grocery_store.py

    """

    def setUp(self):
        self._inventory = [("pink lady apple", 2.99)
         , ("honeycrisp apple", 3.99)
         , ("eggs", 1.29)
         , ("bananas", 3.99)
         , ("milk", 4.59)
         , ("ground beef", 8.99)
         , ("cheerios", 3.69)]

        self._stock = grocery_store.stock()

    def test_stock_valid(self):
        self.assertIsNotNone(self._stock, msg='stock must return valid dictionary, not None!')
        self.assertTrue(type(self._stock) == dict, msg='stock must return valid dictionary, not !'+str(type(self._stock)))

    def test_shop_empty(self):
        total, receipt, out_of_stock = grocery_store.shop(self._stock, [])
        self.assertFalse(out_of_stock, msg='Empty list should have empty out of stock list')

    def test_shop_all_single_items(self):
        for item, price in self._inventory:
            total, receipt, out_of_stock = grocery_store.shop(self._stock, [ (item, 1)])
            self.assertFalse(out_of_stock, msg='Valid item in list has empty out_of_stock list')

    def test_shop_two_items(self):

        # Make list
        grocery_list = []
        exp_total = 0.0
        for item, price in self._inventory:
            grocery_list.append( (item, 2) )
            exp_total += price

        total, receipt, out_of_stock = grocery_store.shop(self._stock, grocery_list )

        self.assertFalse(out_of_stock, msg='Valid item in list has empty out_of_stock list')


    def test_shop_delci_food(self):

        # Make list
        grocery_list = [ ("delci food", 1) ]
        exp_total = 0.0
        for item, price in self._inventory:
            grocery_list.append( (item, 2) )
            exp_total += price

        total, receipt, out_of_stock = grocery_store.shop(self._stock, grocery_list )

        self.assertEqual(["delci food"], out_of_stock, msg='"delci food" is not valid item')

    def test_shop_delci_food_cnu_shirt(self):

        # Make list
        grocery_list = [ ("delci food", 1) ]
        exp_total = 0.0
        for item, price in self._inventory:
            grocery_list.append( (item, 2) )
            exp_total += price
        grocery_list.append(("cnu shirt", 1))
        total, receipt, out_of_stock = grocery_store.shop(self._stock, grocery_list )

        self.assertEqual(["delci food", "cnu shirt"], out_of_stock, msg='Neither "delci_food" or "cnu shirt" are valid')

        



if __name__ == '__main__':
    unittest.main()
