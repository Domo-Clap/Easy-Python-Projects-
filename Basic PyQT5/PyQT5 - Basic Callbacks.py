import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Abstract the QMainWindow function call to a class for easier customization
class MainWindow(QMainWindow):
    # Runs when an object instance of the class is created
    def __init__(self):
        super().__init__()

        #self.button_is_checked = True

        # Sets the title of the window
        self.setWindowTitle('My First Test App')

        # Places a button in the window with the following text
        self.button = QPushButton('Press This Button!')

        #button.setCheckable(True)

        #button.clicked.connect(self.the_button_was_toggled)

        #button.setChecked(self.button_is_checked)

        # Makes it so the button widget is connected to the the_button_was_clicked function
        self.button.clicked.connect(self.the_button_was_clicked)

        # Places the button as the central widget of the window
        self.setCentralWidget(self.button)

    # Callback function for when the button is clicked
    def the_button_was_clicked(self):

        # Prints basic text to console
        self.button.setText('Already Clicked this button')

        # Sets the button enabled aspect to False
        self.button.setEnabled(False)

        # Sets a new title for the window
        self.setWindowTitle('New Title Here!!!')

    #Callback function for when the button is toggled. Not used in this code at the moment
    def the_button_was_toggled(self, checked):

        self.button_is_checked = checked

        print(self.button_is_checked)

# Used to create the window and show it
def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()


if __name__ == '__main__':
    createWindow()

