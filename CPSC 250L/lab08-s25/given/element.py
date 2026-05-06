"""
Given class to hold element data

"""

class Element:

    # Private class attributes to hold CONSTANT values
    __NEUTRON_KG_PER_MOL = 1.007420893
    __PROTON_KG_PER_MOL = 1.007420170
    __ELECTRON_KG_PER_MOL = 0.000548658

    def __init__(self, symbol, name, np, nn, ne):
        self.__name = name
        self.__symbol = symbol
        self.__num_protons = np
        self.__num_neutrons = nn
        self.__num_electrons = ne

    def atomic_mass(self):

        return self.__num_protons*Element.__PROTON_KG_PER_MOL + \
               self.__num_electrons*Element.__ELECTRON_KG_PER_MOL + \
               self.__num_neutrons * Element.__NEUTRON_KG_PER_MOL

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def __str__(self):
        return f"{self.__symbol}, {self.__name}, {self.atomic_mass():.4f} kg/mol"

    def __lt__(self, other):
        return self.atomic_mass() < other.atomic_mass()
