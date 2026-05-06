# Overview

This weekly in-class and homework assignment will go over an introduction to classes and object-oriented programming.

Students must fork to their `firstname.lastname.yy-cpsc250-semesterYear` group, and clone the forked project using Gitlab and Git from the command line. Complete the exercises using PyCharm or as instructed.

The grading for this project will be based on grading via Web-CAT.

****
Project Coding Exercises
====
### File IO and Plotting
* `angles.py`
  * practice writing and reading data files using some math functions and `csv` module

* `plot_angles.py`
  * read data using existing module and visualization
  * Upload plot to Scholar

### Introduction to Classes

We will write a Car class in `car.py` will have the following instance attributes make, model, year, and color.

We will update `car_factory.py` as we go, and leave a bit for homework.

Follow along in class, and the complete after class.

### Methods and Operator Overloading

Later we will work on the `person.py` class, and `person_factory.py`, and
practice writing instance methods and operator overloading.

Follow along in class, but parts will be left for homework.


### Finally, we will cover some tricky issues with attributes

 The file `given/demo_class.py` demonstrates several issues with class and instance attributes.

# Homework

### Homework plotting
* `homework_complexity.py`
  * Write `csv` data
  * Read `csv` data
  * Visualize with MatPlotLib
    * Generate several different views of the data
    * Upload plots to Scholar


### Homework classes
We will continue working with `car.py` and write a new class in `planet.py`


Note: `car_factory.py`, `car.py`, and `person.py` are also graded via Web-CAT under this
same target!.

### Classes

The module `homework.py` continues working with the completed `car.py`
and practicing file I/O.


### Planet

We will write a Planet class in `planet.py` that takes `name`, `radius`, and `mass` as parameters in that order.

Store the data in relevant attributes.  Write `get_name`, `get_radius`, and `get_mass`
instance methods that return the relevant data.

The planet calculates spherical volume, average density, and acceleration due to gravity.
 * write  `get_volume`, `get_density`, and `get_gravity` using instance attributes.


I used the following data sources for writing the tests:
* http://www.softschools.com/formulas/physics/acceleration_due_to_gravity_formula/54/
* https://en.wikipedia.org/wiki/Gravitational_constant
* https://en.wikipedia.org/wiki/Earth

> NOTE: __Pluto was robbed!__  In my childhood, we had nine planets :-)

### Planet Factory

We will continue to practice our file I/O skills.  Read in the data from `data/planets.txt`,
and create a list of planet instances from this data.

>NOTE: The first two lines contain comments starting with a `#` characters.
Ignore those lines when you read in.
Start by reading file (you can use csv or not, your choice) and printing data.
  * Problem solving: What test will you do to skip comment lines?
  * You might want to look up the `continue` statement and it's use in `for` loops



### License

This assignment and all associated files are for the private use of students currently
enrolled in the CPSC 250 course at Christopher Newport University.

All associated files are copyright 2025 by Christopher Newport University.
Posting publicly or sharing files is expressly forbidden.
