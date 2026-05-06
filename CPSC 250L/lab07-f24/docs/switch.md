### Git User Configuration

Each partner should set the git configuration with their name and email **every** time they switch to the *driver* role.

We provide two options:
1. Once your CLI is open, execute the following commands to configure git.
  * To set your user name: `git config --global user.name "Your Name"`
  * To set your Email: `git config --global user.email first.last.yy@cnu.edu`
    * __Please do not use a personal email__
2. Use the `switch.py` script in the main project directory
  * After you clone the project, we will edit the file `switch.py`, and put the appropriate name and email for each partners.
  * Then execute this script `python switch.py` to configure git whenever you switch.

[Go back to the main lab](../README.md)