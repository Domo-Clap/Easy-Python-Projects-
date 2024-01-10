from tkinter import *
from tkinter.ttk import *

root = Tk()

# Sets the title of the window
root.title('Very, very basic title')

# Sets the size of the window
root.geometry('450x300')

# Creates a new label for username
userNameLbl = Label(root, text='Username').place(x = 40, y = 60)
# Creates a new label for password
passWordLbl = Label(root, text='Password').place(x = 40, y = 100)

# Creates a new button. No function currently
submitBtn = Button(root, text='Submit').place(x = 40, y = 130)

# Creates two entry text widgets
userNameEdit = Entry(root, width = 30).place(x = 110, y = 60)
passWordEdit = Entry(root, width = 30).place(x = 110, y = 100)

# Starts the main window and displays it
root.mainloop()