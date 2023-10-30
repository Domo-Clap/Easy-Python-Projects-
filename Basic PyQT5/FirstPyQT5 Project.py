#This mini project is apart of other small pieces of code that I am making as practice
#This is a simple piece of code that will create a window and open it using the pyqt5 library

#Imports the pyqt5 classes
from PyQt5.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

#This function will create the Qapplication instance and the window. Then it will move the window from being hidden to shown.
def createWindow():

    #Creates the Qapplication instance with sys.arg since sys.arg contains the command line arguments.
    app = QApplication(sys.argv)

    # Creates a Qt widget, which is the window being opened.
    window = QWidget()
    #Makes the window shown instead of hidden.
    window.show()

    #Start the event loop.
    app.exec()


#Main function where createWindow function is called.
if __name__ == '__main__':
    createWindow()

