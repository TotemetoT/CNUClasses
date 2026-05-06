# Overview

This in-class participation exercise demonstrates an introduction to file I/O ("Input/Output") as well as some homework problems.

Students must fork to their `firstname.lastname.yy-cpsc250-semesterYear` group, and clone the forked project using Gitlab and Git from the command line.  Complete the exercises using PyCharm by following along with in-class demonstrations.  

Work must be completed and submitted __to WebCat__ for a grade.  Presuming your WCUSER/WCPASS variables are set up correctly, this should happen automatically when you push changes to GitLab.  __You are responsible for verifying the submission and grade on WebCat.  This is part of your final grade.__

> Some, but not all of the code, will be automatically graded by WebCat (50 points for inclass and 50 for homework)
>   * Check your WebCat page to verify points (this is the grade that counts)
>   * Due date specified on WebCat

****
Project Coding Exercises
====
## In Class - Text File IO

For this we have given you some code that is commented out.
Follow along in class, and uncomment/comment the code as directed.

* `letter.py`
  * read a letter to students and display text
  * practice `open`, `read`, `close`, `tell`, and `seek`
* `fellowship.py`
  * practice `readlines` and `strip` to remove *white space* characters
  * newlines
* `small_data.py`
  * do NOT import any modules
  * define method `read_data(open_file)`
    * returns 3 separate lists, one per column
    * practice using `with`, `as`, and `split`
  * define method `append_data(file_name, max_val=32)`
    * complete pattern up to first column max_val
    * return total lines added
    * Hint: You might need to call `read_data` to add only what is needed
  * define method `write_data(file_name, start, end)`
    * Overwrite file with pattern from start to end
    * return total number of lines written
* `csv_data.py`
  * Start to use the `csv` module to simplify our lives
* `plot_data.py`
  * In class we will use matplotlib to plot the data

## Homework - String Manipulation Practice and File IO
* In `src/homework.py` String manipulation with lists and dictionaries.
* In `src/homework_file_io.py` you will find homework based on reading, writing, and appending text files.


> Unit tests are provided for some methods; these will be run in WebCAT for grade.
