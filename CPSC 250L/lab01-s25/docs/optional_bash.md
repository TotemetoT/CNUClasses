
## Optional Reading

The following is provided for your edification, but is not something that will be graded in CPSC 250/L.

#### Options
You can find out more about each of the commands above by using `help`.
Type `man pwd` at a Bash prompt (or `help pwd` on Windows Git-Bash).
You should see an explanation of what pwd does.

**NOTE:** Use SPACE to continue to next man page and `q` to quit the manual view.

You should also see the following
* ```pwd: pwd [-LPw]```

The part in the brackets is a list of options.
Some commands have these; some do not.
Options are usually preceded by a single dash,
like `rm -i` above. Use help to find out what the
i option does for rm.  Use help when you are not sure
what a command does.

(**Note: Options are case sensitive in git-bash**)

### Command Line Command Review

To summarize, you can navigate directories in the command line just as you can in File Explorer.

**NOTE:** Because Bash is the same on all machines, the following section will work equally well for Windows git-bash and Mac/Linux terminals.

Do the following:
* Open a git bash shell. This shell puts you in the `Home` directory. You can always tell what directory you are in by typing `pwd`
* Type `pwd` [this stands for Print Working Directory]
* To go down a directory, you use `cd <name of directory>`. For example, to go from the Home directory to the Desktop folder within the Home folder, type `cd ~/Desktop` [cd stands for change directory]
* Type `cd ~/Desktop` to jump from anywhere to the Desktop directory under Home (`~`) folder
* Type `pwd` to see that you are in the Desktop folder
* To go back up to the `Home` directory, type `cd ..` (that is, cd space dot dot then the enter key). that means go up one directory.
*  You can change to a directory that is not one above or one below. Make sure you are in the Desktop directory (type pwd to make sure). Now type `cd ../../../../bin` That means, go up a directory. Then go up another one. Then another one and another one. Then go down the directory named bin.
* Type `pwd` to make sure that you are in the bin directory.
* To go back to your home directory (the `Home` folder), type `cd ~` or `cd` with nothing after it.
Type `pwd` to make sure you are there.

* Other commands that are useful are:
  * `cp <source> <destination>` to copy a file where source is the original file and destination is the file that you are creating. This will overlay *destination* if that file already exists.
  * `rm -i filename` to remove a file (that is `rm space dash i space filename` where filename is the name of the file that you want to remove). Unlike GUIs, once you have removed a file, it is gone forever. There is no trashcan or recycle bin where files deleted from a bash shell are stored. The `-i` (which enables confirmation) asks you if you are sure you want to remove the file. Type y for yes, or anything else to  keep the file.
  * `rmdir dirname` to remove a directory. The directory must be empty to be removed.
  * `mv orig_name new_name` to rename a file from orig_name to new_name. If new_name exists, it will be removed, and the contents of orig_name will be put in a new file named new_name.

### Advanced Study

In CPSC 250, you will only need the basic bash commands we cover in lab.  But, there are a lot more useful commands available.

For more information and future study, see :
* [top 25 bash commands](https://www.educative.io/blog/bash-shell-command-cheat-sheet)
* [101 bash commands](https://dev.to/awwsmm/101-bash-commands-and-tips-for-beginners-to-experts-30je)
* [UW Bash Reference](https://courses.cs.washington.edu/courses/cse390a/14au/bash.html)

You can also write *shell scripts* that are programs to do common file operations.
* https://devhints.io/bash

Shell scripting is **well** beyond the scope of CPSC 250, but you should add shell scripting to your repertoire before you graduate!  

---------
