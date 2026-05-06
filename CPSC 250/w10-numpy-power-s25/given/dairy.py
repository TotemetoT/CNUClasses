from given.grocery import Grocery


class Dairy(Grocery):

    def __init__(self, price):
        Grocery.__init__(self, price)
