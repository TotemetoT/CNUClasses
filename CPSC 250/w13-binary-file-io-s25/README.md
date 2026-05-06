# Overview

This in-class participation exercise using File I/O, numpy, and MatPlotLib.

Students must fork to their `firstname.lastname.yy-cpsc250-semesterYear` group, and clone the forked project using Gitlab and Git from the command line.

The grading for this project will require submission of plots (with your name) to scholar as well as grading via Web-CAT.

****
Project Coding Exercises
====

## In Class - Binary File IO

* We will write some methods in `signal_io.py` that handles the data as described in class.
* We will begin by reading in the data from `data/signal_data.csv`.
    * The data has 3 columns of data: 2 integers and 1 floating point value.
    * The first two columns are the time stamp of the data given as a Epoch (Unix standard) timestamp in
      whole seconds and nanoseconds since midnight January 1, 1970 (GMT).
        * See https://www.epochconverter.com for more information.

* Practice reading in a binary file, using NumPy, and matplotlib in `mystery_data.py`
    * We will read in `mystery_data.dat`. The format is a columnwise dataset with 3 integers and it is in big endian format.
    * While reading in the data you can check your results by looking at the data in `mystery_data.csv`

We will write this data in binary format as directed in class using a `bytearray` and `struct` module.
You may choose either big endian or little endian formating so long as you are consistent.

## Homework - Practice

* For homework there are functions you must complete in `homework.py`.
* Practice reading in a binary file and matplotlib with `read_star_data.py`

Note: `signal_io.py` and `homework.py` are graded via Web-CAT. Your instructor may ask you to submit plots to scholar.


## Pickle Demo

A Python "pickle" file is an easy way of preserving data in binary form.
It is useful for short term storage, but can be easily broken by code changes or Python version changes.  
We provide notes for the `pickle_demo.py` and `pickle_test.py` files.  

Pickle will NOT be on the exam.

*****

Copyright 2024 Christopher Newport University.

All rights reserved.

For the private use of CNU students currently enrolled in CPSC 250.
Not for posting on any site other than internal personal
group on `student-gitlab.pcs` server.
