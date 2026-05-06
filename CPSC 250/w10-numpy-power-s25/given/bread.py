from given.grocery import Grocery


class Bread(Grocery):

    def __init__(self, price):
        Grocery.__init__(self, price)
