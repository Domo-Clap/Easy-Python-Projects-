# Imports random
import random

# Imports tkinter
from tkinter import *
from tkinter import ttk, messagebox

# Function used to display a dialog box with details about the number rolled
def roll_dialog_box(number_rolled):
    dialog=Toplevel(root)

    # Sets the size of the dialog box
    dialog.geometry('125x125')

    # Sets the title of the dialog box
    dialog.title('You Rolled!')

    # Creates a label to be displayed in the dialog box. Sets the text to the int from the roll() function
    dialogLabel = Label(dialog, text=f'You rolled a: {number_rolled}')
    # Places the label into the dialog pox with padding
    dialogLabel.pack(padx = 20, pady = 20)

# Function used to determine what the random roll is and changes the label
def roll():

    # Creates a list of 6 dots that determine what number is rolled via the dice
    diceDots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']

    # Gets the dice visual via a random selection of the list
    rolledVis = random.choice(diceDots)

    # Gets the int value via indexing of the randomly selected visual
    rolled_num = diceDots.index(rolledVis) + 1

    # Reassigns the label to the new visual
    rollLabel.configure(text= rolledVis)

    # Places the label in the root
    rollLabel.pack()

    # Creates the dialog box to tell the user the number they rolled after the image is displayed
    roll_dialog_box(rolled_num)

# Creates the window
root = Tk()

# Sets the window size
root.geometry('300x500')

# Sets the window background
root.configure(bg="grey")

# Sets the window title
root.title('Dice Roll App')

# Creates a label to hold the dice image to be displayed
rollLabel = Label(root, font=("times", 250), bg="grey", fg='white')

# Creates a button to click to use the roll function
roll_btn = Button(root, text='Roll Dice', width=15, height=2, bg='violet', command=roll)

# Places the button into the window
roll_btn.pack(side = BOTTOM, padx = 85,pady = 50)

# Starts the window execution
root.mainloop()

