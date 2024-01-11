# Imports tkinter for UI
from tkinter import *

# Imports tkinter controls for file systems
from tkinter import filedialog

# Function used to open up the file system on a computer and change the label when a file is selected or the file system is closed
def browseFiles():
    filename= filedialog.askopenfilename(initialdir= "/", title='Select a File', filetypes=(("Text files", "*.txt"),("all files", ".")))

    label_file_explorer.configure(text="File Opened:" + filename)


root = Tk()

# Creates the title fpr the main window
root.title('File Explorer')

# Sets the size of the main window
root.geometry("700x500")

# Changes the background of the main window
root.config(background='lavender')

# Creates a label widget to be displayed in the main window with some basic text
label_file_explorer = Label(root, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue")

# Creates a button widget that is attached to the browseFiles function
btn_explorer = Button(root, text="Browse Files", command=browseFiles)

# Creates a button that is used to exit the application
btn_exit = Button(root, text="Exit", command=exit)

# Places said widgets into the main window
label_file_explorer.grid(row=1, column=0)
btn_explorer.grid(row=2, column=0)
btn_exit.grid(row=3, column=0)

# Starts the main window and displays it
root.mainloop()