import unittest
import copy
from src import grocery_store



class TestStock(unittest.TestCase):
    """
        Test Class for grocery_store.py stock method

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

        self.assertTrue(type(self._stock) == dict, msg='stock must return valid dictionary, not None!')


    def test_has_some_items(self):
        self.assertIsNotNone(self._stock, msg='stock must return valid dictionary, not None!')
        self.assertTrue(type(self._stock) == dict, msg='stock must return valid dictionary, not None!')
        stocked = False
        for item, price in self._inventory:
            if item in self._stock:
                stocked = True

        if not stocked:
            self.fail(msg="Stock dictionary does not contain any of required items!")

    def test_has_all_items(self):
        self.assertIsNotNone(self._stock, msg='stock must return valid dictionary, not None!')
        self.assertTrue(type(self._stock) == dict, msg='stock must return valid dictionary, not None!')
        stocked = True
        for item, price in self._inventory:
            if item not in self._stock:
                self.fail(msg="Stock dictionary does not contain all of required items! ("+item+" is missing)")



    def test_has_all_prices(self):
        self.assertIsNotNone(self._stock, msg='stock must return valid dictionary, not None!')
        self.assertTrue(type(self._stock) == dict, msg='stock must return valid dictionary, not None!')
        stocked = True
        for item, price in self._inventory:
            if item not in self._stock:
                self.fail(msg="Stock dictionary does not contain all of required items! ("+item+" is missing)")

            cost = self._stock[item]
            self.assertAlmostEqual(price, cost, msg=" Item "+item+" cost="+str(cost)+" is not "+str(price))


    def test_has_only_proper_stock(self):
        self.assertIsNotNone(self._stock, msg='stock must return valid dictionary, not None!')
        self.assertTrue(type(self._stock) == dict, msg='stock must return valid dictionary, not None!')
        stocked = True
        valid = [item for item, price in self._inventory]

        for item in self._stock:
            if item not in valid:
                self.fail(msg="Stock dictionary contains an invalid item! ("+item+" is not valid!)")

if __name__ == '__main__':
    unittest.main()
