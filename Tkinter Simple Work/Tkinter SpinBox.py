from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()

# Sets title for main window or root
root.title('SpinBoxes!')

# Sets the size of the main window
root.geometry('450x300')

# Creates a new label widdget
newLabel = Label(root, text='SpinBox Work!', font = '50')
newLabel.pack()

# Creates a new spinbox widget allowing values from 0 to 20
sp = Spinbox(root, from_= 0, to = 20)
sp.pack()

# Starts the main window and displays it
mainloop()