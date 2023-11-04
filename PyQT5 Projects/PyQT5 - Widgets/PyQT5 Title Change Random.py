from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

# List of possible titles for the application
possible_titles = [
    'Initial window title'
    'Try this new app!',
    'Or maybe try this one',
    'Possibly this one',
    'Funny title haha',
    'Gotta love water!',
    'Idk about that one',
    'Generic App Title',
    'Powerade is better',
    'Something went wrong'
]

class MainWindow(QMainWindow):
    # Runs when an object instance of the class is created
    def __init__(self):
        super().__init__()

        # Holds the number of times the button is clicked in the app
        self.n_times_clicked = 0

        # Sets the window title
        self.setWindowTitle('Initial window title')

        # Creates a button widget in the app
        self.button = QPushButton('Click this button!')

        # Connects the button widget to a callback
        self.button.clicked.connect(self.the_button_was_clicked)

        # Connects the act of the window title changing to a callback
        self.windowTitleChanged.connect(self.the_window_title_changes)

        # Places the button as the central widget
        self.setCentralWidget(self.button)

    # Callback function for when the button is clicked
    def the_button_was_clicked(self):
        print('Button Clicked')

        # Assigns a random title from the possible_titles list to the temp variable
        new_title = choice(possible_titles)
        print('Setting title:  %s' % new_title)

        # Sets the window title to the random selection from the possible_titles list
        self.setWindowTitle(new_title)

    # Callback function for when the window title is changed
    def the_window_title_changes(self, window_title):
        print('Window title has been changed accordingly: %s' % window_title)

        # If the window title is Something went wrong, then the button cannot be clicked anymore
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

# Used to create the window and show it
def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()


if __name__ == '__main__':
    createWindow()