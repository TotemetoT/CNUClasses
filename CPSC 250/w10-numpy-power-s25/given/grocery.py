class Grocery:

    def __init__(self, price):
        self.price = price

    def __str__(self):
        return "{},{:.2f}".format(self.__class__.__name__, self.price)

    def cost(self):
        return self.price

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.cost == other.cost

    def __lt__(self, other):
        # Sort by class name, then by cost

        if type(self) != type(other):
            return self.__class__.__name__ < other.__class__.name
        else:
            return self.cost() < other.cost()
