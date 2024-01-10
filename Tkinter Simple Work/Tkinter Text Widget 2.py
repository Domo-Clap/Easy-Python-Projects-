import tkinter
from tkinter import *
from tkinter.ttk import *

root = Tk()

# Sets title for main window or root
root.title('Very, very basic title')

# Sets the size of the main window
root.geometry('450x300')

# Function used to get input from the user for the question and determine if it is correct or not
# Reassigns the output widget to a certain string
def Get_Input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if(INPUT == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong Answer")

# Creates a new label widget
newLabel = Label(text = 'What is 24 * 5? ')
# Creates a new text widget
inputtxt = Text(root, height=10, width=25, bg="light yellow")

# Creates another new text widget to hold the data for whether the user is correct
Output = Text(root, height=5, width=25, bg='light cyan')

# Creates a button widget that allows a user to submit their answer and see if it is correct or not
Display = Button(root, width=20, text="Show", command= lambda:Get_Input())

# Places all widgets into the window
newLabel.pack()
inputtxt.pack()
Display.pack()
Output.pack()

# Starts the main window and displays it
mainloop()