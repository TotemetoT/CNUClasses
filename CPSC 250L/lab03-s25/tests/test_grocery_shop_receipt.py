import unittest
import os
from src import grocery_store



class TestGroceryReceipt(unittest.TestCase):
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
        self.assertIsNotNone(self._stock, msg='stock must return valid dictionary, not None!')
        total, receipt, out_of_stock = grocery_store.shop(self._stock, [])
        self.assertFalse( out_of_stock, msg='Empty list should have empty out of stock list')
        self.assertEqual( 0.0, total, msg='Empty list should have zero total cost')
        self.assertTrue("otal" in receipt , msg='Valid receipt must include total')

    def test_shop_all_single_items(self):
        for item, price in self._inventory:
            total, receipt, out_of_stock = grocery_store.shop(self._stock, [ (item, 1)])
            self.assertTrue(item in receipt , msg='Valid item must be in receipt')
            self.assertTrue(type(receipt) is str, msg='Receipt must be a single string')
            self.assertEqual(price, total,    msg='Single item should have the total cost = price')
            self.assertTrue("total" in receipt.lower() , msg='Valid receipt must include total line')

    """
    Need to add more tests
    """
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

        self.assertTrue(type(receipt) is str, msg='Receipt must be a single string')
        self.assertTrue("total" in receipt.lower(), msg='Valid receipt must include total line')

        for index, stock in enumerate(self._inventory):
            item=stock[0]
            price=stock[1]
            self.assertTrue(item in receipt, msg='Valid item must be in receipt')

        lines = receipt.split('\n')
        self.assertTrue("total" in lines[-1].lower(),msg='Valid receipt must include total as last line')

    def test_shop_multiple_items_exact(self):

        # Make list
        grocery_list = []
        exp_total = 0.0
        for index, stock in enumerate(self._inventory):
            item = stock[0]
            price = stock[1]
            grocery_list.append((item, index + 1))
            exp_total += price * (index + 1)

        total, receipt, out_of_stock = grocery_store.shop(self._stock, grocery_list)

        receipt = receipt.strip()   # ignore final newline

        self.assertTrue(type(receipt) is str, msg='Receipt must be a single string')
        self.assertTrue("total" in receipt.lower(), msg='Valid receipt must include total line')

        for index, stock in enumerate(self._inventory):
            item = stock[0]
            price = stock[1]
            self.assertTrue(item in receipt, msg='Valid item must be in receipt')

        lines = receipt.split('\n')
        self.assertTrue("total" in lines[-1].lower(), msg='Valid receipt must include total as last line')
        fields = lines[-1].split("$")

        #print("total fields: ",fields)
        self.assertAlmostEqual(exp_total, float(fields[1]), places=2,
                               msg="Total cost {} is not {} in receipt ".format(exp_total, fields[1]))

        for index, stock in enumerate(self._inventory):
            item=stock[0]
            price=stock[1]
            cost = price*(index+1)

            fields = lines[index].split("$")
            #print("Item fields: ",fields)
            self.assertEqual(item.lower(), fields[0].strip().lower(),msg="{} is not {} in receipt".format(item,fields[0]))

            self.assertAlmostEqual(cost, float(fields[1]),places=2, msg="Cost {} is not {} in receipt for item {}".format(cost, fields[1],item))

    #def test_shop_multiple_items_exact2(self):
    #    self.test_shop_multiple_items_exact() # Just repeat the test to double weight exactness


if __name__ == '__main__':
    unittest.main()
