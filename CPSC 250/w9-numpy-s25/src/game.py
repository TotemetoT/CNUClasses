
"""
Write simple classes for fantasy role playing game here

"""
# from rdkit.Contrib.LEF.AddLabels import delim
import csv
import os

class Humanoid:
    def __init__(self, name, species, agility, stealth, intelligence, dexterity, wisdom):
        self.name = name
        self.species = species
        self.agility = int(agility)
        self.stealth = int(stealth)
        self.intelligence = int(intelligence)
        self.dexterity = int(dexterity)
        self.wisdom = int(wisdom)

    def __lt__(self,other):
        return (self.wisdom, self.name) < (other.wisdom, other.name)

class Human(Humanoid):
    def __init__(self, name, agility, stealth, intelligence, dexterity, wisdom):
        super().__init__(name,"Human",agility,stealth,intelligence, dexterity,wisdom)
class Dwarf(Humanoid):
    def __init__(self, name, agility, stealth, intelligence, dexterity, wisdom):
        super().__init__(name, "Dwarf", agility, stealth, intelligence, dexterity, wisdom)
class Elf(Humanoid):
    def __init__(self, name, agility, stealth, intelligence, dexterity, wisdom):
        super().__init__(name, "Elf", agility, stealth, intelligence, dexterity, wisdom)
class Harfoot(Humanoid):
    def __init__(self, name, agility, stealth, intelligence, dexterity, wisdom):
        super().__init__(name, "Harfoot", agility, stealth, intelligence, dexterity, wisdom)

def read_characters_from_file(file_path):
    """
    param: file_path
    return: list of instances
    """
    print("Running")
    instance_list = []
    with open(file_path, 'rt') as fin:
        reader = csv.reader(fin,delimiter=',')
        next(reader)
        for read in reader:
            if read[1] == "Human":
                instance_list.append(Human(read[0],read[2],read[3],read[4],read[5],read[6]))
            elif read[1] == "Dwarf":
                instance_list.append(Dwarf(read[0],read[2],read[3],read[4],read[5],read[6]))
            elif read[1] == "Elf":
                instance_list.append(Elf(read[0],read[2],read[3],read[4],read[5],read[6]))
            elif read[1] == "Harfoot":
                instance_list.append(Harfoot(read[0],read[2],read[3],read[4],read[5],read[6]))
    return instance_list
if __name__ == '__main__':
    path = "data/characters.csv"
    characters = read_characters_from_file(path)
    print(characters)
    print(len(characters))