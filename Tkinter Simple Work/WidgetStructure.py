from tkinter import *
from tkinter.ttk import *

def createWindow():
    # Creates the main window
    root = Tk()

    # Sets title for the main window
    root.title("Widget Objects Concept")

    # Creates a frame object to hold widgets
    frame = Frame(root)

    # Packs the frame
    frame.pack()

    # Creates a button with the text Geek
    button = Button(frame, text='Geek')
    button.pack()

    # Runs the application and tells it to continue running
    root.mainloop()



if __name__ == '__main__':
    createWindow()