# Overview

This lab gives practice working with strings, lists, and tuples.

We also continue to reinforcing our workflow using PyCharm, GitLab, and WebCAT.

You must use the lab machines for this lab during class, and strive to complete
during lab.

Ask questions as needed, don't just "spin your wheels" without making progress.

Students must fork to their `firstname.lastname.yy-cpsc250-semesterYear` group,
and clone the forked project using Gitlab and Git from the command line.  
Complete the exercises using PyCharm by following along with in-class demonstrations.  

Work must be completed and submitted __to WebCat__ for a grade.  
Presuming your WCUSER/WCPASS variables are set up correctly, this should happen
automatically when you push changes to GitLab.

__You are responsible for verifying the submission and grade on WebCat.  This is part of your final grade.__


****
Work flow
====

Follow the below directions, and get a checkoff from your instructor before continuing on to the next exercise.

 * Fork the project to your personal group as described above
 * Open `gitbash` terminal
 * Change to the *root* folder using `cd /`
 * List files using `ls -altr`
 * Change to your home folder using `cd ~`
 * List files using `ls -altr`
 * Change into your preferred course directory
   * Possibly `cd Desktop`
   * Make new course directory if it does not exist (e.g. `mkdir cs250l`)
   * Change using `cd <folder name` (e.g. `cd cs250l`)
 * Clone the project from your personal fork
   * `git clone < your URL address>`
 * Change into the project folder (`cd lab02-f23`)
 * List files (`ls -altr`)
 * Open project in `PyCharm`
 * Mark the project folder as the *Sources Root*
 * Edit the `src/string_methods.py` and add your name to the `@author` tag at top
 * Go back to `gitbash` terminal
   * `git status`
   * `git diff`
 * Assuming the change is valid, `git commit -am "specified my name"`
 * `git push origin main`

 * Open WebCAT, and verify your submission reached WebCAT.
   * If not, then verify that you forked to your course group and the WCUSER and WCPASS variables are set.

 At this point, show your instructor your `gitbash` terminal and GitLab commit status before continuing.

### String methods

Fix the string methods in `src/string_methods.py` as specified in to *doc-strings* .

For this, you may assume the input string is a valid `str` type.

The solutions should only take one line of code.
If you don't know how to do it in one line, review ZyBooks and

* https://docs.python.org/3/library/stdtypes.html#str
* https://docs.python.org/3/library/stdtypes.html#str.format

Familiarize yourself with this documentation.  
You may need it on future exams.

After fixing each method, and testing, make a `git commit` for each fix,
then move on to the next method.

> NOTE: If you are stuck on one method, make a commit, and the move on to next.
> You ARE allowed to come back and fix them later, but do commit your progress.


### List methods 1

Fix the list methods in `src/list_methods.py` as specified in to *doc-strings* .

After fixing each method, and testing, make a `git commit`.

Push to Gitlab  at least after every two methods completed.


### List methods 2

Fix the list methods in `src/list_methods2.py` as specified in to *doc-strings* .

After fixing each method, and testing, make a `git commit`.

Push to Gitlab  at least after every two methods completed.


## Motions

You will fix the code in `src/motion.py` as specified in to *doc-strings*
such that it functions like the TA presentation.

This models motion on a 2D grid (x, y) coordinates given incremental changes

The arguments are *tuples*, which cannot be modified.  You might need to change
one of them to a *list*; just use the *list()* function to convert!

```python
a = (3, 4, 5)  # a tuple
b = [3, 4, 5]  # a list
c = list(a)    # list from a tuple
d = tuple(b)   # tuple from a list
print(' a == b? ', a == b) # list not equal to tuple, even with same values (False)
print(' a == d? ', a == d) # tuples are equal  (True)
print(' b == c? ', b == c) # lists are equal  (True)
```

Good luck and have fun!

## Grading

This lab is graded out of 100 points based participation, your correctness score on WebCat, and style conformity (grader script on GitLab):

* 30 points - Progress/participation during lab period
* 40 points - Logical Correctness (WebCAT)
* 30 points - Style points (Grader script)


1. Participation (30 points)
  * Based on good effort and progress during the lab period
  * You are not allowed to leave until full credit on WebCat
2. The code will be automatically tested by WebCat (40 points)
   * Check your WebCat  to verify points (this is the grade that counts)
   * Due before your next lab period if you do not finish during lab period
   * There is plenty of time to ask questions and complete, but try to finish early as there is other work to do!
3. The code will automatically be graded for style (30 points)
   * Run the `test_pylint.py` or `grader.py` script and address any issues
     * You can run in PyCharm or see the GitLab output
   * You must get at least 50% on the overall correctness before style is scored!
   * This includes variable names and code suggestions from PyLint

 If you complete the lab during the lab period, then show grader output
 on GitLab with full credit to your instructor, and you are free to leave.

 If you do not get full credit by the end of lab period, then you need to finish the projects outside of lab.

 Your participation credit in that case is based on making a good effort the entire period, including asking appropriate questions to help you make progress.

 Work outside of lab must be your individual work following empty hands rules.

 ### License

 This assignment and all associated files are for the private use of students currently
 enrolled in the CPSC 250 Lab course at Christopher Newport University.

 All associated files are copyright 2024 by Christopher Newport University.
 Posting publicly or sharing files is expressly forbidden.
