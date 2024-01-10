from tkinter import *
from tkinter.ttk import *

root = Tk()

# Sets the title of the window
root.title('Very, very basic title')

# Sets the size of the window
root.geometry('450x300')

# Creates a new label
w = Label(root, text='Check Buttons!!!', font="50")
w.pack()

# Creates 3 int variables
Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

# Creates 3 new button widgets
Button1 = Checkbutton(root, text = "First Option", variable = Checkbutton1, onvalue = 1, offvalue = 0, width=15)
Button2 = Checkbutton(root, text = "Second Option", variable = Checkbutton2, onvalue = 1, offvalue = 0, width=15)
Button3 = Checkbutton(root, text = "Third Option", variable = Checkbutton3, onvalue = 1, offvalue = 0, width=15)

# Places all 3 button widgets in the main window
Button1.pack()
Button2.pack()
Button3.pack()

# Starts the main window and displays it
root.mainloop()