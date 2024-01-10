from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()

# Sets title for main window or root
root.title('Resizeable Window!')
# Sets the minimum size of the window
root.minsize(150, 100)

# Creates a label widget and places it in the main window
Label(root, text = 'It\'s not resizable').pack(side = TOP, pady = 10)

# Makes it so the main window is not resizable
root.resizable(False, False)

# Starts the main window and displays it
mainloop()