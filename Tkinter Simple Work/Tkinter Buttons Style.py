from tkinter import *
from tkinter.ttk import *

root = Tk()

# Sets the title of the window
root.title('Very, very basic title')

# Sets the size of the window
root.geometry('450x300')

# Creates a style object
style = Style()

# Configures the style so that it has a specific font
style.configure('TButton', font = ('calibri', 10, 'bold'), borderwidth = '4')

# Maps the style
style.map('TButton',  foreground = [('active', '!disabled', 'green')],
                            background = [('active', 'black')])

# Creates a Button that destroys the window on click
btn = Button(root, text='Click me !', command=root.destroy)
# Places the button in the main window
btn.grid(row=0, column=3, padx=100)

# Starts the main window and displays it
root.mainloop()