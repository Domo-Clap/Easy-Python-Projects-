import tkinter
from tkinter import *

root = Tk()
# Sets the minimum size for the main window
root.minsize(600, 400)


name = tkinter.StringVar()
password = tkinter.StringVar()

# Function used to take input from user and print it out in the console
def submit():

    # Holds the name value sent in the nameEntry widget
    nameVar = name.get()
    # Holds the password value sent in the passwordEntry widget
    passVar = password.get()

    # Prints out the username and password submitted by the user in the entry widgets
    print("The name is : " + nameVar)
    print("The password is : " + passVar)

    # Resets the name and password variables back to normal
    name.set("")
    password.set("")

# Creates a new label showing text related to name
nameLabel = tkinter.Label(root, text = 'Username', font = ('calibre', 10, 'bold'))
# Creates a new text entry widget that allows a user to enter text
nameEntry = tkinter.Entry(root, textvariable= name, font = ('calibre', 10, 'normal'))

# Creates a new label showing text related to password
passwordLabel = tkinter.Label(root, text = 'Password', font = ('calibre', 10, 'bold'))
# Creates a new text entry widget that allows a user to enter text
passwordEntry = tkinter.Entry(root, textvariable= password, font = ('calibre', 10, 'normal'), show = '*')

# Creates a button that has the text submit and is connected to the submit function
btn1 = tkinter.Button(root, text = 'Submit', command= submit)

# Places the name label and name entry widgets in the grid for the main window
nameLabel.grid(row=0, column=0)
nameEntry.grid(row=0, column=1)

# Places the password label and password entry widgets in the grid for the main window
passwordLabel.grid(row=1, column=0)
passwordEntry.grid(row=1, column=1)

# Places the button in the grid for the main window
btn1.grid(row=2, column=1)

# Starts the main window and displays it
mainloop()

