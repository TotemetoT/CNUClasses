# Overview

This weekly project will be used to demonstrate several debugging
techniques as we review some CPSC 150 concepts.

During class, follow along with instructor as we demonstrate several
common errors we see, and practice some debugging skills that will
come in handy during this course.

> NOTE: Do NOT work ahead and correct the obvious errors!  Practice debugging with us.

Practice these debugging techniques frequently so you are proficient in using them on the exam.


## Directions

1) When directed, *fork* this project to your personal group
2) Clone the forked project from your *personal* group to your machine using the `gitbash` command line
 * change to your desired target directory
 * create (`mkdir <folder name>`) a folder to hold your CPSC 250 projects if you haven't already
 * change into the course folder (`cd <folder name>`)
 * clone the personal fork (`git clone <copied URL of forked repo>`)
3) Change into the cloned repo `cd w2-150-review-s25`
4) Open the project in `PyCharm Community Edition`
5) Follow along with instructor for exercise 1, 2, 3, and the homework
  * Do not *rush* ahead; work with class and pay attention to issues raised
6) Complete Exercise 3 and the homework problems at home individually.

## Exercise 1

Open `int_calc.py`  it has some style errors on naming convention that we will fix.

Verify the changes to the local repository:
```
git status
git diff
```

Commit the updated test_odd.py that the current code.
```
git commit -am "fixed some style issues with int_calc.py"
```

Then *follow along* with given steps in class, make the same errors as instructor.

Commit as I do.

We will add some unit tests to tests/tests_in_calc.py.
> NOTE: this is one of the few times we will ask you to modify tests.

## Exercise 2

We will write an `is_odd` method in Python.
In Java/C++ you will learn of some subtleties that are not in Python.
However, we will consider some special cases that are not an issue for Java and C++.

We will do this in class, so *DO NOT* rush ahead.  Work with the class.

I have provided a Unit test, but it has some errors.  

We will fix, and add some *corner cases* that we should consider.
DO NOT modify `odd.py` just yet.

First figure out what's wrong with our unit test.  
Programming has an expression *GIGO* - *Garbage In - Garbage Out*.
Here, our unit test is incorrect garbage, which is worse than having no unit test.

Let's fix the existing tests.

Verify the changes to the local repository:
```
git status
git diff
```

Commit the updated test_odd.py that the current code.
```
git commit -am "added unit tests that catch errors in odd.py"
```

Have we tested all of our ``corner cases``?

Let's think of a few, and add those unit tests together.

Verify existing and add additional unit tests that catches all potential errors first.

Verify the changes to the local repository:
```
git status
git diff
```

Commit the updated test_odd.py that fails with the current code.
```
git commit -am "added unit tests for some integer corner cases"
```
At this point, the code should be working, but they are some other cases
we may want to consider.  Let's add those test cases together.

```
git commit -am "added additional corner cases "
git push origin main
```
> NOTE: Here, I specified to use the full `git push origin main`.  
> A simple `git push` will work, but it is good to get in the habit of being explicit
> about what you are pushing to remote.
> In the future courses or projects, you may be working with multiple branches
> and/or multiple remote servers.

Now simplify the code using your knowledge of Boolean conditionals.
Be sure to test against your unit tests.

```
git commit -am "fixed odd.py using Boolean conditionals"
```

## Exercise 3

We will do a bit with lists to illustrate immutable and copying references.

Just follow along and focus on the demo; you will likely need to complete this at home.

## Homework

This is to be done independently.  Do not look at anyone else's code, and
strictly follow empty hands rules for coding. You are encouraged to start early and
contact your professor if you have any questions.

*Most of these are questions that appeared on earlier semester's Exam 1 for 250.*

Similar questions are fair game for your Exam 1.

* `homework.py`

  Inside `homework.py`, you will create 3 functions. The first function should be called `split_emails()` that takes a list of email addresses (ex: christopher.newport.19@cnu.edu) and returns a list of usernames (ex: christopher.newport.19).
  Hint: Use the string `.split()` function.

  The second function will be called `create_email_header()` and you will take a list of usernames (ex: christopher.newport.19) and create a list of greetings. The email greeting should include follow this pattern: "Dear Christopher Newport,"
  Note: You need to capitalize the first letter of the first and last names before creating your email greeting.

  The third function will be called `create_email_addresses()` that will take a list of space separated names (ex: "Christopher Newport") and you will need to return a list of email addresses formatted in the CNU style assuming a 2019 entry year. Christopher Newport's email address would be "christopher.newport.19@cnu.edu"
  Note: You should make sure the first and last names are converted to lower case before making your email addresses.

  *Hint: Use the `.lower()` and `.upper()` to covert between cases and the array slicing syntax works very well on strings.*


* `homework_review.py` y

    You will find 5 functions that are for you to review and write in preparation for the first exam.
    These are based on CPSC150 knowledge, so they really should be review.

    You will need to define some function names, check the tests if you are unsure of exact form.

Again, these homework problems are taken from past Exam 1 questions, and
you should expect similar questions on the Exam 1 coding portion.

## Grading

 Grading will be done in Web-CAT. The tests are provided for you in the tests folder and you can run them locally.

  Due dates can be found on Web-Cat.

  > Warning: Avoid pushing to gitlab after the due date as we accept late work with penalty.
  If you accidentally incur a penalty, let your professor know.

  Look at the test_pylint outputs for coding suggestions and style issues.
  For now we will not be grading you on style in lecture.

  Lab on the other hand ....

### License

This assignment and all associated files are for the private use of students currently
enrolled in the CPSC 250 Lab course at Christopher Newport University.

All associated files are copyright 2025 by Christopher Newport University.
Posting publicly or sharing files is expressly forbidden.
