# Lab 5 - Must be demonstrated before the start of the next class

For this lab, you will be given overall requirements, but you must come up with intermediate steps yourself.

Read this README carefully before starting.

Submissions will NOT be graded by WebCat.  
We will run the code on gitlab which will only fail if your program crashes.
A green check mark does NOT indicate success today.

It will be up to you to test and be confident in your work.
Think about testing strategy as part of your design.

You are required to demonstrate your code to the lab instructor for your final grade.
There is no WebCAT for this assignment; just push your code to GitLab.

> NOTE: You should complete most of this during the lab period.
> Work inside AND outside of class is required to be your own independent
> work without reference to prior solutions or any resources other than:

* Zybooks
* https://student-gitlab.pcs.cnu.edu   - your personal CS250 repo's only
  * You *are* allowed to reference your prior projects
* https://web-cat.cs.vt.edu    - your webcat submissions
* https://docs.python.org/3/
* https://docs.python.org/3/library/stdtypes.html?highlight=str#str ('str')
* https://docs.python.org/3/library/stdtypes.html#str.format (`format`)
* https://docs.python.org/3/library/string.html (`string` module)

> You are expected to show incremental progress throughout the lab.
> Accessing prior semester solutions of your own or anyone else's, including online tutoring sites such as
> (but not limited to) Chegg, Docsity, StackOverflow, ChatGPT or other is strictly
> forbidden and warrants a CHECS referral.
>
> Reference to StackOverflow for general questions (e.g. how to format a string) is allowed.
>
> You are only allowed to have general discussions (e.g. how to format a string) under empty hands rules.
> The design and implementation should be your own work.
> The use of ChatGPT for anything beyond "how do I format a string in Python" is
> not allowed.

You are expected to practice good problem solving skills on this assignment.



## Instructions

You are to write the script 'shopping.py'.

In the data folder you are given three txt files: List.txt, FoodLion.txt and HarrisTeeter.txt.
List.txt contains a list of the items and quantities of those items that the user wants to buy.

They could be listed as [item, quantity] or [quantity, item].
When reading the file, it is your job to differentiate between the two.
I have added a comma to separate (delimit) the item name and quantity.

*You are required to read the given data files, and not just copy the data.*

Your code should work if we changed the contents of the data files.

HarrisTeeter.txt and FoodLion.txt contain lists of items and their price values.
As a shopper you want to find the store that has your item for the cheapest price.
If both stores carry your item, buy the quantity needed from the shop selling the item for the smallest price.
If only one shop sells your item, then buy your item from there, regardless of the price.
If no shops sell your item, be sure to flag that item as ‘Not Sold’.

These are old prices and have NOT been updated to reflect recent inflation.
You should do so.  As you read in each price multiple each price (as a number) by 1.18
to reflect the dollars required in 2024 to purchase the same items given 2021 prices.

> Note:  Inflation is real, but the prices were mostly made up in the first place :-)

Also, folks are a bit inconsistent in their use of capital letters.  Your code
should use the names in the shopping list for receipt, but when searching for items
in the store you need to be *case insensitive*; e.g., so that 'Berries', 'beRries' all match 'berries' when looking up a price.

You should output the final shopping receipt as follows, containing the store an item was purchased from,
the item name, the quantity and the total price (after multiplying the item price by its quantity).
Then you should output the total.
Finally, you should put a list of items that were not found.
You may format the output however you'd like as long as it is neat and all items are spaced evenly with columns aligned.

![Example](output.png?raw+true)

**NOTES and HINTS**
* Your output will look different as the screenshot shown as your items and prices may vary.
* Your program should work on any data files that follow the same formatting, but have different data.
  * Think about using this to your advantage during testing.  
    * You are free to create some simpler test files, so long as you keep these and demonstrate using these files.

* Start by thinking through the steps you need to do
  * Write some comments in the `shopping.py` to document your design and problem solving
  * *Commit this to GitLab before starting* to write the code
  * This initial design is part of the deliverable of this lab.
  * This design should be your independent work without referencing any outside resources!
    * e.g. Do NOT look this project up on Chegg or similar site, or ask ChatGPT!

* Think about what steps need to be repeated, and look for opportunities to write functions.
* Think about putting your steps into functions to break the problem into more readable and testable chunks.
* Think about the best way to organize your data that you read from files to be used when shopping.
* Dictionaries are your friend.

## Grading

 * In class grading for today (30 points)
   * 10 points: Initial program design written as text comments in 'shopping.py'
     * These comments should show your initial thoughts on program division and possible functions
     * They should highlight plan for incremental development and testing as you go (do NOT try to write whole program)
     * Commit this *before* starting to code
     * You are *NOT* stuck with the initial design; you may modify as you begin and test program
     * This design is required by end of lab period

   * 10 points: At least three significant commits are made during lab class period showing progress and original thought

   * 10 points: Points assigned based on in-class progress at discretion of the instructor based on productive use of time and independent work
     * Note: help from TA and teaching assistant *is* allowed, but no outside help.

 * Final Grading (70 points)
   * 10 points Proper Python style as reported by Pylint test
   * 10 points: Program prints correct total price of items found
     * i.e., correctly calculates the item quantity x price for cheapest store for all found items, and accounts for inflation.

   * 10 points: Program prints the correct store each item was found at for the best price

   * 10 points: Program prints a list of items not found

   * 10 points: Program outputs all-data in neatly-formatted order

   * 10 points: Main program lines are commented thoroughly (At least 5 comments are present in code)

   * 10 points: Proper Git usage with frequent commits and relevant commit messages showing incremental progress at regular intervals
     * A single commit of a significant fraction of solution is not allowed
     * You are expected to make regular commits showing incremental progress
     * Commit messages should be relevant to the task completed and tested
     * Make commits after code changes, and prior to testing, and after significant bug fixes
     * If it's not on GitLab, you were not working on it!
     * We expect at least 1 commit for every 20 minutes of effort.
