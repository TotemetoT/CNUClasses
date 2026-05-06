import tkinter as tk
from tkinter import colorchooser
import os

class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=5, sticky="nsew")

        self.pen_shape = "circle"
        self.pen_color = "black"
        self.pen_size = 5

        #Color Frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=0, column=0, sticky="ew")

        #Bottom Frame
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.grid(row=2, column=0, sticky="ew")

        self.canvas.bind("<B1-Motion>", self.paint)

        #Color Buttons Row
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=0, column=0, sticky="ew")

        # Create Different Color Buttons
        self.create_color_button("Red")
        self.create_color_button("Orange")
        self.create_color_button("Yellow")
        self.create_color_button("Green")
        self.create_color_button("Blue")
        self.create_color_button("Purple")
        self.anyColor = button = tk.Button(self.button_frame, text="Pick Color", fg="Black", bg="White", command=self.choose_custom_color)
        self.anyColor.pack(side="left", padx=5, pady=5)


        self.root.rowconfigure(1, weight=1)  # Make canvas row expandable
        self.root.columnconfigure(0, weight=1)  # Full width
        self.button_frame.columnconfigure(tuple(range(6)), weight=1)  # Even spacing for buttons

        # Pen Size Buttons
        self.smaller_button = tk.Button(self.bottom_frame, text="Smaller", command=self.decrease_pen_size)
        self.smaller_button.pack(side="left", padx=5, pady=5)
        self.larger_button = tk.Button(self.bottom_frame, text="Larger", command=self.increase_pen_size)
        self.larger_button.pack(side="left", padx=5, pady=5)

        # Clear and Eraser Buttons
        self.clear_button = tk.Button(self.bottom_frame, text="Clear", command=self.clear)
        self.clear_button.pack(side="right", padx=5, pady=5)
        self.eraser_button = tk.Button(self.bottom_frame, text="Eraser", command=lambda: self.change_color("White"))
        self.eraser_button.pack(side="right", padx=5, pady=5)

        # Pen Size Text Entry (Challenge #1)
        self.pen_size_var = tk.StringVar(value=str(self.pen_size))
        self.pen_size_entry = tk.Entry(self.bottom_frame, textvariable=self.pen_size_var, width=5)
        self.pen_size_entry.pack(side="left", padx=5, pady=5)

        # Click "enter" to change text size
        self.pen_size_entry.bind("<Return>", self.set_pen_size_from_entry)

        # Pen Shape Buttons
        self.shape_circle = tk.Button(self.bottom_frame, text="Circle", command=lambda: self.change_shape("circle"))
        self.shape_circle.pack(side="left", padx=5, pady=5)

        self.shape_square = tk.Button(self.bottom_frame, text="Square", command=lambda: self.change_shape("square"))
        self.shape_square.pack(side="left", padx=5, pady=5)

        self.shape_triangle = tk.Button(self.bottom_frame, text="Triangle", command=lambda: self.change_shape("triangle"))
        self.shape_triangle.pack(side="left", padx=5, pady=5)

    def create_color_button(self, color):
        button = tk.Button(self.button_frame, text="COLOR__BUTTON", fg=color, bg=color, command=lambda c=color: self.change_color(c))
        button.pack(side="left", padx=5, pady=5)

    def change_color(self, color):
        print(color)
        self.pen_color = color

    def increase_pen_size(self):
        self.pen_size += 1
        self.pen_size_var.set(str(self.pen_size))
        print(f"Pen size increased to {self.pen_size}")

    def decrease_pen_size(self):
        if self.pen_size > 1:
            self.pen_size -= 1
            self.pen_size_var.set(str(self.pen_size))
            print(f"Pen size decreased to {self.pen_size}")
        else:
            print("Pen size is already at minimum")

    def clear(self):
        self.canvas.delete("all")

    def choose_custom_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code[1]:  # color_code[1] is the hex string
            self.change_color(color_code[1])

    def paint(self, event):
        x, y = event.x, event.y
        size = self.pen_size

        if self.pen_shape == "circle":
            self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=self.pen_color, outline=self.pen_color)
        elif self.pen_shape == "square":
            self.canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=self.pen_color,
                                         outline=self.pen_color)
        elif self.pen_shape == "triangle":
            points = [
                x, y - size,
                   x - size, y + size,
                   x + size, y + size
            ]
            self.canvas.create_polygon(points, fill=self.pen_color, outline=self.pen_color)

    def set_pen_size_from_entry(self, event=None):
        try:
            size = int(self.pen_size_var.get())
            if size > 0:
                self.pen_size = size
                print(f"Pen size set to {self.pen_size}")
            else:
                print("Pen size must be positive.")
        except ValueError:
            print("Invalid pen size input.")

    def change_shape(self, shape):
        print(f"Pen shape changed to {shape}")
        self.pen_shape = shape
        self.pen_shape.set(f"Current Brush: {shape.capitalize()}")


if __name__ == "__main__":
    root = tk.Tk()
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    app = Paint(root)
    root.mainloop()
