# Lab 1 - Part 2<br>Git-based Source Code Management and Workflow

This project modifies the simple hello world example as we demonstrate the workflow and tool chain that we will use in lecture and lab this semester.  

Learning these tools is part of your professional development, and is required for this course; you are expected to master this workflow.

The required tools are installed on the lab machines.
For setup directions for your personal machine, see [Toolchain Setup](./toolchain_setup.md).


This lab assignment duplicates the `w1` project from lecture.  There is minimal coding involved, so write the code independently.  

**DO NOT COPY FILES/CODE FROM ONE PROJECT TO THE OTHER!**

Follow the provided *Workflow Slides*, just substitute `lab01-semesterYear` for `w1-hello-world-semesterYear`,
and get project from your lab group.

****
GitLab Setup
====

We have created a personal Gitlab group for you to use in this class following the `firstname.lastname.yy-cpsc250-semesterYear` convention.  
Your lecture and lab instructors are members of this group, and can view all of your projects in this group.  
You are required to use this group for all assignments in the course.

Be sure to update your `WCUSER` and `WCPASS` variables on your personal `firstname.lastname.yy-cpsc250-semesterYear` **group**
so that your code is submitted to WebCat with your user ID and password.  
See the lecture slides for details on updating these variables.

> NOTE: Be sure to NOT hit return after text;
> WCUSER/WCPASS must be single lines only!

**Do this now.**

Doing this once for the **group** will work for all projects submitted to this group for both lecture and lab.
It is your responsibility to verify that your code is on WebCat and successfully passed the required tests.

If you change your password on WebCAT in the future, then be sure to update the `WCPASS` variable for your group.  


Projects in CPSC 250 will have common structure.
```
cpsc250-<project ID>
|-src   (source files that you will modify)
|-tests  (provided unit test files that you should NOT modify)
|-given (optional folder for instructor provided code - do NOT modify)
|-exam (optional folder with exam specific information - do NOT modify)
|-docs (optional folder for instructions and documentation)
|-img (optional folder for images used in README and documents)
```

All of your changes should be to files in the `src` folder; **do NOT modify or move files in the other folders.**

****
Setting up the project
====

Fork this repository into your personal group (with name of the form `firstname.lastname.yy-cpsc250-semesterYear`).
After the fork completes, you will be at a repository in that group.
Check the URL for your group name to verify.

Once the fork is
done, select the `Clone` dropdown menu, and click the double file button to right of URL (web) address under `Clone with HTTPS`.  See the Workflow slides if you have doubts; ask instructor if you need help.

Clicking the icon copies the entire address into the computer *clipboard* memory.
Open up a Bash shell, `cd` into your
`cs250L` directory created in Part 1 of this lab.
Use `pwd` to verify that you are in the correct directory.

> NOTE: This assumes a Bash terminal is installed.  See the tool chain setup directions for installing the necessary software on your personal machine (e.g. GitBash for Windows)

> NOTE: Recall the shortcut to your home directory is (with tilde mark):
```
cd ~
```

Before we begin using git commands in our terminal, lets first define the four fundamental commands of git. These are:

* `git clone <url>` - The git clone command takes a URL (either internet or local path) and clones or copies all of the files in the git repository to a new folder in the current working directory.

* `git add <file>` - The git add command takes a file or files and prepares them for the next git commit (explained next). We use this command to tell git which files that we have changed and want to add to take a snapshot of. You can visualize this process as git taking the file or files and putting them into an open box that is being prepped to be stored or sent somewhere. Generally as developers we want to add all of the files that we have changed, so it is common to use the command `git add *` to tell git to add all of the changed files to the prepped box.

* `git commit -m "<your commit message>"` - The git commit command takes all of the added files (from the `git add` command) and stores a snapshot of the current code base with the new changes. We use this command to save a snapshot of the code at this current time. Imagine a word document you have been writing for your English class, where instead of your paper being overwritten with the latest stuff you've typed, its a running series of saves of your text from every time you've hit the save button. You can visualize this step as taking the box from the `git add` and sealing it, keeping a perfect copy of the code at that point in time. We use this command so we have a snapshot history of our code as the code develops.
As a short cut, you can combine  `git add` and `git commit` for previously tracked files by using `git commit -am <commit message>`.  This automatically adds *all* modified files, and commits them.

  > Note: If you fail to use the `- m` option, git will open a default editor for you to type your commit message.  The editor varies by machine, but the default uses a *vim*-like interface that requires you to `esc-w-q` to write and quit the editor.  Use this `-m` option and type your message to avoid this complexity.  See your instructor if you get confused by the editor.

* `git push <repository> <branch>` - The git push command takes all of the commits only the local machine and *pushes* them to the repository and branch specified. It will be most common in this class that you will want to push your code to the remote repository on GitLab, so the command to do that is `git push origin main`. The *origin* stands for the repository you originally cloned from (your forked GitLab repository) and the *main* stands for the branch your working on. We will most likely be working on the main branch of our projects.

 > NOTE: For our lab set up, you can just `git push` which defaults to `git push origin main`.  For more complicated branching and remote setups, you should get in the habit of specifying what branch and where you are pushing it to.

Git needs to know who to give credit to when you make a commit; therefore, we need to set our Git *credentials*.  From the GitBash shell, type:
```
git config --global user.name "Full Name"
git config --global user.email "first.last.yy@cnu.edu"
```
replacing `Full Name` and `first.last.yy` with your personal info.

**NOTE: Pay attention to the quote marks around the text.**

  > NOTE: You will need to set these credentials every time you log into a new a lab machine.  
  > You only need to do this once on your personal machine.

On Lab Windows machines, git will use the built in Windows `Credential Manager`.  If you mis-type your password, you need to hit the Windows start button and type "cred" and the credential manager should pop up.  Click on it, find the gitlab setup, and "remove" to reset your password.

On Mac machines, the `osxkeychain` can be used.  Google is your friend to help set up on personal machine.

For Linux machines, add
```
git config --global credential.helper "cache --timeout=1800"
```
The `credential.helper cache` saves you from repeatedly needing to type your password for multiple *pushes* to the remote. The 1800 is seconds, which corresponds to a half hour.  Be sure to log out from your machines after you are finished coding and pushing your commits to GitLab.

After configuring your git user information, we are ready to clone our project.

From your designated `cs250l` folder, type  `git clone ` followed by a SPACE and *PASTE* the URL of your forked repository.
Different machines have different commands for `PASTE`; most often `Ctrl-v (Windows)`, (`Command-v` on Mac), `Ctrl-Shift-Insert` on Ubuntu, or Right click and select `Paste` from menu.

Before pressing enter, ensure that *your personal group name* is in that URL.   
If it is, press enter.

> NOTE: A common error is for students to forget to *fork* and clone the project from the student distribution group.
> If this happens all is not lost, you can `git remote add mine <URL>`.  This adds an additional Git remote called `mine` in addition to the default `origin`.
> Just remember to substitute `git push mine main` where you see `origin` in the below commands.  
> Fork first and avoid this complexity!


If you're on the lab machines
you will be prompted to enter your Gitlab credentials, if you're on your own computer you may be asked to provide
credentials.

If the clone fails, *read the error message carefully* and try again.
* If the Gitlab remote is unreachable on lab machines, you may need to reboot the lab laptop.
* On Windows machines, you may need to reset the Credential Manager if your login credentials changed or were entered incorrectly.  
> NOTE: To reset credentials on Windows, hit Windows button, and type `Creden` and you should see the `Credential Manager` application pop up.  Select it, select `Windows Credentials` and remove the credential associated with Git.


If it fails to clone after 3 tries, *immediately* ask your instructor for assistance.


Once the clone succeeds, `cd` into the cloned directory.
 * `cd la<TAB>` should work for this first labs

Use `pwd` to determine the full path to this repo, and use `ls -altr` to view the contents of the folder.

 > NOTE: A common error is to forget to `cd` *into* the cloned project folder.
 > Git commands will not work until you are *inside* the project folder!

** Add requested information to your form to show your progress.**


****
PyCharm
====

PyCharm is an *Integrated Development Environment* (IDE) for Python.  

Start the PyCharm IDE; the main page will start at the project selection menu.

Select `Open Project` and browse to the folder where you just cloned the repo.

> NOTE: Always `Open` the cloned repo folder.  
> Do NOT copy files around because you are editing in a different folder than your git repo.
> Do NOT create a `New` project; always `Open` in CPSC 250.
> Always open an individual project, NOT the `cs250l` folder containing all projects.

In order to consistently run our unit tests in PyCharm and on GitLab/WebCat,
we need to make a change to the PyCharm configuration for our project.

The Run configuration must set the *Sources Root* folder to the *project Root* .

Do this by right clicking on the project name (e.g. `lab01-s24` in this case), and select
`Mark Directory as` and `Sources Root` as shown in

Also you need to set the Run configuration.
See the *Workflow slides* for setting the "Configuration Templates" correctly.

If you do this at the beginning all tests should work correctly.

> NOTE: The Edu edition of PyCharm requires jumping through some hoops to
> expose the `Run` menu required to set the Working directory.  
> Using the `Community Edition` simplifies our life.

We are now ready to start coding.

****
Project Coding Exercises
====

### Exercise 1

Modify the simple print statement in `hello_world.py`.

First create a method called `say_hello()` that returns the string "Hello World!".
```python
def say_hello():
    """
        Specify a string
        @return string
    """

    return "Hello World!"

```
This basic method just defines a string.  This example includes a doc string to provide a description of the method.

Call this method from within the script.
```python
print(say_hello())
```
For now, your file should only have the `say_hello()` method and the single `print` command.

Right click on the `hello_world.py` file and select `Run hello_world`.
You should see the string printed to the console window that is part of PyCharm.

Open a terminal with current directory corresponding to the project, and `cd src` to change into the source folder.
Run `python hello_world.py` from the command line.  Again you should see the `Hello World!` output.

Now, again from PyCharm, right click on the `hello_world_test.py` and run the unit tests.
This will verify that the method is named correctly, and the output is exactly as specified.

After debugging and completing the last change for this exercise, open a (GitBash) terminal, change to the project folder,
and verify the changed file:
```
git status
```
 > NOTE: If this gives an error, likely you are not inside the cloned project folder.  Use `pwd` to confirm, and `cd cpsc<TAB>` (using TAB completion) or `cd cpsc250l-lab01` to get into the proper cloned folder.


View the changes:
```
git diff
```

Doing the `status` and `diff` checks is optional, but is helpful to verify that you are making changes in the correct folder.

Commit the changes to the local repository:
```
git commit -am "implemented say_hello"
```
This commits *a*ll changes to tracked files, and adds the *m*essage in quotes.
This `commit` command records your changes to your *LOCAL* repository on your current machine.

You are free to make additional commits, but be sure to include this commit.

Push your committed changes from your local repo to the remote repository on our PCSE Gitlab server.
```
git push origin main
```
The `push` command records your *commits* from your local repo to the remote server.

The remote server is named "origin" by default, and "main" is the default branch name.  
For now, we will stick with these default branch names.  


Be sure to make at least one commit and one push *EVERY* time you work on coding; **if you aren't committing and pushing, then you aren't working on code in CPSC 250.**
If it is not on GitLab, it didn't happen!

 >  NOTE: Verify commit made to Gitlab by clicking on the project name
 > in the Gitlab window, and making sure you see your commit message!




### Exercise 2

Import `hello_world.py` into  the `say_it.py` script, and call the `say_hello` method inside a print statement.

```python
import hello_world
print(hello_world.say_hello())
```


Now run the `say_it.py` script from within PyCharm, *AND* from the command line as above.
You should see `Hello World!` printed twice!

By default, scripts run when imported into another script.
Modify the `hello_world.py` script to use the `main` construct so that "hello world" is only printed once.

```python
if __name__ == '__main__':

    print(say_hello())


```
This change only runs the print command if the script is executed as `main`, which is not the case when it is imported into another script.

Now re-run the `say_it.py` script in PyCharm *AND* on the comand line;
you should only see one `Hello World!` on the screen each place.

Now run the `say_it_test.py` unit test.

After verifying the correctness,
```
git commit -am "called say_hello from say_it.py"
```
You are free to make additional commits, but be sure to include this commit.

Push your changes to the remote server.
```
git push origin main
```

Again, click on the Gitlab project name to return to refresh main project page, and verify your commit is there.

****
GitLab Continuous Integration
====

Each project contains a ```.gitlab-ci.yml``` file that specifies code that is automatically executed on the Gitlab server with each push.  This may include unit tests and the code that automatically uploads the modified files to WebCat for grading.

This file starts with a ``.`` which means that it is hidden from the file browser by default.

**You should NOT modify  this file.**

Go to the project webpage on your forked repo, and view the status report for the tests.   
(See lecture notes for detailed instructions.)

Verify that the code was automatically uploaded to WebCat.  
The most common problem is issues with the ``WCUSER`` and ``WCPASS`` variables set for your personal GitLab *GROUP*.

After setting the `WCUSER` and `WCPASS` variables, you will need to re-trigger the WebCat submission task as shown in the lecture notes.

From now on, for any project on your personal group, every push to GitLab will automatically submit to WebCat.

Once you complete this lab, you should add *Source code management (Git)* on your resume!
You're a beginner, but at least you know your way around `git clone, git add, git commit, and git push`.
That's more than many.

****
WebCat Automated Grader
====

Your grade is determined by WebCat based on unit tests.  For most cases, these are the same unit tests distributed with each project.  In some cases, additional tests may be executed by WebCat.
Your code must be individually submitted to WebCat for credit.  

Verify that your code reached WebCat by logging into WebCat directly and viewing your score as shown in the lecture notes.

See your instructor immediately if you are having issues with WebCat.

You need to refresh the WebCAT page by clicking "Home" at the top menu of the WebCAT page.  Refreshing an existing results page will *NOT* grab the latest results.  Refresh by first clicking "Home".


### Git Notes

* If you do your work on different machines, you will need to get in the habit of doing a `git pull` at the start of every session.

> When you first clone a project this is not necessary, but once you are set up on different machines, you need to `git pull` to get your local repo up to date *BEFORE* making changes.
> Otherwise, you will not be able to push to GitLab. If you `git pull` after making changes, you may get *merge conflicts* that must be cleaned up.
> See your instructor for assistance if this happens to you.
