# Lab 1 Part 1 <br> Introduction to File/Directory Structure and Bash Command Line Interface in Ubuntu Linux

## Logging On

You are required to do this lab on the PCSE lab machines in your classroom.
Login using your CNU email address (first.last.yy@cnu.edu) and your CNU password (e.g. what you use to log into Scholar/GMail).

**NOTE:** *PCSE* is an abbreviation for the *Physics, Computer Science and Engineering* department.

These machines use the Ubuntu (Linux) Operating System (OS), which may be new to most of you.
Follow the provided *Ubuntu Intro* slides for logging in and opening your first `terminal` session.

During lab this semester, we want you to use these machines to get experience with Linux.

> Note: For Spring 23, some labs will be held in Luter 109, which will have Windows machines.
> For lab, do all of the terminal work in the Windows "GitBash" prompt, except run
> Python from the "Conda Prompt" (just use Windows search bar) to open.
> You will be using Linux machines during lecture, and are required to use them during Exams.

You may use your personal machines at home to complete the labs, but use lab machines during all labs.
The machines in Hunter Creech also have Ubuntu on them so you can get more practice with Ubuntu.

## Files and Directories

Computers use *files* to store data, and *directories* (also called *folders*) to organize files.  
Some files contain simple human readable text, some *binary* computer readable data, and yet others contain executable *application* code.  
Directories can hold other directories, call sub-directories, as well as files.

Your files, (sub-)directories,
and application programs are in a hierarchical *file system*.

For example, to see what `Files` (and folders) are in your ``home`` directory in Linux,
select the folder icon on the favorites bar to the left side of screen.

  > NOTE: If you hover the mouse pointer over the icon, it will say `Files`.

  ![File Explorer Launch Icon][img/01_files_icon.png]

  ![File Explorer GUI][img/02_file_explorer.png]

** Do this now.**

You should see several graphical *folder* icons, analogous to a folder in a file cabinet;
in everyday usage, people use the term *folder* and *directory* interchangeably.

This `File Explorer` is an *interface* that lets users interact with their computers.
Most people who use computers use Graphical User Interfaces (GUIs) to navigate their computer.
On Windows this is known as the `File Manager` or  `File Explorer`.

File Explorer is the GUI that lets you view where a file is.
You can open most of the files in File Explorer by moving your mouse to them,
and double clicking on them (press and release left mouse button quickly
  two times for double click).
Most novice users interface with their computer using GUIs such as File Explorer.

**Now click on `Documents` icon in the Files window.**

You should see a list of the files in your `Documents` folder.  
At this point, it is likely empty.

**NOTE:** As you go along, please initial the appropriate line on the provided form to keep track of your progress.

Now go back to your user `Home` directory
in File Explorer by choosing "Home" left pane of the Files window.

**Go to the home directory now.**
Make note of your progress on the provided form.


 After clicking `Home` you should again see the above image again.

 **Now click on `Desktop` icon in the Files window.**

 You should see a list of the files and folders that appear on your Desktop.
 At this point, it is also likely empty.

 Make note of your progress on the provided form.

## Graphical User Interfaces (GUIs) vs. Command Line Interfaces (CLIs)

In contrast to the GUI, we will use a Command Line Interface (CLI),
also called a *shell* or *terminal* much of the semester.
CLIs are available on all operating systems including
Windows, MAC OS, and Linux,
and are often available when GUIs are not an option.  
For example, many servers or embedded systems do not have monitors attached;
 the only access is via a network interface to a CLI.

Different operating systems use different commands for their CLI.  
The lab machines with Ubuntu Operating System uses *Bash* commands, which are
standard on MAC OS and Linux.  
If you are curious, see https://en.wikipedia.org/wiki/Bash_(Unix_shell) for more information (Optional reading - not required!).

To avoid learning different commands, we will make use of the ``GitBash`` CLI on Windows for your personal machines.
Later we will provide directions for installing GitBash on your personal Windows machine,
but for now use the lab machines where Bash is the default installed terminal.

Some terms to know moving forward are:

* **Working directory** - This term refers to the directory (or folder)
that our commands are relevant to.  
If one does not specify a directory for a command to use, generally the current *working directory* is assumed.
You can visualize this term as when you open your file explorer,
and click into the Desktop icon.
It will list the folders and files currently contained in the Desktop folder,
so the current working directory is now the Desktop folder.

* **ANY OTHER USEFUL TERMS TO KNOW**

To start, click the dots icon in lower left side of Ubuntu screen and type `term` in the search bar at top.  You should see the `terminal` icon; select this.

> NOTE: Refer to the `Ubuntu Intro` slides posted on Scholar for images of this process.


> NOTE: On Windows, you would press the Windows key, and type "Git Bash" in the search prompt,
and choose Git Bash Shell.

The terminal (git-bash) command brings up a window that is called a Bash shell
(a "shell" is another name for the Command Line Interface).
You can create the same type of window on a Mac by choosing Terminal from Spotlight Search (press command-space then type "Terminal" then press the Enter (or Return) key).
Terminal in Mac is a Bash shell.  

We will go over the most common commands that you will use in this shell,
but you can always *Google* these bash commands because bash shells are common.

Here is a summary of the 4 fundamental bash commands you will use in this course:

* `pwd` - Stands for *print working directory*.
  * This command prints out the **full path** to your current working directory.
  * Use the Enter/Return key at the end of each command to execute
    * Some keyboards say "Enter", some say "Return", and some use an angled arrow for Enter/Return key
  Under MAC OS/Linux/Bash terminals, directory names are delimited with a forward slash `/`;
   under Windows, directory names are delimited with a back slash `\`.
  For the curious, see [this article](https://www.howtogeek.com/181774/why-windows-uses-backslashes-and-everything-else-uses-forward-slashes/) .

* `ls`
  * To be clear, this is a lower-case "ell-ess"
  * The `ls` command lists all of the current files and directories contained in your working directory.
  * `ls -altr` is a common option for listing all files including hidden ones, in list format, by date/time in reverse order.
  * Optional: Run the `man ls` command in terminal to see more options.
    * Press `spacebar` to show subsequent pages
    * Press `q` to quit man page.


* `cd` - Stands for change directory.
  * This command allows the user to navigate the file system tree. You can change directories by typing in the prompt `cd <directory>`
  * Try it now from your Home directory `cd Documents`.
* Verify your current working directory using the *print working directory* command `pwd`
  * You should see `/home/<YOUR USERNAME>/Documents`in the Bash terminal after the `pwd`
  * Don't forget to document progress on your worksheet.

* Return to your Home directory using the ``~`` (tilde) shortcut
  * `cd ~`
  * `pwd` should show the full path
  * Using `cd ~` brings you back Home from any folder on computer

* Now change to your Desktop folder
  * Note that the terminal prompt will indicate `~/Desktop` where ``~`` is the shorthand for the true full path to your Home folder.
  * Document progress on your worksheet.

* `mkdir` - Stands for make directory.
  * This is similar to right clicking and selecting ``new folder`` in the file explorer gui.
  This command will make a new directory given a name in the current working directory.
  For example, `mkdir cpsc250l` will make a new folder in the current working directory called `cs250l`.
  * Note: If you prefer, you can create your `cs250l` folder in Documents or Home
    * Just remember where you created it.

**NOTE:** The term *folder* and *directory* are often used interchangeably.
There *IS* a technical distinction and *directory* is the proper term for a hierarchical file system.  See https://en.wikipedia.org/wiki/Directory_(computing) for more information.
We will follow the colloquial use an use both terms ("folder" is quicker to type!).

* Use `ls` in the terminal, which should show the new cs250l directory in terminal
* Use the `Files` GUI, and navigate to the same current working directory.

You should see the same directory/folder listed in both.

* Now use the command `ls -altr`
  * to list all files (including hidden ones) in a detailed (long) form in order of modified date.  
  * Optional details: [Web linuxize.com/post](https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-command/)
  * Note that three directories are shown : `.`, `..`, `cs250l`
    * Assuming nothing created prior to this lab.
    * The single dot (`.`) is short hand for the current directory
    * The double dot (`..`) is short hand for the "parent" directory above this directory  
      * E.g., if you're in '~/Desktop', then `..` refers to the Home directory (`~`)
      * So `cd ..` with take you "up" one directory in the hierarchy
      * Do a `pwd`, then `cd ..`, and a second`pwd` to confirm.
        * Do this now, and initial your worksheet

Use the command `pwd` to *print working directory* to show the full path of the current directory.  

* Now, `cd /` to change to the "root" directory
  * Do a `pwd` to confirm

  > NOTE: Files/directories are stored according to a *tree* structure starting from the *root* node.
  In computer science, we normally view "trees" upside down with the root on top, and *leaf* nodes on bottom!

  * `ls` to see contents of root directory
    * Which should be similar to:

    ![picture of Ubuntu file hierarchy - https://askubuntu.com/tags/filesystem/info][img/lxf95-feat_filesystem-diagram.png]

  * Do `ls etc` to see contents of `/etc` folder
  * Do `ls -altr /etc`

  > NOTE: If a directory name starts with `/` it is an *absolute* path relative to the root folder.
  > If it starts with some other character, then it is *relative* to the current working directory.
  > In the above example, there is no difference because you are in the root directory.

  * Navigate back to Home directory step-by-step using *relative* directory names starting in root
    * `cd home` then `pwd` to confirm (but note, that the path is shown in prompt and window title as well)
    * `cd 0XXX` where XXX is next 3 digits of your user ID then hit Tab key
      * If you are only user with those first four digits it will auto complete your home folder
      * If multiple users have same, you might have to add some characters before TAB completes
      * Hit Enter/Return after name completes to the `@cnuadmin.cnu.edu` part
      * *Learn to use TAB complete!*
      * `pwd` and `ls` to confirm you are in your
    * `cd Desk<TAB>/cs250l`
      * Where `<TAB>` denotes Tab key, followed by `/cs250l` before hitting Enter
      * Use `pwd` to verify that you are back in your project folder for lab class
    * Initial worksheet to document progress  

You should have navigated the file structure via command line just as you did before using the File Explorer GUI.


**NOTE:** Although Windows does not care if you type "Documents/documents", or "desktop/DEsKToP" for the Desktop folder, most operating systems (including Mac and Linux) and most programming languages (including Python) will care.
They are **case-sensitive** meaning that UPPERCASE letters and lowercase letters are completely different.
In case sensitive operating systems,  you could have two files, one named a.txt, and other named A.txt,
and they could store completely different information,
and they would be unrelated to each other.
Windows ignores case in file and directory names,
but you should get used to paying attention to
whether a letter is UPPERCASE or lowercase.


#### Shortcuts
Wow! That is a lot of typing. There are two shortcuts that you should use a great deal in the bash shell:

First, bash shells allow you to use the TAB key for file completion as described above.

  **NOTE:** If there other files or directories with same starting characters, then hitting TAB again will show a list of the possible options.  Just continue typing letters to *disambiguate* the name, then hit TAB to complete.

Second, Bash shell remembers your previous commands.
Type the UP arrow to see what your previous command was.
Tap the Enter/Return key, and Bash will execute your command again.
Or, type the UP arrow key twice to see the two commands before.
Type the DOWN arrow to go to back.  
Using UP and DOWN arrays can help you quickly retrieve prior commands that you want to repeat.

**Make frequent use of the TAB File completion and UP/DOWN arrow command recall whenever you are in the bash shell.  
It will save you much time!**.

Once you complete this lab, you should add *Linux (Ubuntu)* on your resume!
You're a beginner, but at least you know your way around file structure, and have learned some Bash basics.
That's more than many.

## Questions to answer (on form)

1. What is another name for the CLI?
2. What is the full path to the `Desktop` directory? (as given in Bash terminal)
3. What command do you use to back up one directory?
4. What is the full path to the directory above `Desktop`?



## Optional Reading

The following is not part of the lab, but if provided to give you pointers for advanced learning.  This is material you need to develop as part of your computing skill set before your graduate, regardless of your major.

[Optional Reading](optional_bash.md)


**Use your browser back button to return to the main README.**
---------

[bashpic]: ../img/git_pic.png
[folderstructure]: ../img/folder_structure.png
