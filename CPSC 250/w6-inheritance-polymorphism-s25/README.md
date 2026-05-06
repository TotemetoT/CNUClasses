# Overview

This in-class participation exercise using Classes, Polymorphism, and operator overloading.

Students must fork to their `firstname.lastname.yy-cpsc250-semesterYear` group, and clone the forked project using Gitlab and Git from the command line.  
Complete the exercises using PyCharm by following along with in-class demonstrations.  

This project will be graded, and must be submitted to WebCat.


****
Project Coding Exercises
====
 ## In-class Exercises
* `clock_demo.py` - Demonstrate the Clock class.
* `hr_system.py` - Demonstrate inheritance with Person, Employee, Student classes.

 ## Homework
 ### Homework Part 1 - Inheritance Practice
In this project you will write 9 classes as shown in the slides

The classes are to be defined in the `src` folder using the following file and class names:
* `farm_animal.py` : `FarmAnimal`
  * All farm animals have constructor that has a single age (in years) instance attribute  (use `self.age` as the name)
  * All farm animals have a `str` conversion method that prints the class type and age; you can do this with only a single `str` method in the `FarmAnimal` or you can override as needed.
  * All farm animals have a `make_sound` method that returns a string
    * The method in `FarmAnimal` should just return an empty string
  * All farm animals have an equal (`__eq__`) method that returns true if the objects are the same class type and the same age
    * That is, two 3-year-old `Hen` instances are equivalent, but a `Cow` and `Duck` are never equivalent.
    
* `winged_animal.py` : `WingedAnimal`
  * Winged animals are FarmAnimals that make a `flap, flap` sound

* `ruminant.py` : `Ruminant`
  * https://en.wikipedia.org/wiki/Ruminant
  * Ruminants make a `burp` sound

* `duck.py` : `Duck`
  * `Duck`s are `WingedAnimal`s that add a `quack, quack` sound
    * e.g. `flap, flap - quack, quack`

* `chicken.py` : `Chicken`
  * `Chicken`s are `WingedAnimal`s that add a `cluck, cluck` sound

* `goat.py` : `Goat`
  * `Goat`s are `Ruminant`s that add a `baaah` sound

* `cow.py` : `Cow`
  * `Cow`s are `Ruminant`s that make either (your choice) of two sounds:
    * They add `moo` to the `burp`, or
    * They say `Eat mor chikin!` without the `burp` (these are civilized cows)

* `hen.py` : `Hen`
  * `Hen`s are `Chicken`s that add a `squawk!` sound when laying eggs
    * e.g. `flap, flap - cluck, cluck - squawk!`

* `rooster.py` : `Rooster`
  * `Rooster`s are `Chicken`s that add a `cock-a-doodle doo` to WingedAnimal sound
    * e.g. `flap, flap - cock-a-doodle doo!`

These class definitions are repetitive but don't require a lot of code, and even less
if you properly use inheritance.

In addition to the classes, define `barnyard.py` script (not class) with the following methods:
* `get_barnyard()` method
  * returns a `list` of `FarmAnimals` containing:
    * At least 1 of each "leaf" types in the inheritance tree (i.e., Hen, Rooster, Duck, Cow, Goat)
    * At least 4 hens with the following ages (0.25, 0.6, 1.0, 8)
    * At least 3 roosters with the following ages (0.25, 0.6, 1.0)
    * Thus, the list must contain at least 10 items
    * Keep the list reasonable with no more the 100 items
    * Contains only `FarmAnimal` instances
    * I suggest using `random.shuffle` to shuffle your list in place so the animals are in no particular order for testing other methods

* `listen(barnyard_list)` method
  * Given a list, return a new list containing the associated sounds they make (one string item per animal)
  * If the list contains something other than a FarmAnimal, just ignore that item
    * Do not let the program crash, but I don't care how you protect this

* `get_roosters(barnyard_list)` method
  * Given list, return a new list containing only `Rooster`s
  * It is possible to do this in one line using a list comprehension
    * But you do NOT have to do it that "Pythonic" way

* `get_layers(barnyard_list)` method
  * Given a list of `FarmAnimal`s, return a new list containing only `Hen`s that are between the ages of 0.5 and 7.0 years inclusive
  * The given list may contain other animal types, so `isinstance` is your friend
  * It is possible to do this in one line using a list comprehension with if statement
    * But you do NOT have to do it that "Pythonic" way

### Usage
<pre>
cow = Cow(3.5)
print(cow)
print(cow.make_sound())
barnyard = [cow] # A list with one cow
</pre>

shows:
<pre>
Cow : 3.5
burp - moo
</pre>
### Look at the provided unit tests for more details!

### Homework Part 2 - Classes and File IO
You are given two text data files:
 * small_elements.csv 
 * big_elements.csv

The ``small`` files contain less data and simpler format and are useful for testing initial.
The ``big`` files contain most data, but is still using simpler format.

### Original data from
* https://byjus.com/chemical-compound-formulas/
* https://gist.github.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee

The `*_elements` files contain information about the atomic structure of atoms of various elements.
The data is given as a comma (',') delimited CSV file with the following data on each line

<pre>
{name},{symbol},{num_protons},{num_neutrons},{num_electrons},{type}
</pre>

Where `type` is either `Nonmetal`, `Metal`, or `Metalloid`.

### Instructions for element.py
You should design and implement a class inside `src/element.py` file that holds
the data for name, symbol, and number of protons/electrons/neutrons as attributes.

Your class needs a method called `atomic_mass` that calculates the total atomic mass in kg/mol using:

 * neutron_kg_per_mol  = 1.007420893
 * proton_kg_per_mol   = 1.007420170
 * electron_kg_per_mol = 0.000548658

You should define these values as private class attributes (not instance attributes).

So, an atom with 2 protons would have an atomic mass of 2.0144 kg per mol (where a mol is 6.023E26 individual atoms). 
    Note: This is an approximation that does not include the binding energy.

Create a string conversion method that prints "symbol, name, mass kg/mol" for each instance.
Use five decimal places for the atomic mass.

We will want to sort a list of atoms by *atomic mass* using `elements_list.sort()`.
To do this easily, we'll need a less than (<) operator defined for the class 
that does a comparison based on the atomic mass (not name!).


After you create your class, modify `element_factory.py` to read the `elements` file and return a list of Element instances.
Note: All grading will be done based on the objects returned from the `element_factory.py` file.
So you need both the element class and the `element_factory` completed to pass any 
tests.  Think about who you can test your `element` class before completing 
`element_factory.py`.
