# Overview

This weekly project will be used to demonstrate working with lists and dictionaries.

During class, follow along with instructor as we demonstrate several
common errors we see, and practice some debugging skills that will
come in handy during this course.

> NOTE: Do NOT work ahead and correct the obvious errors!

Practice these debugging techniques frequently so you are proficient in using them on the exam.


## Directions

1) When directed, *fork* this project to your personal group
2) Clone the forked project from your *personal* group to your machine using the `gitbash` command line or terminal
 * change to your desired target directory
 * create (`mkdir <folder name>`) a folder to hold your CPSC 250 projects if you haven't already
 * change into the course folder (`cd <folder name>`)
 * clone the personal fork (`git clone <copied URL of forked repo>`)
3) Change into the cloned repo `cd w3-lists-review-s25`
4) Open the project in `PyCharm Community Edition`
5) Follow along with instructor for the exercises.
  * Do not *rush* ahead; work with class and pay attention to issues raised
6) Complete the homework problems at home individually.


## Demonstration Code

The two files in `/given` folder do NOT require modification, but are provided as a demonstration.
We will review some in class, but you should carefully review at home.  Make sure you understand each step.

## In-class Exercise

We will do a bit with lists in `list_methods.py` to illustrate differences between append, and
extend, along with some list slicing practice.

Just follow along and focus on the demo; you will likely need to complete this at home.


## Homework

This is to be done independently.  Do not look at anyone else's code, and
strictly follow empty hands rules for coding. You are encouraged to start early and
contact your professor if you have any questions.


* `homework.py`

  Inside `homework.py`, you will one function to "Intermingle Lists" given two lists.

  So given [1, 2, 3] and [A, B, C], you generate a *new* list that contains [1, A, 2, B, 3, C].

  Your code should be able to handle the case where one list is shorter.
  If either list is not defined (e.g., the argument is `None`), then
  return the other list or None if both are None.

  See the defined unit tests for more information.

## Grading

  Web-Cat will be used for grading correctness and checking for timely submissions.
  Sometimes we add additional tests on Web-Cat that are not distributed.
  Check Web-Cat.

  Due dates can be found on Web-Cat.

  > Warning: Avoid pushing to gitlab after the due date as we accept late work with penalty.
  If you accidentally incur a penalty, let your professor know.

  Look at the test_pylint outputs for coding suggestions and style issues.

### License

This assignment and all associated files are for the private use of students currently
enrolled in the CPSC 250 Lecture and Lab course at Christopher Newport University.

All associated files are copyright 2025 by Christopher Newport University.
Posting publicly or sharing files is expressly forbidden.
