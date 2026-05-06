"""
Define class to hold planet data
"""
import math
class Planet:

    # Define class attribute to hold gravitational constant G
    # Style schmile; G demands a capital G
    __G = 6.67408E-11  #m^3 kg^(-1) s^(-2)

    # initialize given name, radius, and mass
    # Define 3 private instance variables for
    #   string name
    #   float radius # average radius in meters
    #   float mass   # mass in kg
    def __init__(self, name, radius, mass):
        self.__name = name
        self.__radius = radius
        self.__mass = mass


    # Get string using __str__ that shows:
    #  name  radius=<value> m; mass=<value> kg; density=<value> kg/m^3; surface=<value> m^2; g=<value> m/s^2
    # e.g, "Earth radius = 6378100.0 m; mass = 5.97219e+24 kg; volume=1.0868324119376286e+21 m^3; density = 5495.042229512322 kg / m ^ 3;
    #       surface area = 511201962310544.9 m ^ 2; g = 9.798111466947612 m / s ^ 2"

    # Define the following methods
    # get_name()
    # get_radius()
    # get_mass()
    # get_volume() # m^3
    # get_density()  # mass/volume
    # get_surface_area() # m^2
    # get_gravity() # acceleration due to gravity at surface
    #  see http://www.softschools.com/formulas/physics/acceleration_due_to_gravity_formula/54/


    # Get string using __str__ that shows:
    #  name  radius=<value> m; mass=<value> kg; volume=1.0868324119376286e+21 m^3; density=<value> kg/m^3; surface=<value> m^2; g=<value> m/s^2
    def __str__(self):
        return "{} radius={:.3g} m; mass={:.3g} kg; volume={:.3g} m^3; density={:.3g} kg/m^3; surface area={:.3g} m^2; g={:.3g} m/s^2".format(
            self.__name, self.__radius, self.__mass, self.get_volume(),
            self.get_density(), self.get_surface_area(), self.get_gravity()
        )

    def get_name(self):
        return self.__name

    def get_radius(self):
        return self.__radius

    def get_mass(self):
        return self.__mass

    # get_volume() # m^3
    def get_volume(self):
        return (4./3)*math.pi*math.pow(self.__radius, 3)

    def get_density(self):  # mass/volume
        return self.__mass/self.get_volume()

    # get_surface_area() # m^2
    def get_surface_area(self):
        return 4*math.pi*math.pow(self.__radius, 2)

    def get_gravity(self): # acceleration due to gravity at surface
        return self.__G*self.__mass/math.pow(self.__radius, 2)



if __name__ == '__main__':
    print(Planet("Earth", 6.3781e6, 5.97219e24))
