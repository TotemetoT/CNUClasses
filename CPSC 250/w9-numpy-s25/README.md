# Overview

This in-class participation exercise demonstrates file I/O, calculations using NumPy,
 plotting using MatPlotLib, and file I/O using the CSV module.

Students must fork to their `firstname.lastname.yy-cpsc250-semesterYear` group, and clone the forked project using Gitlab and Git from the command line.  Complete the exercises using PyCharm by following along with in-class demonstrations.  

Work must be completed and submitted __to WebCat__ for a grade.  
Presuming your WCUSER/WCPASS variables are set up correctly, this should happen automatically when you push changes to GitLab.  
__You are responsible for verifying the submission and grade on WebCat.  This is part of your final grade.__

> Some, but not all of the code, will be automatically graded by WebCat (100 points)
>   * Check your WebCat page to verify points (this is the grade that counts)
>   * Due date specified on WebCat
>   * There is plenty of time to ask questions and complete, but try to finish early as there is other work to do!


****
Project Coding Exercises
====

For this we have given you some code that is commented out.
Follow along in class, and uncomment/comment the code as directed.

## In Class - NumPy, Matplotlib, and Monte Carlo Methods
* `angles_module.py`
  * re-do `angles.py` from prior work but now with NumPy goodness!
* `plot_sine_module.py`
  * Plot sine function (`sin` is method name) using NumPy arrays
* `monte_carlo_pi.py`
  * Calculate the value of pi using the Monte Carlo method

## Homework
### NumPy and Matplotlib practice
* `homework_numpy.py`
  * Practice with NumPy and Matplotlib

### Inheritance Practice


We will write some some classes for practice, and then practice file I/O and
creating instances.  The concept is based on a simplified role playing game in a
fantasy realm.

We will not be making use of the classes in a game in 250,  but you are welcome to expand!.
We will just use for practice before Exam 3.

The inheritance diagrams will be discussed in lecture.  

Briefly, your code will read the data file and return a list of `Humanoid` instances.
`Humanoids` are characterized in this fantasy world as `Human`, `Dwarf`, `Elf`, or `Harfoot`.
Each `Humanoid` has attributes for  `agility`, `perception`, `stealth`, `strength`, and `wisdom`.


Write your classes, so that you can read the `characters.csv` file and properly populate
the instances according to the test file.

To simplify the tests, write all required classes in the `game.py` file.

Write the function `read_characters_from_file` to read the data file in `read_characters.py`.
The data in file is given by:

`Name`, `Humanoid`, `agility`, `perception`, `stealth`, `strength`, `wisdom`


Read the data and create the instances in the order that they are defined in file, and
return a list of instance in same order as the file.

You will need to define a less than operator for Humanoid so I can sort by name so that they pass the tests.


## Deliverables
* Check Scholar for an assignment where you should upload your plots for plot_sine and monte_carlo_pi

Submit all plots for a grade on Scholar. Web-CAT Grading will be for `homework_numpy.py` and `homework_weather.py` only.

> Unit tests are provided for some methods; these will be run in WebCAT for grade.


### License

This assignment and all associated files are for the private use of students currently
enrolled in the CPSC 250 course at Christopher Newport University.

All associated files are copyright 2025 by Christopher Newport University.
Posting publicly or sharing files is expressly forbidden.
