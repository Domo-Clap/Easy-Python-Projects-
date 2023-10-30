from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys

class MainWindow(QMainWindow):
    # Runs when an object instance of the class is created
    def __init__(self):
        super().__init__()

        # Sets the window title
        self.setWindowTitle('Initial window title')

        # Creates a label in the application
        self.label = QLabel()

        # Creates an input text box in the application
        self.input = QLineEdit()

        # Connects the action of the text being changed to the setText function for a label widget
        self.input.textChanged.connect(self.label.setText)

        # Creates a layout for the label and input box to be placed in
        layout = QVBoxLayout()

        # Adds the two widgets to the layout
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        # Creates a container which will hold the layout specified above
        container = QWidget()
        container.setLayout(layout)

        # Sets the container as the central widget for the app
        self.setCentralWidget(container)

# Used to create the window and show it
def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()


if __name__ == '__main__':
    createWindow()