## Pair programming

We will be using pair programming in this lab for *all* remaining labs.  

[Introductory Video](https://www.youtube.com/watch?v=rG_U12uqRhE)

[Introductory Article](https://www.infoq.com/articles/introducing-pair-programming/)

Your instructor will assign you a partner for the duration of the lab.
You will work with this person to complete the lab, ___NO EXCEPTIONS! 40% of your lab grades will be based on participation with your partner!___

You are expected to complete the work __during__ the class period, therefore, your attendance is required each and every week.  Notify your instructor ASAP if you will miss any class period; unexcused absences will lose all participation points for that week.

Roles:
* **Navigator** - responsible for thinking about what needs to be done, the logic of the code, and looking ahead for trouble
* **Driver** - focused on mechanics of entering the code (e.g. typing and syntax)

The navigator is the one "directing" the development, and must verbally communicate with the driver.  For example, the navigator may say "Use an if statement to check that the result equals the expected value", and the driver will type:
```python
if result == expected:
```

You should switch roles often during each programming session, and be sure to have a Git commit whenever you switch.

In general, partners should have on a similar abilities at this stage for the learning to be most effective.
Your lab instructor will assign your partner for each lab;
 these partners will likely rotate during the year.
If there are any issues that would cause conflict with a particular partner,
please discreetly notify your instructor.

You are required to be present during the lab period and remain until the lab is completed;
if the lab is not completed during the period then you are responsible for making
plans to meet with your partner outside of class to complete.  
Schedule before leaving the lab, and notify your instructor of your plans.

The expectation is that each partner will have at least __3, non-trivial, non-sequential__
commits to Git by the end of this lab.  
A failure to have the proper commits is a failure of __BOTH__ partners.

Make a commit when you define a method signature (i.e. the `def` statement) and doc-string.
Just put `pass` in the method body.  
Alternate doing one method signature each, and commit after each one.

Then at least one commit per completed method.

> Note: Partners may have additional sequential commits if necessary.
> This practice is encouraged as committing often is a good Git practice.

We discuss the mechanics of switching Driver roles later in this writeup.

To simplify collaboration, it is best if you use one of the lab computers.  You are required to use these on in-class quizzes and lecture exams, so practice is good.  These computers already have the proper environment set up for your.

If your personal machine is already set up, you may with partners agreement choose to use a personal machine during lab.

### Forking

Choose one of the partners to be the the initial *owner* of the project.  The owner will perform the inital forking of the project.

1. Navigate to the top of this project page, once there you will see the fork button. ![Fork](/img/gitlab_fork.png)
2. Once you select "Fork", you will see a list of your groups. Select the following group: first.last.yy-cpsc250-s20 (where first is the owner's first name, last is their last name, and yy is their CNU entry year).
  * This is the personal group for all CPSC 250 related projects for both lab and lecture.
3. GitLab will automatically fork the project.
  * After the forking process is complete you will be redirected to the project page.
4. Once you are in your group, you can clone the project.
  > ___NOTE: You need to clone the repository from YOUR group, NOT the repository you were given at the start of class. You will only be able to commit to your personal repository.___

  > A common error is to forget to *fork* and clone the project from the student distribution group.  __ DO NOT DO THIS!__ However, if this happens all is not lost.

  > You can `git remote add mine <PERSONAL URL>`. This adds an additional remote called `mine` in addition to the default `origin`.
 Just remember to substitute `mine` where you see `origin` in the below commands.


### Code Collaboration

Both partners need to access the repo, so the owner of this repository should make their partner a `Maintainer` on the *project* in GitLab.

> NOTE: Do this on the project, and not your group!

In order to do this navigate to the Members Page of the project:

![](/img/members_page.png)

Type the `first.last.yy` of your partner in the *Select members to invite* box, and select your partner, then choose `Maintainer` as their permision level.

> ___Note: Do NOT add your partner to your group, only add them to your PROJECT.
> Adding someone to your group gives them the ability to view other projects you may be working on.
> This *IS* an HONOR CODE VIOLATION.
> If you have any questions or are unsure, please ask your instructor.___


### Cloning
As of now your project is located in the "cloud" (or rather the PCSE GitLab Server). You will need to create a local copy of this project repository on you local machine before you can start working on it. Git is what is known as a
Distributed VCS, meaning that it does not have a centralized repository, rather, every repository is a __clone__ of the remote repository. You will "checkout" this project with the `git clone` command.

#### Switching Roles

It is advised that you and your partner use a common machine in lab.
This will simplify your process, and minimize the chance of having merge conflicts.  

To simplify managing your Git configuration that is used to track who commits what, we have provided a simple python script called `switch.py` in the project root folder.

Edit this file to contain the proper partner names and emails as Driver 0 and Driver 1 (remember in CS we count from 0).  Then, run this script whenever you new to change drivers:
```python
python switch.py
```
Now when you make a commit, the credit will be given properly.

See [Switching Git Configuration](docs/switch.md) for more information.


If you want to use multiple machines follow
[this guide](/docs/multiple_machines.md).
