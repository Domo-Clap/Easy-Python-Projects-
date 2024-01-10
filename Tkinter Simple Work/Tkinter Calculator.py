#Imports tkinter for UI
from tkinter import *

# Used to hold the expression or equation to be calculated in the text box
expression = ""



# Used to update the text in the text entry box
def press(num):
    global expression

    # Represents the math expression and updates it with the num or value passed in
    # Essentially this changes the text string that will eventually show in the entry widget
    expression = expression + str(num)

    # Used to hold the new expression
    equation.set(expression)

# Called whenever the equals button is pressed in the calculator
def equalPress():

    try:
         global expression

         # Holds the total value of the calculated expression. So it will hold the result of the expression
         total = str(eval(expression))

         # Holds the new expression/calculation
         equation.set(total)

         # Leaves off by clearing the expression variable
         expression = ""

    except:
        equation.set(" err ")
        expression = ""

# Called whenever the 'C' button is pressed in the calculator
def clear():
    global expression
    # Clears the expression variable for future input
    expression= ""
    # Clears the equation variable for future calculations
    equation.set("")

# Start of main function loop where widgets are placed and main window is built
if __name__ == '__main__':
    root = Tk()

    # Sets title for main window or root
    root.title('Calculator')

    # Sets the size of the main window
    root.geometry('350x250')

    # Makes it so the main window is not resizable
    root.resizable(False, False)

    # Creates the equation variable used in calculations
    equation = StringVar()

    # Creates an Entry widget to hold text from equation variable. Font argument is used to change the size of the Entry box
    expressionText = Entry(root, textvariable=equation, font=('Arial', 14))

    # Assigns the expressionText Entry widget to 0, 0 in the grid. Makes it span 4 columns
    expressionText.grid(columnspan=4, ipadx=70)

    # Creates button for the number 1 and assigns its click callback to the press function. Passes 1 as the argument to the press function
    btn1 = Button(root, text= ' 1 ', fg='black', bg='light green', command=lambda: press(1), height=2, width=7)
    # Assigns the #1 button to a specified point in the grid
    btn1.grid(row=2, column = 0)

    # Creates button for the number 2 and assigns its click callback to the press function. Passes 2 as the argument to the press function
    btn2 = Button(root, text=' 2 ', fg='black', bg='light green', command=lambda: press(2), height=2, width=7)
    # Assigns the #2 button to a specified point in the grid
    btn2.grid(row=2, column=1)

    # Creates button for the number 3 and assigns its click callback to the press function. Passes 3 as the argument to the press function
    btn3 = Button(root, text=' 3 ', fg='black', bg='light green', command=lambda: press(3), height=2, width=7)
    # Assigns the #3 button to a specified point in the grid
    btn3.grid(row=2, column=2)

    # Creates button for the number 4 and assigns its click callback to the press function. Passes 4 as the argument to the press function
    btn4 = Button(root, text=' 4 ', fg='black', bg='light green', command=lambda: press(4), height=2, width=7)
    # Assigns the #4 button to a specified point in the grid
    btn4.grid(row=3, column=0)

    # Creates button for the number 5 and assigns its click callback to the press function. Passes 5 as the argument to the press function
    btn5 = Button(root, text=' 5 ', fg='black', bg='light green', command=lambda: press(5), height=2, width=7)
    # Assigns the #5 button to a specified point in the grid
    btn5.grid(row=3, column=1)

    # Creates button for the number 6 and assigns its click callback to the press function. Passes 6 as the argument to the press function
    btn6 = Button(root, text=' 6 ', fg='black', bg='light green', command=lambda: press(6), height=2, width=7)
    # Assigns the #6 button to a specified point in the grid
    btn6.grid(row=3, column=2)


    # Creates button for the number 7 and assigns its click callback to the press function. Passes 7 as the argument to the press function
    btn7 = Button(root, text=' 7 ', fg='black', bg='light green', command=lambda: press(7), height=2, width=7)
    # Assigns the #7 button to a specified point in the grid
    btn7.grid(row=4, column=0)

    # Creates button for the number 8 and assigns its click callback to the press function. Passes 8 as the argument to the press function
    btn8 = Button(root, text=' 8 ', fg='black', bg='light green', command=lambda: press(8), height=2, width=7)
    # Assigns the #8 button to a specified point in the grid
    btn8.grid(row=4, column=1)

    # Creates button for the number 9 and assigns its click callback to the press function. Passes 9 as the argument to the press function
    btn9 = Button(root, text=' 9 ', fg='black', bg='light green', command=lambda: press(9), height=2, width=7)
    # Assigns the #9 button to a specified point in the grid
    btn9.grid(row=4, column=2)

    # Creates button for the number 0 and assigns its click callback to the press function. Passes 0 as the argument to the press function
    btn0 = Button(root, text=' 0 ', fg='black', bg='light green', command=lambda: press(0), height=2, width=7)
    # Assigns the #0 button to a specified point in the grid
    btn0.grid(row=5, column=1)


    # Creates button for the + operator and assigns its click callback to the press function. Passes + as the argument to the press function
    btnPlus = Button(root, text = ' + ', fg='black', bg='light green', command=lambda: press("+"), height=2, width=7)
    # Assigns the + button to a specified point in the grid
    btnPlus.grid(row=2, column=3)

    # Creates button for the - operator and assigns its click callback to the press function. Passes - as the argument to the press function
    btnMinus = Button(root, text=' - ', fg='black', bg='light green', command=lambda: press("-"), height=2, width=7)
    # Assigns the - button to a specified point in the grid
    btnMinus.grid(row=3, column=3)

    # Creates button for the * operator and assigns its click callback to the press function. Passes * as the argument to the press function
    btnMultiply = Button(root, text=' * ', fg='black', bg='light green', command=lambda: press("*"), height=2, width=7)
    # Assigns the * button to a specified point in the grid
    btnMultiply.grid(row=4, column=3)

    # Creates button for the / operator and assigns its click callback to the press function. Passes / as the argument to the press function
    btnDivide = Button(root, text=' / ', fg='black', bg='light green', command=lambda: press("/"), height=2, width=7)
    # Assigns the / button to a specified point in the grid
    btnDivide.grid(row=5, column=3)


    # Creates button for the = operator and assigns its click callback to the equalPress function.
    btnEqual = Button(root, text = ' = ', fg='black', bg='light green', command=equalPress, height=2, width=7)
    # Assigns the = button to a specified point in the grid
    btnEqual.grid(row=6, column=3)

    # Creates button for the clear function and assigns its click callback to the clear function.
    btnClear = Button(root, text= ' C ', fg='black', bg='light green', command=clear, height=2, width=7)
    # Assigns the clear button to a specified point in the grid
    btnClear.grid(row=5, column=0)

    # Creates button for the '.' decimal point and assigns its click callback to the press function. Passes '.' as the argument to the press function
    btnDecimal = Button(root, text=' . ', fg='black', bg='light green', command=lambda: press('.'), height=2, width=7)
    # Assigns the '.' button to a specified point in the grid
    btnDecimal.grid(row=5, column=2)

    # Starts the main window and displays it
    root.mainloop()