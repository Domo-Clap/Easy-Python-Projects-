from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
# Sets the minimum size of the window
root.minsize(150, 100)

# Creates a label widget and places it in the main window
Label(root, text = 'Random Text Lol', font = ('Verdana', 15)).pack(side= TOP, pady = 10)
# Creates a button widget and places it in the main window. No function atm
Button(root, text = 'Click Me!').pack(side = TOP)

# Starts the main window and displays it
mainloop()