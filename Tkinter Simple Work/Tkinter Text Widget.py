import tkinter
from tkinter import *
from tkinter.ttk import *

root = Tk()

# Sets title for main window or root
root.title('Very, very basic title')

# Sets the size of the main window
root.geometry('450x300')

# Creates a new text widget
newText = Text(root, height = 5, width = 52)

# Creates a new label widget with specific text
newLabel = Label(root, text = 'Fact of the Day!')
# Changes the font of the label widget
newLabel.config(font=('Courier', 14))

# Holds string to be displayed
Fact = """A man can be arrested in Italy for wearing a skirt in public"""

# Creates a new button widget
btn1 = Button(root, text = 'Next')
# Creates a new button widget
btn2 = Button(root, text = 'Exit', command=root.destroy)

# Places all widgets into the window
newLabel.pack()
newText.pack()
btn1.pack()
btn2.pack()

# Inserts text into the text wiidget
newText.insert(tkinter.END, Fact)

# Starts the main window and displays it
mainloop()