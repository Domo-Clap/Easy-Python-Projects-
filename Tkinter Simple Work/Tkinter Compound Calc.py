#Imports tkinter for UI
from tkinter import *

# Function used to clear the entry widgets
def clear_all():
    # Uses the .delete method to remove all text in the entry widgets from index 0 to the end
    principEntry.delete(0, END)
    rateEntry.delete(0, END)
    timeEntry.delete(0, END)
    resultEntry.delete(0, END)

    # Sets the focus on the principal_field entry box
    principEntry.focus_set()

# Function used to calculate the compound interest
def calculate_ci():
    # Gets values from the entry widgets and turns them into ints
    principle = int(principEntry.get())
    rate = float(rateEntry.get())
    time = int(timeEntry.get())
    # Takes the altered values from the entry widgets and plugs them into the equation to find compound interest
    CI = principle * (pow((1 + rate / 100), time))

    # Changes the text in the result entry widget and replaces it with the found CI
    # Could possibly change this widget from a entry widget
    resultEntry.insert(10, CI)

# Main function that holds UI placement logic
if __name__ == '__main__':

    root = Tk()

    # Changes the main window config so that the background is lavender
    root.configure(background = 'lavender')

    # Sets the main window size
    root.geometry("400x300")

    # Sets the main window title
    root.title('Compound Interest Calculator')

    mainLabel = Label(root, text='Compound Interest Finder!', font=('Arial', 16, 'bold'), fg = 'black', bg = 'lavender')
    mainLabel.grid(row=0, columnspan=3)

    # Creates a label and sets its font and color
    label1 = Label(root, text='Principle Amount(Rs):', font=('Arial', 13), fg='black', bg='light grey')

    # Creates a label and sets its font and color
    label2 = Label(root, text='Rate(%):', font=('Arial', 13), fg='black', bg='light grey')

    # Creates a label and sets its font and color
    label3 = Label(root, text='Time(years):', font=('Arial', 13), fg='black', bg='light grey')

    # Creates a label and sets its font and color
    label4 = Label(root, text='Compound Interest:', font=('Arial', 13), fg='black', bg='light grey')

    # Places all of the previously made labels into the main window via grid rows and columns
    label1.grid(row=1, column=0, padx= 10, pady= 10)
    label2.grid(row=2, column=0, padx= 10, pady= 10)
    label3.grid(row=3, column=0, padx= 10, pady= 10)
    label4.grid(row=4, column=0, padx= 10, pady= 10)

    # Creates an entry text widget for users to enter text
    principEntry = Entry(root)
    # Creates an entry text widget for users to enter text
    rateEntry = Entry(root)
    # Creates an entry text widget for users to enter text
    timeEntry = Entry(root)
    # Creates an entry text widget for users to enter text
    resultEntry = Entry(root)

    # Places all of the entry text widgets into the main window via rows and columns
    principEntry.grid(row=1, column=1, padx= 10, pady= 10)
    rateEntry.grid(row=2, column=1, padx= 10, pady= 10)
    timeEntry.grid(row=3, column=1, padx= 10, pady= 10)
    resultEntry.grid(row=4, column=1, padx= 10, pady= 10)

    # Creates a button that is used to submit the info in the entry text widgets
    btn1 = Button(root, text='Submit', bg='light green', fg='black', command=calculate_ci)

    # Creates a button that is used to clear the info in the entry text widgets
    btn2 = Button(root, text='Clear', bg='light green', fg='black', command=clear_all)

    # Adds tje buttons to the main window via grid rows and columns
    btn1.grid(row=5, column=1, pady=10)
    btn2.grid(row=6, column=1, pady=10)

    # Starts the main window and displays it
    root.mainloop()