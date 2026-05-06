import unittest
import copy
from src import grocery_store



class TestGroceryTotal(unittest.TestCase):
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
        self.assertTrue(type(self._stock) == dict,
                        msg='stock must return valid dictionary, not !' + str(type(self._stock)))

    def test_shop_empty(self):
        total, receipt, out_of_stock = grocery_store.shop(self._stock, [])
        self.assertAlmostEqual(0.0, total, msg='Empty list should have total cost of 0.0')

    def test_shop_eggs(self):
        total, receipt, out_of_stock = grocery_store.shop(self._stock, [ (self._inventory[2][0], 1)])
        self.assertAlmostEqual(self._inventory[2][1], total, msg='Single '+self._inventory[2][0]+' should have cost='+str(self._inventory[2][1]))

    def test_shop_all_single_items(self):
        for item, price in self._inventory:
            total, receipt, out_of_stock = grocery_store.shop(self._stock, [ (item, 1)])
            self.assertAlmostEqual(price, total, msg='Single '+str(price)+' should have cost='+str(price))

    def test_shop_single_items(self):

        # Make list
        grocery_list = []
        exp_total = 0.0
        for item, price in self._inventory:
            grocery_list.append( (item, 1) )
            exp_total += price

        total, receipt, out_of_stock = grocery_store.shop(self._stock, grocery_list )

        self.assertAlmostEqual(exp_total, total, msg='Total cost of all items is '+str(exp_total) +' not '+str(total))

    def test_shop_two_items(self):

        # Make list
        grocery_list = []
        exp_total = 0.0
        for item, price in self._inventory:
            grocery_list.append( (item, 2) )
            exp_total += price

        total, receipt, out_of_stock = grocery_store.shop(self._stock, grocery_list )

        self.assertAlmostEqual(2*exp_total, total, msg='Total cost of all items is '+str(exp_total) +' not '+str(total))

    def test_shop_multiple_items(self):

        # Make list
        grocery_list = []
        exp_total = 0.0
        for index, stock in enumerate(self._inventory):
            item=stock[0]
            price=stock[1]
            grocery_list.append( (item, index+1) )
            exp_total += price*(index+1)

        total, receipt, out_of_stock = grocery_store.shop(self._stock, grocery_list )

        self.assertAlmostEqual(exp_total, total, msg='Total cost of all items is '+str(exp_total) +' not '+str(total))

if __name__ == '__main__':
    unittest.main()
