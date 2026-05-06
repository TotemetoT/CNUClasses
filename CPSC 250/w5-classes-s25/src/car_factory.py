from src.car import Car


def create_car():
    """
    Create an instance of a car where the model year is > 1886 and the color is "Blue"

    return: an instance of a car as specified above
    """
    return Car("Volkswagen", "Golf GTI", 2018, "Blue")


def dealership_inventory():
    """
    Make a list of at least 5 cars and return that list

    return: a list with at least 5 cars
    """
    my_cars = []
    my_cars.append(Car("Ford", "Fusion", 2017, "Blue"))
    my_cars.append(Car("Honda", "Civic", 2001, "Blue"))
    my_cars.append(Car("Volkswagen", "Golf GTI", 2018, "Dark Iron Blue"))
    my_cars.append(Car("Honda", "Accord", 2019, "Silver"))
    my_cars.append(Car("Ford", "Bronco", 1996, "White and Red"))
    return my_cars



if __name__ == '__main__':
    # We will explore creating instances here
    car_1 = Car("Ford", "Fusion", 2017, "Blue")
    car_2 = Car("Honda", "Accord", 2019, "Silver")

    cars = [car_1, car_2]
    cars.append(Car("Nissan", "Altima", 2008, "Jade"))

    print("Cars:\n",cars)
    for car in cars:
        print(car)
