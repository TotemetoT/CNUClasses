# # import csv
# #
# # class Element():
# #     def __init__(self, element):
# #
# #         self.name = element[0]
# #         self.symbol = element[1]
# #         self.protons = int(element[2])
# #         self.electrons = int(element[3])
# #         self.neutrons = int(element[4])
# #         self.type = element[5]
# #         #Atomic Mass Things
# #         self.neutron_kg_per_mol = 1.008664915
# #         self.proton_kg_per_mol = 1.007276466812
# #         self.electron_kg_per_mol = 0.000548579909
# #         self.atomicMass = self.atomic_mass()
# #
# #     def atomic_mass(self):
# #         total_protons = self.protons * self.proton_kg_per_mol
# #         total_neutrons = self.neutrons * self.neutron_kg_per_mol
# #         total_electrons = self.electrons * self.electron_kg_per_mol
# #         return total_protons + total_neutrons + total_electrons
# #
# #     def __lt__(self, other):
# #         return self.atomicMass < other.atomicMass
# #
# #     def __str__(self):
# #         return f'{self.symbol}, {self.name}, {self.atomicMass:.5f}'
#
# class Element():
#     def __init__(self, element):
#         self.name = element[0]
#         self.symbol = element[1]
#         self.protons = int(element[2])
#         self.electrons = int(element[3])
#         self.neutrons = int(element[4])
#         self.type = element[5]
#
#         # Atomic Mass Constants (in g/mol, similar to amu)
#         self.neutron_amu = 1.008664915  # Neutron mass (g/mol)
#         self.proton_amu = 1.007276466812  # Proton mass (g/mol)
#         self.electron_amu = 0.000548658  # Electron mass (g/mol)
#
#         # Calculate atomic mass
#         self.atomicMass = self.atomic_mass()
#
#     def atomic_mass(self):
#         # Calculate the atomic mass based on protons, neutrons, and electrons
#         total_protons = self.protons * self.proton_amu
#         total_neutrons = self.neutrons * self.neutron_amu
#         total_electrons = self.electrons * self.electron_amu  # Include electron mass
#
#         return total_protons + total_neutrons + total_electrons
#
#     def __lt__(self, other):
#         return self.atomicMass < other.atomicMass
#
#     def __str__(self):
#         # Ensure atomic mass is rounded to 5 decimal places for consistent output
#         return f'{self.symbol}, {self.name}, {self.atomicMass}'

class Element:
    def __init__(self, element):
        self.name = element[0]
        self.symbol = element[1]
        self.protons = int(element[2])
        self.electrons = int(element[4])
        self.neutrons = int(element[3])
        self.type = element[5]

        # Atomic Mass Constants (in g/mol, similar to amu)
        self.neutron_amu = 1.007420893  # Neutron mass (g/mol)
        self.proton_amu = 1.007420170  # Proton mass (g/mol)
        self.electron_amu = 0.000548658  # Electron mass (g/mol) - corrected

        # Calculate atomic mass
        self.mass_atomic = self.atomic_mass()

    def atomic_mass(self):
        # Calculate the atomic mass based on protons, neutrons, and electrons
        total_protons = self.protons * self.proton_amu
        total_neutrons = self.neutrons * self.neutron_amu
        total_electrons = self.electrons * self.electron_amu
        return total_protons + total_neutrons + total_electrons  # Ensure precision

    def __lt__(self, other):
        return self.mass_atomic < other.mass_atomic

    def __str__(self):
        return f'{self.symbol}, {self.name}, {self.mass_atomic:.5f}'  # Ensure formatted output
