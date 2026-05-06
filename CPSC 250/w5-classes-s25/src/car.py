"""
Sample class file for demo

Create a Car class with the following constructor parameters in order:
    make, model, year, color

Later we will add a method to convert the instance data to a string

"""

class Car:

    def __init__(self,make_name="Mazda",model_name="3",model_year=2019,color_name="White"):

        self.make = make_name
        self.model = model_name
        self.year = model_year
        self.color = color_name

    def __str__(self):
        return "{} {} {} {}".format(self.year,self.make,self.model,self.color)
