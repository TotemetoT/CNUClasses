from tkinter import *
import math


class Helper:

    def __init__(self, width, height):

        print("  initializing the Helper class ...")
        self.root = Tk()

        self.root.title("Help Demo")

        # We no longer need to specify a width and height, because we are going to
        # add items to a frame win the window, AND we will specify that frame
        # to have the size needed to fit everything we add to it (self.win.pack())
        #self.root.geometry('{}x{}'.format(width,height))
        self.root.configure(background='green')

        # The correct way to create a GUI with tkinter is to create a "Frame" and place it in the root
        #  Then, you add elements to the frame
        # Create a frame and bind it to the root
        self.win = Frame(self.root)
        #Notice, that the background you see is red. That is because we placed a frame on top of the root
        #self.win.configure(background='red')

        # A label is a Widget that displays text
        # We add the label to the frame, not the root, and we specify the label to display the text "Enter cmd:"
        self.cmd_label = Label(self.win, text="Enter cmd:")
        # You MUST specify where to add the label to the frame using the grid's row/column
        self.cmd_label.grid(row=2, column=1)

        # Items are added to the grid, but the cells in the grid have no size, so you will at first
        # only see the label. As you add items, they are added relative to each other, and the
        # grid will scale to fit items in it

        # Create a text box (Entry) which allows a user to type in text
        # We are adding it to the right of the "Enter cmd:" label (column 2)
        # We specify its width is 20, and its background is white
        self.cmd_entry = Entry(self.win, width=20, bg="white")
        self.cmd_entry.grid(row=2,column=2)

        # We can "Bind" events and a response to widgets. Here, we are binding a user hits the return key in the
        # cmd_entry box event to the self.do_it method
        self.cmd_entry.bind('<Return>', self.do_it)
        # Here, we are binding a user hits 'a' key in the cmd_entry to the self.do_that method
        self.cmd_entry.bind('<a>', self.do_that)

        # Add a button to the frame, and specify its the frame to place it in, text = text on the button,
        # command = the method that is called when it is clicked. Then, specify its location in the frame's grid
        self.btn = Button(self.win, text="Do It!", command=self.do_it)
        print("   Type of do_it = " + str(type(self.do_it))) # You can pass functions as parameters in python.
        self.btn.grid(row=2, column=3)

        # Add a label that says output
        self.output_label = Label(self.win, text="Output:")
        self.output_label.grid(row=3, column=1)

        # Add a Text, which will display a lot of text. Specify the frame to add it to,
        # its width, how to handle text wrapping (break by word), its background color (bg), and the text color (fg)
        self.output = Text(self.win, width=80, wrap=WORD,bg='blue',fg='white')
        # Add the text box to row4,col1, and tell it to span 4 columns
        # TODO - try without columnspan to see what happens
        self.output.grid(row=4,column=1, columnspan=4)

        # Ad a quit button, and on clicked tell it to exit the root, thereby quitting the program mainloop
        self.quit = Button(self.win, text="Quit!", command=self.root.quit)
        self.quit.grid(row=5, column=4)

        # don't do geometry and size to fit (required unless we specify exact pixel dimensions, etc of everything)
        self.win.pack()

        print("  done init!")

    def do_it(self, *args):
        #print(args)
        print("    Doing it for {}!".format(self.cmd_entry.get()))

        # Keeps adding to the end if we don't delete prior
        # self.output.delete(0.0,END) # This will clear the text box
        self.output.insert(END, "{} ".format(self.cmd_entry.get())*10)


    def do_that(self, *args):
        # The args specify the event that triggered this method call
        # An event is an object which holds information about itself
        # Such as a KeyPress event - what triggered it, and the location (relative to the top left of the window)
        # where it was triggered
        print ("   Doing that, args = ", args)

    def run(self):
        print("    Entering the Tk main event loop")
        self.root.mainloop()
        print("    Leaving the Tk main event loop")


if __name__ == '__main__':

    print("Inside main...")
    helper = Helper(600, 500)
    helper.run()
    print("done!")
