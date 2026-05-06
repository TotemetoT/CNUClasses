# Overview Lab06 - Working with classes


This lab reworks Lab04 to focus on working with classes.
I have provided you a solution to Lab04 in `given/make_library_dict.py` for comparison.
> NOTE: This is "A" solution NOT "THE" solution.
>  There are many possible correct solutions to Lab04 as
> there are for this lab.

> Take a few minutes to review this solution and compare to your solution for `lab04`.

> Note: There is also a `convert_data` script that I used to update the list I
 found online to put it into the TAB separated format.  You don't need this, but
 I provide as a reference.

# Directions

For this lab, we will use classes to organize the data instead of dictionaries.

Define two classes: `Book` and `Library` and a `main` method that:
* reads data file in the `data` folder
   * Start with the `small_list.txt`, but use `big_list.txt` for full credit
      * Books lists are based on https://gist.github.com/jaidevd/23aef12e9bf56c618c41

The book data is stored in a TAB separated list with a header starting with `#`.
```
# Title	Author	Genre	SubGenre	Height	Publisher
Fundamentals of Wavelets	Goswami, Jaideva	tech	signal_processing	228	Wiley
Data Smart	Foreman, John	tech	data_science	235	Wiley
God Created the Integers	Hawking, Stephen	tech	mathematics	197	Penguin
```
   * Store the book data in an instance of `Book` class
     * Ignore the `Height` field
   * Store the data in an instance of the `Library` class
     * The `Library` will hold all of the lists of books
       * There are several ways to think about what `attributes` the class should have.

   * print using the instance of the library
     * that is, your main should have a `print(library)` statement
     that uses the `__str__` methods of `Library` and `Book` appropriately.
     * Output should be organized by genre type
       * 'fiction', 'nonfiction', and 'textbook'
       * When printed each list of books should be organized by:
         * author, then title, then publisher
           * Note: some publishers are unknown (e.g. ""), so add them as "" if needed
           * The fields should be aligned when printed, so specify column width for strings
             * Note: This is an excellent opportunity for incremental coding.
               * Get any list print working, commit, then work on aligning columns
         * Fields may be blank (empty string "")
         * the list `sort` method is your friend, but it requires work in your `Book` class
       * Ignore 'comic' books
       * Anything other than 'fiction' or 'nonfiction' categorize as `textbook`.

Do a design first!
  > Students are expected to deliver evidence of design work in the
  form on comments in code as an early commit, or a flow chart or other drawing.
  > This work is required *before* the end of class.
  > Failure to complete a "reasonable" initial design will incur a 50%
    penalty in the overall grade.

Students must fork to their `firstname.lastname.yy-cpsc250-semesterYear` group, and clone the forked project using Gitlab and Git from the command line.  Complete the exercises using PyCharm by following along with in-class demonstrations.  


The grading is based participation and your demonstration to lab TA:
1. Participation (30 pts)
  * Based on good effort and progress *during the lab period*
  * A commit showing basic design *before* you start coding
  * Evidence of incremental development and testing based on commit history!
  * You are not allowed to leave early unless you demonstrate the entire solution
2. Grading (70 points)
   * 30% Style from grader script
   * 30% TA Code review and *efficiency* of your code
     * Did you use classes and methods properly; did you implement `__str__` method.
   * 30% Demonstration to TA
   * Due before your next lab period if you do not finish during lab period
   * There is plenty of time to ask questions and complete, but try to finish early as there is other work to do!


Good luck and have fun!

######

Copyright 2024 Christopher Newport University

Only for posting on student-gitlab.pcs.cnu.edu
