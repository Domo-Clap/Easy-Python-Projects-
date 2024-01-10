from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()

# Sets title for main window or root
root.title('MENUSSSSS!!!!')

# Sets the size of the main window
root.geometry('450x300')

# Creates a menu widget for the main window
menubar = Menu(root)

# Creates a branch of the menu widget and attaches it to the menubar menu
file = Menu(menubar, tearoff=0)
# Adds the label file to the menu
menubar.add_cascade(label='File', menu = file)
# Adds numerous labels under the file branch
file.add_command(label='New File', command = None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
# Creates a separator in the branch. Will show up as a straight line
file.add_separator()
file.add_command(label='Exit', command= root.destroy)

# Creates a branch of the menu widget and attaches it to the menubar menu
edit = Menu(menubar, tearoff=0)
# Adds the edit label to the menu
menubar.add_cascade(label='Edit', menu = edit)
# Adds numerous label under the edit branch
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
# Creates a separator in the branch. Will show up as a straight line
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Creates a branch of the menu widget and attaches it to the menubar menu
help_ = Menu(menubar, tearoff=0)
# Adds the help label to the menu
menubar.add_cascade(label='Help', menu=help_)
# Adds numerous label under the help branch
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
# Creates a separator in the branch. Will show up as a straight line
help_.add_separator()
help_.add_command(label='About Tk', command=None)

root.config(menu=menubar)

# Starts the main window and displays it
mainloop()