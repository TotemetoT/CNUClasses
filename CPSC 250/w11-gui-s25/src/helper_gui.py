from tkinter import *
import math

"""
Shell class for helper GUI

This code is missing some code and needs modifying:

1) "do it" button OR entry return should process the entered command
2) "quit" button should exit the program.
3) Output text box should display the __doc__ string of command (use eval(cmd).__doc__),
    OR print "Invalid command" if not a valid built in Python command

"""

class Helper:

    def __init__(self):

        print("  initializing the Helper class ...")
        self.root = Tk()

        self.root.title("Help Demo")
        self.win = Frame(self.root)

        # Create the Enter Cmd label
        self.cmd_label = Label(self.win, text="Enter cmd:")
        self.cmd_label.grid(row=2, column=1)

        # Create the command entry box
        self.cmd_entry = Entry(self.win, width=20, bg="white")
        self.cmd_entry.grid(row=2,column=2)

        # Create the Do It Button
        self.btn = Button(self.win, text="Do It!")
        self.btn.grid(row=2, column=3)

        # Create the Output Label
        self.output_label = Label(self.win, text="Output:")
        self.output_label.grid(row=3, column=1)

        # Create the Output text box
        self.output = Text(self.win, width=80, wrap=WORD,bg='blue',fg='white')
        self.output.grid(row=4,column=1, columnspan=4)

        # Create the Quit Button
        self.quit = Button(self.win, text="Quit!")
        self.quit.grid(row=5, column=4)

        # Pack the frame
        self.win.pack()
        print("  done init!")


    def run(self):
        print("    Entering the Tk main event loop")
        self.root.mainloop()
        print("    Leaving the Tk main event loop")


if __name__ == '__main__':

    print("Inside main...")
    helper = Helper()
    helper.run()
    print("done!")
