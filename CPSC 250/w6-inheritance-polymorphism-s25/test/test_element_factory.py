import unittest
from src.element_factory import load_element_data
import os


class TestElementFactory(unittest.TestCase):
    def setUp(self):
        self.small_atomic_mass = [16.123117768, 1.007968828, 23.176707824, 35.269046149999994, 128.978366924]
        self.big_atomic_mass = [106.811819668, 191.45161273, 40.30669855, 79.604880337, 84.643080672, 176.33755965999998, 253.924310601, 65.498796095, 132.001725473, 59.453174867, 16.123117768, 224.702529484, 101.773619333, 128.978366924, 270.048524239, 32.246235536, 23.176707824, 7.053590056, 28.215456094, 210.596445242, 233.77096132600002, 93.71260838399999, 211.60441407, 170.291938432, 223.69456065599996, 75.57464883, 274.079303681, 91.697218663, 119.91048301699999, 264.000711271, 40.30779441999999, 291.20710266699996, 48.368257434, 112.857440896, 252.916341773, 239.81658255399998, 187.421381223, 9.068979777, 166.26115899, 185.405991502, 19.145928382, 27.207487266, 208.581055521, 260.977900657, 259.969931829, 266.017744797, 232.764088368, 164.245769269, 24.184676652, 182.383180888, 20.153897209999997, 138.047346701, 160.215537762, 264.001807141, 89.681828942, 205.558244907, 269.040555411, 296.246398872, 140.062736422, 88.673860114, 290.200229709, 4.030779442, 52.399036876, 198.50520278599998, 297.25327182999996, 127.971493966, 51.391068048, 56.429816318, 248.885562331, 98.75080871899999, 286.169450267, 108.82720938899999, 64.490827267, 179.360370274, 174.322169939, 146.10945352, 211.604962005, 145.10148469199999, 244.855330824, 103.78900905399999, 202.53543429299998, 273.071334853, 59.452626932, 258.961963001, 11.084369498, 14.107728047, 73.55925910900001, 153.162495641, 268.032038648, 39.299825592, 262.99383831299997, 85.6510495, 238.809709596, 70.536448495, 122.933293631, 115.88025151000001, 141.07070525, 287.176323225, 168.27654871099998, 151.14710592, 193.46700245099998, 35.269046149999994, 294.230461216, 96.735418998, 134.01711519399998, 158.200148041, 31.238266707999998, 45.34544682, 228.733308926, 12.092338326, 227.725340098, 142.078674078, 248.886110266, 1.007968828, 196.489813065, 55.421847490000005, 245.862203782, 80.612849165]
        self.big_symbol = ["Pd", "Os", "Ar", "Se", "Kr", "Lu", "Es", "Zn", "Xe", "Ni", "O", "Fr", "Ru", "Te", "Mt", "S", "Na", "Li", "Si", "Bi", "Th", "Nb", "Po", "Tm", "Rn", "As", "Rg ", "Zr", "Sn", "Lr", "Ca", "Fl", "Ti", "Cd", "Cf", "U", "Re", "Be", "Ho", "W", "F", "Al", "Pb", "No", "Md", "Bh", "Pa", "Dy", "Mg", "Ta", "Ne", "Ba", "Tb", "Db", "Y", "Tl", "Hs", "Og", "La", "Sr", "Mc", "He", "Cr", "Au", "Ts", "I", "V", "Fe", "Cm", "Tc", "Nh", "Ag", "Cu", "Hf", "Yb", "Pm", "At", "Nd", "Am", "Rh", "Hg", "Ds ", "Co", "Fm", "B", "N", "Ge", "Eu", "Sg", "K", "Rf", "Rb", "Np", "Ga", "Sb", "In", "Ce", "Cn ", "Er", "Sm", "Ir", "Cl", "Lv", "Mo", "Cs", "Gd", "P", "Sc", "Ac", "C", "Ra", "Pr", "Bk", "H", "Pt", "Mn", "Pu", "Br"]
        self.big_name = ["Palladium", "Osmium", "Argon", "Selenium", "Krypton", "Lutetium", "Einsteinium", "Zinc", "Xenon", "Nickel", "Oxygen", "Francium", "Ruthenium", "Tellurium", "Meitnerium", "Sulfur", "Sodium", "Lithium", "Silicon", "Bismuth", "Thorium", "Niobium", "Polonium", "Thulium", "Radon", "Arsenic", "Roentgenium ", "Zirconium", "Tin", "Lawrencium", "Calcium", "Flerovium", "Titanium", "Cadmium", "Californium", "Uranium", "Rhenium", "Beryllium", "Holmium", "Wolfram", "Fluorine", "Aluminum", "Lead", "Nobelium", "Mendelevium", "Bohrium", "Protactinium", "Dysprosium", "Magnesium", "Tantalum", "Neon", "Barium", "Terbium", "Dubnium", "Yttrium", "Thallium", "Hassium", "Oganesson", "Lanthanum", "Strontium", "Moscovium", "Helium", "Chromium", "Gold", "Tennessine", "Iodine", "Vanadium", "Iron", "Curium", "Technetium", "Nihonium", "Silver", "Copper", "Hafnium", "Ytterbium", "Promethium", "Astatine", "Neodymium", "Americium", "Rhodium", "Mercury", "Darmstadtium ", "Cobalt", "Fermium", "Boron", "Nitrogen", "Germanium", "Europium", "Seaborgium", "Potassium", "Rutherfordium", "Rubidium", "Neptunium", "Gallium", "Antimony", "Indium", "Cerium", "Copernicium ", "Erbium", "Samarium", "Iridium", "Chlorine", "Livermorium", "Molybdenum", "Cesium", "Gadolinium", "Phosphorus", "Scandium", "Actinium", "Carbon", "Radium", "Praseodymium", "Berkelium", "Hydrogen", "Platinum", "Manganese", "Plutonium", "Bromine"]
        self.small_symbol = ["O", "H", "Na", "Cl", "Te"]
        self.small_name = ["Oxygen", "Hydrogen", "Sodium", "Chlorine", "Tellurium"]
        self.__delta = 0.001
        if os.getcwd().endswith('test'):
            raise Exception('Please run this test from the project directory. Rememeber to check your run configuration.')

    def test_atomic_mass_exists(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        for element in data:
            self.assertTrue(hasattr(element, 'atomic_mass'))

    def test_load_element_data_returns_list(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        self.assertIsInstance(data, list)

    def test_load_element_data_returns_nonzero_list(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

    def test_element_factory_small(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertAlmostEqual(element.atomic_mass(), self.small_atomic_mass[i], delta=self.__delta)
        self.assertEqual(len(self.small_atomic_mass), len(data))

    def test_atomic_mass_returns_float(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        for element in data:
            self.assertIsInstance(element.atomic_mass(), float)

    def test_element_factory_big(self):
        file_path = os.path.join("data", "big_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertAlmostEqual(element.atomic_mass(), self.big_atomic_mass[i], delta=self.__delta)
        self.assertEqual(len(self.big_atomic_mass), len(data))

    def test_element_factory_big_and_small(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertAlmostEqual(element.atomic_mass(), self.small_atomic_mass[i], delta=self.__delta)
        self.assertEqual(len(self.small_atomic_mass), len(data))

        file_path = os.path.join("data", "big_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertAlmostEqual(element.atomic_mass(), self.big_atomic_mass[i], delta=self.__delta)
        self.assertEqual(len(self.big_atomic_mass), len(data))

    def test_element_factory_sort(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        sorted_small = sorted(self.small_atomic_mass)
        for i, element in enumerate(sorted(data)):
            self.assertAlmostEqual(element.atomic_mass(), sorted_small[i], delta=self.__delta)
        self.assertEqual(len(sorted_small), len(data))

    def test_element_factory_sort_big_and_small(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        sorted_small = sorted(self.small_atomic_mass)
        for i, element in enumerate(sorted(data)):
            self.assertAlmostEqual(element.atomic_mass(), sorted_small[i], delta=self.__delta)
        self.assertEqual(len(sorted_small), len(data))

        file_path = os.path.join("data", "big_elements.csv")
        data = load_element_data(file_path)
        sorted_big = sorted(self.big_atomic_mass)
        for i, element in enumerate(sorted(data)):
            self.assertAlmostEqual(element.atomic_mass(), sorted_big[i], delta=self.__delta)
        self.assertEqual(len(sorted_big), len(data))

    def test_element_not_return_default_str_method(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        for element in data:
            self.assertNotIn("<src.element.", element.__str__())
            self.assertNotIn("object", element.__str__())

    def test_element_str_method_contains_name_small(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertIn(self.small_name[i], element.__str__())

    def test_element_str_method_contains_symbol_small(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertIn(self.small_symbol[i], element.__str__())

    def test_element_str_method_all_but_precision(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertIn(self.small_name[i], element.__str__())
            self.assertIn(self.small_symbol[i], element.__str__())

        file_path = os.path.join("data", "big_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertIn(self.big_name[i], element.__str__())
            self.assertIn(self.big_symbol[i], element.__str__())

    def test_element_str_method_contains_atomic_mass_precision_big(self):
        file_path = os.path.join("data", "big_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertIn(f"{self.big_atomic_mass[i]:.5f}", element.__str__())

    def test_element_str_method_all(self):
        file_path = os.path.join("data", "small_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertIn(self.small_name[i], element.__str__())
            self.assertIn(self.small_symbol[i], element.__str__())
            self.assertIn(f"{self.small_atomic_mass[i]:.5f}", element.__str__())

        file_path = os.path.join("data", "big_elements.csv")
        data = load_element_data(file_path)
        for i, element in enumerate(data):
            self.assertIn(self.big_name[i], element.__str__())
            self.assertIn(self.big_symbol[i], element.__str__())
            self.assertIn(f"{self.big_atomic_mass[i]:.5f}", element.__str__())


if __name__ == '__main__':
    unittest.main()