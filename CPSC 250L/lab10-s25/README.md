*****
Copyright 2025 Christopher Newport University.

All rights reserved.

For the private use of CNU students currently enrolled in CPSC 250L.
Not for posting on any site other than internal student-gitlab.pcs server.

*****

# Lab10

For this lab, you will be given overall requirements and are expected to use the Python
tools you've been taught to solve the problem and satisfy the requirements.

The Norfolk Zoo had an intern that accidentally mixed up all of their 
animal data files into one file and then deleted the software.
I won't say what university they were from, 
but let's just say they were not a graduate of CNU's CPSC 250 course!

Your job is to recreate the software, read the data file in a list of animal instances, 
then separate the animal instances by type, and write the data to new files.

You are expected to use class inheritance and separate using `isinstance`.

Unfortunately some of the data is bogus, and you will need to clean that up.
Just print a warning message when you encounter bogus data, skip the entry, 
and continue processing.  Do not crash the program.

Running `zoo.py` from the project folder as working directory, should read the relevant file, 
and write the data to separate files.

You should strive to finish this during this lab period.

Below are the original specifications for the project.

----

# Zoo Management System Details

## Overview
This lab simulates a **Zoo Management System** where you'll read animal data from 
a file and create instances of different classes using inheritance. 

Each animal will belong to a category (e.g., `Mammal`, `Bird`, `Reptile`) and 
will have specific attributes and behaviors based on its type. 

The goal is to practice file handling, data parsing, exception handling, 
and working with class inheritance in Python.

## Objectives
- **File Handling**: Learn to read and parse data from a file in Python.
- **Class Inheritance**: Use inheritance to model relationships between different types of animals.
- **Error Handling**: Implement exception handling to manage invalid or missing data.

## Problem Statement

1. **Base Class - Animal**  
   Create a base class named `Animal` with the following attributes and method:
   - **Attributes**:
     - `first_name`: Animal's first name.
     - `middle_name`: Animal's middle name (can be optional).
     - `last_name`: Animal's last name.
     - `species`: The scientific species name of the animal.
     - `age`: The animal's age. (only positive numbers are valid)

   - **Method**:
     - The default string method returns a string with the animal’s full name, species, and age.

2. **Subclass - Mammal**  
   Inherit from `Animal` to create a `Mammal` class, adding:
   - **Additional Attribute**: `diet` (e.g., "Carnivore", "Herbivore", "Omnivore").
     * Only these are valid!
   - **Overridden Method**: Update string method to include the diet.

3. **Subclass - Bird**  
   Inherit from `Animal` to create a `Bird` class, adding:
   - **Additional Attribute**: `wing_span_meters` (number e.g., number 1.5, 2.0).
   - **Overridden Method**: Update string method  to include the wing span.

4. **Subclass - Reptile**  
   Inherit from `Animal` to create a `Reptile` class, adding:
   - **Additional Attribute**: `region` (e.g., "Rainforest", "Savannah", "Desert", "Mountain", "Wetlands").
     - Only these strings are valid
   - **Overridden Method**: Update string method to include the region.

## Data File Format
The data file (`zoo.txt`) will contain tab-separated values with each 
line representing an animal entry in the following format:

`AnimalType\tLastName-LastName, FirstName, MiddleName\tSpecies\tAge\tAdditionalAttribute`


## Requirements

1. **File Parsing and Validation**:
   - Read and parse data from `zoo.txt`.
     - I suggest you start with `zoo_demo.txt` at first, then try other files. `zoo.txt` is required for full credit.
   - Use exception handling to manage missing or invalid data (e.g., non-numeric ages, invalid wing spans).
   - Print warnings and skip faulty entries.

2. **Class Instantiation**:
   - Create instances of `Mammal`, `Bird`, or `Reptile` based on the `AnimalType` field.
   - Use inheritance to define shared attributes in the `Animal` class and specific attributes in each subclass.
   - Validate data and throw error if invalid (but do not crash the program, just print warning)

3. **Display Animal Details**:
   - Print details of each valid animal entry using the string method from the respective class.

4. **Write separate data files for each type of animal.**




----

Submissions will NOT be graded by WebCat.  

It will be up to you to test and be confident in your work.
Think about testing strategy as part of your design.

You are required to demonstrate your code to the lab instructor for your final grade.

> NOTE: You should complete most of this during the lab period.
> Work inside AND outside of class is subject to the following restrictions.
> The work is your own independent work without reference to any resources other than:

* Zybooks
* https://student-gitlab.pcs.cnu.edu   - your personal CS250 repo's only
* You *are* allowed to reference your prior projects
* https://web-cat.cs.vt.edu    - your webcat submissions
* https://docs.python.org/3/

> You are expected to show incremental progress throughout the lab.
> Accessing prior semester solutions of your own or anyone else's, including online tutoring sites such as
> (but not limited to) Chegg, Docsity, StackOverflow or other is strictly forbidden and warrants a CHECS referral.
>
> Reference to StackOverflow for general questions (e.g. how to format a string) is allowed.
>
> You are only allowed to have general discussions (e.g. how to format a string) under empty hands rules.
> The design and implementation should be your own work.

> You *MAY* refer to ChatGPT for specific questions (e.g. how to plot on map), but not for the overall design.

## Grading

  * Final Grading (100 points)
    * 20 points: Significant progress during the lab
    * 20 points: Classes with inheritance defined and demonstrated
    * 20 points: Reading data from clean file
    * 20 points: Reading data from dirty file using exception handling
    * 10 points: Writing separate data files for each animal type
    * 10 points: Style and efficiency points defined by instructor
