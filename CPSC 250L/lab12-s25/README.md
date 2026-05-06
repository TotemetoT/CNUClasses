# Lab 12 - Tkinter Paint Program

For this lab, you will be given overall requirements, but you must come up with intermediate steps yourself.

Read this README carefully before starting.

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
* https://docs.python.org/3/library/tkinter.html - Tkinter documentation

> You are expected to show incremental progress throughout the lab.
> Accessing prior semester solutions of your own or anyone else's, including online tutoring sites such as
> (but not limited to) Chegg, Docsity, StackOverflow, ChatGPT or other is strictly
> forbidden and warrants a CHECS referral.
>
> Reference to StackOverflow for general questions (e.g. how to format a string) is allowed.
>
> You are only allowed to have general discussions (e.g. how to format a string) under empty hands rules.
> The design and implementation should be your own work.

## Instructions

In this file we will create a GUI that will emulate a paint program (similar to MS Paint).  The GUI will have a canvas that will be used to draw on.
* The base requirements for this program are
  * Ability to draw with different brush sizes (at least 3 sizes)
  * Ability to change brush color (at least 3 colors)
  * Ability to clear the canvas
  * Note: Style will be included in the grading (e.g. not a single column of widgets)
* Challenge Tasks
  * A reasonable file menu with the following options as an example:
    * New
    * Save
    * Save As
    * Exit
  * Ability to draw with a brush of your choice (e.g. circle, square, etc.)
  * Brush size should be adjustable with a slider or with visual indication of size (not just buttons with text)
  * Ability to save your drawing in a file (png)
    * Hint: You may need to use the `PIL` library for this
    * Hint: You may need to use the `tkinter.filedialog` library for this
  * Ability to choose any color from a color picker
    * Hint: You may need to use the `tkinter.colorchooser` library for this

You will find an example in `paint_example.py`. Create a new file called `paint.py` and start from there.
  
    
## Grading

 * In class grading for today (40 points)
   * 20 points: Initial program design written as text comments in your python file
     * These comments should show your initial thoughts on program division and possible functions
     * They should highlight plan for incremental development and testing as you go (do NOT try to write whole program)
     * Commit this *before* starting to code
     * You are *NOT* stuck with the initial design; you may modify as you begin and test program
     * This design is required by end of lab period
   * 10 points: At least three significant commits are made during lab class period showing progress and original thought
   * 10 points: Points assigned based on in-class progress at discretion of the instructor based on productive use of time

 * Final Grading (60 points)
   * 25 points: Program is functional and meets all requirements listed above
     * This includes having a subjectively reasonable layout (e.g. not a single column of widgets. Up to lab instructor's discretion)
   * 20 points: The challenge tasks are completed. 5 points per task above (This can exceed 20 points if you complete more than 4 tasks)
   * 5 points: Main program lines are commented thoroughly (At least 5 comments are present in code (not the ones I have already written in the example code)
   * 10 points: Proper Git usage with frequent commits and relevant commit messages showing incremental progress at regular intervals
     * A single commit of a significant fraction of solution is not allowed
     * You are expected to make regular commits showing incremental progress
     * Commit messages should be relevant to the task completed and tested
     * Make commits after code changes, and prior to testing, and after significant bug fixes
     * If it's not on GitLab, you were not working on it!
