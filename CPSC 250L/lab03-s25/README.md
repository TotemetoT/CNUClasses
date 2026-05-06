# Overview

This lab focuses on reinforcing our workflow, and working with strings, lists, and dictionaries.

Students must fork to their `firstname.lastname.yy-cpsc250-semesterYear` group, and clone the forked project using Gitlab and Git from the command line.  Complete the exercises using PyCharm by following along with in-class demonstrations.  

Work must be completed and submitted __to WebCat__ for a grade.  

Presuming your WCUSER/WCPASS variables are set up correctly, this should happen automatically when you push changes to GitLab.  __You are responsible for verifying the submission and grade on WebCat.  
This is part of your final grade.__

The grading is based participation and your correctness score on WebCat:
1. Participation (30 pts)
  * Based on good effort and progress *during the lab period*
  * You are not allowed to leave until full credit on WebCat
2. The code will be automatically tested by WebCat (70 points)
   * 30% Style from grader script
   * 40% Correctness from grader script and WebCat
      * Check WebCAT page to verify correctness points (this is the grade that counts)
   * Due before your next lab period if you do not finish during lab period
   * There is plenty of time to ask questions and complete, but try to finish
     early as there is other work to do!


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
 * Change into the project folder (`cd <lab name>`)
 * List files (`ls -altr`)
 * Open project in `PyCharm`
 * Mark the main project folder as the *Sources Root* (see lab01 for directions)
 * Edit the `src/string_methods.py` and add your name to the `@author` tag at top
 * Go back to `gitbash` terminal
   * `git status`
   * `git diff`
 * Assuming the change is valid, `git commit -am "specified my name"`
 * `git push origin main`




### String methods

Fix the string methods as specified in to *doc-strings* in `src/string_methods.py`.

You need to fix some style and naming issues.
Look at the unit tests to confirm desired method names!

After fixing each method, and testing, make a `git commit`.

Push to Gitlab  at least after every two methods completed.


## Grocery Shopping

Fix the code in `src/grocery_store.py`.

The method `stock()` should return a reference to a `dict()` with the following `key:value` pairs
 * "pink lady apple":2.99
 * "honeycrisp apple":3.99
 * "eggs":1.29
 * "bananas":3.99
 * "milk":4.59
 * "ground beef":8.99
 * "cheerios":3.69

> Note: These prices are out of date, and have not been adjusted for recent inflation.

 To do this, you need to create a dictionary object with the above data, and
 return the reference to that object.  There are several ways to do this,
 including a one-liner.

The method `shop(stock_dict, grocery_list)` takes a reference to a stock dictionary,
as returned by `stock()` above, and a grocery list as a `list` of `tuples`.
Each `tuple` is a pair `("item name", qty)`

For example, given `grocery_list = [ ("honeycrisp apple", 2), ("milk", 1), ("delci food", 1)]`.

Example usage: `shop(stock(), grocery_list)`

The `shop` method returns a `3-tuple` with `(total, receipt, out_of_stock)`, where:
 * `total` is a `float` of the total cost of shopping trip
 * `receipt` is a single `str` (string) type can be printed; format described below
 * `out_of_stock` is a list of strings for each item name that is not in stock

 Using the example `grocery_list` above, the result would be:
 * `total` is 12.57
 * When printed, the `receipt` will look something like:
 <pre>
 honeycrisp apple     $  7.98
 milk                 $  4.49
                       ------
 total                $ 12.57
</pre>
 * The `out_of_stock` will be `["delci food"]`

 The items should be on one line per item when printed (e.g. include line separator),
 starting with the first item on first line and continuing in same order as the
 grocery list.  Use a `$` for each price.
 The last line should be the total cost with `$`.
 Use a delimiter such as `------` to separate total from items.

 You will get partial credit for having the `item name` and `subtotal` for each,
 and `total` in receipt.
 Partial credit for the correct number of lines, and the `-----` division line,
 and `$` .

 Recall your string formatting (ZyBooks 4.8).


 I suggest you code incrementally.
 * Get the `stock` method working and passing all tests before starting on `shop`.
 * With `shop`, get the `total` correct for those tests
 * Next, then work on the `out_of_stock` list
 * Then focus on the `receipt` tests


Good luck and have fun!

## Grading (100 points)

 * 40 points correctness (as measured on WebCAT)
 * 30 points style (as measured by grader script)
 * 30 points significant participation during lab
