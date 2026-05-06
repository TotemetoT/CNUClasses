from tkinter import *
class Helper:
    def __init__(self, width, height):

        print("  initializing the Helper class ...")
        self.root = Tk() #This is the "root" window
        self.root.title("Help Demo") #This sets the title on the window
        self.root.geometry('{}x{}'.format(width,height)) #this sets the size of the window as a string
        self.root.configure(background='cyan') #using configure we can set lots of properties of the window. Here we set the background to cyan


        # Placing a button requires you pass the window it will be placed in, and has optional params, such as 'text'
        # place a button in the root window, set the type to "Do It!"
        self.btn = Button(self.root, text="Do It!")

        # Specify the location of the button to "place" it in the window.
        # Here, we specify to place it directly in the center of the window
        self.btn.place(x=width//2, y=height//2)
        print("  done init!")

    def run(self):
        print("    Entering the Tk main event loop")
        # root is a Tk Window. It has a mainloop which just runs forever (until it is closed by a Human)
        # in the main loop, it "listens" for 'Events' such as mouse clicks, keyboard commands, OS interrupts, etc.
        self.root.mainloop()
        print("    Leaving the Tk main event loop")

if __name__ == '__main__':

    print("Inside main...")
    helper = Helper(400, 500) # create the window
    helper.run() # run the window
    print("done!")
