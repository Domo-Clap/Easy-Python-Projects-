from tkinter import *
from tkinter.ttk import *

root = Tk()

# Sets the title of the window
root.title('Very, very basic title')

# Sets the size of the window
root.geometry('450x300')

# Creates a menu widget
menu = Menu(root)
# Creates a tab to be shown in the menu
item = Menu(menu)
# Adds the following label under the new item on the menu bar
item.add_command(label='New')
# Adds the following label on the menubar
menu.add_cascade(label='File', menu=item)
# Adds the menubar to the window
root.config(menu=menu)

# Creates a new label
label1 = Label(root, text = 'Basic Label Text')
# Places said label
label1.grid()

# Creates a new text entry widget
txtBox = Entry(root, width=10)
# Places said widget
txtBox.grid(column=1, row=0)

# Function used to react to the button being clicked
# Changes the first label to what the user entered
def clicked():
    res = "Stuff you wrote: " + txtBox.get()
    label1.configure(text = res)

# Creates a new button widget
# Connected to clicked() callback
button = Button(root, text = 'Geek', command=clicked)

# Places the button in the main window
button.grid(column=2, row=0)

# Starts the main window and displays it
root.mainloop()