# Using multiple machines

If you use different machines, then you will need to use the `git pull` command when you switch roles.  First ensure that you have both cloned the owner's repository.  Then whenever you and your partner are about to switch off, perform an __add__, __commit__, __push__ cycle on the code from partner A's machine. Then from partner B's machine perform `git pull` to download the changes.  Partner B is free to work before doing their own __add, commit, push__ cycle, followed by Partner A pulling.

#### Resolving conflicts
From time to time, you may encounter a situation where you are unable to push because there are changes on the remote that are not on your local copy.
You must first __git pull__ to get the remote changes, but this may result in a merge conflict. In order to resolve this, you will need to edit the files to manually remove the offending code.

To avoid the potential for conflicts, just use one machine and switch git configuration information as described [here](switch.md)

[Go back to the main lab](../README.md)