"""
Main class - Animal:
    Attributes:
        * first_name
        * middle_name
        * last_name
        * species
        * age
    Method:
        * __str__ returns string w/ full name, species & age
 > Subclass - Mammal:
        Additional Attribute:
            * diet; (Carnivore, Herbivore, Omnivore)
        Overridded Method:
            * Add diet to __str__ using super()
 > Subclass - Bird:
        Additional Attribute:
            * wing_span_meters; (float number)
        Overridden Number:
            * add wing_span_meters to __str__ using super()
 > Subclass - Reptile:
        Additional Attribute:
            * region; ONLY THESE ARE VALID - (Rainforest, Savannah, Desert, Mountain, Wetlands)
        Overridden Method:
            * add region to __str__ using super()
Break down info from txt file:
 > Break down through the spaces since can't use delim
 > Use the period in middle names to see if there is a middle name (ex. M.)
"""
from given.generator import middle_names
import os

class Animal:
    def __init__(self, first_name, last_name, species, age, middle_name=""):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.species = species
        self.age = age
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}, {self.species}, {self.age}'
class Mammal(Animal):
    def __init__(self, first_name, last_name, species, age,diet, middle_name=""):
        Animal.__init__(self, first_name, last_name, species, age, middle_name)
        self.diet = diet
    def __str__(self):
        possible_diets = ["Carnivore","Herbivore","Omnivore"]
        if self.diet in possible_diets:
            return super().__str__() + f', {self.diet}'
        else:
            print(f'{self.diet} is not in possible_diets -> Skipping')
            # raise ValueError(f'{self.diet} is not in possible_diets')
class Bird(Animal):
    def __init__(self, first_name, last_name, species, age, wing_span_meters, middle_name=""):
        Animal.__init__(self, first_name, last_name, species, age, middle_name)
        self.wing_span_meters = wing_span_meters
    def __str__(self):
        if self.wing_span_meters[0].isdigit():
            return super().__str__() + f', {self.wing_span_meters}'
        else:
            print(f'{self.wing_span_meters} is not a number -> Skipping')
            # raise ValueError(f'{self.wing_span_meters} is not a number')
class Reptile(Animal):
    def __init__(self, first_name, last_name, species, age, region, middle_name=""):
        Animal.__init__(self, first_name, last_name, species, age, middle_name)
        self.region = region
    def __str__(self):
        possible_regions = ["Rainforest", "Savannah", "Desert", "Mountain", "Wetlands"]
        if self.region in possible_regions:
            return super().__str__() + f', {self.region}'
        else:
            print(f'{self.region} is not in possible_regions -> Skipping')
            # raise ValueError(f'{self.region} is not in possible_regions')

def file_breakdown(file_path):
    possible_diets = ["Carnivore", "Herbivore", "Omnivore"]
    possible_regions = ["Rainforest", "Savannah", "Desert", "Mountain", "Wetlands"]
    animal_list = []
    instance_list = []
    with open(file_path, 'rt') as fin:
        lines = fin.read()
        lines = lines.splitlines()
        for line in lines:
            line = line.split("\t")
            if len(line) != 7:
                # raise ValueError(f'line: {line} length:{len(line)}, should be 7')
                print(f'length:{len(line)}, should be 7; Line: {line} -> Skipping')
            else:
                if not line[5].isdigit():
                    # raise ValueError(f'Value ({line[5]}) cannot be negative and must be a number; Line: {line} -> Skipping')
                    print(f'Value ({line[5]}) cannot be negative and must be a number; Line: {line} -> Skipping')
                else:
                    animal_list.append(line)
    for line in animal_list:
        if line[0] == "Reptile":
            if line[-1] in possible_regions:
                instance_list.append(Reptile(line[1], line[2], line[4], line[5], line[6], line[3]))
            else:
                # raise ValueError(f'Region must be in possible_regions - {list[-1]}:{possible_regions} -> Skipping')
                print(f'Region must be in possible_regions - {list[-1]}:{possible_regions} -> Skipping')
        elif line[0] == "Bird":
            if line[-1][0].isdigit():
                instance_list.append(Bird(line[1], line[2], line[4], line[5], line[6], line[3]))
            else:
                # raise ValueError(f'Wingspan ({line[-1]}) must be a digit -> Skipping')
                print(f'Wingspan ({line[-1]}) must be a digit; Line: {line} -> Skipping')
        elif line[0] == "Mammal":
            if line[-1] in possible_diets:
                instance_list.append(Mammal(line[1], line[2], line[4], line[5], line[6], line[3]))
            else:
                # raise ValueError(f'Region must be in possible_regions - {list[-1]}:{possible_regions} -> Skipping')
                print(f'Diet must be in possible_diets - {list[-1]}:{possible_diets} -> Skipping')
        else:
            raise ValueError(f'{line[0]} is not an animal from this Zoo')
    return instance_list

def instance_breakdown(animals):
    animal_dict = {
        "Mammal":[],
        "Bird":[],
        "Reptile":[]
    }
    for animal in animals:
        if isinstance(animal, Mammal):
            animal_dict["Mammal"].append(animal)
        elif isinstance(animal, Bird):
            animal_dict["Bird"].append(animal)
        elif isinstance(animal, Reptile):
            animal_dict["Reptile"].append(animal)
    for key in animal_dict:
        wPath = os.path.join("data",key + ".txt")
        with open(wPath,'wt') as clear:
            clear.write("")
        with open(wPath,'a') as adding:
            for animal in animal_dict[key]:
                adding.write(f'{animal.__str__()}\n')
if __name__ == "__main__":

    instances = file_breakdown("data/zoo.txt")

    instance_breakdown(instances)





