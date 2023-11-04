import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QAction, QStatusBar, QVBoxLayout, QPushButton, QDialog, QWidget

# Class for creating another window in the app
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Creates a layout for the label widget
        layout = QVBoxLayout()
        # Creates the label
        self.label = QLabel('Another Window')
        #Adds the label to the widget
        layout.addWidget(self.label)
        #sets the layout of the window
        self.setLayout(layout)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.w = None

        # Sets the window title
        self.setWindowTitle("PyQT5 MultiWindow Example")

        # Creates a button
        self.button = QPushButton('Push this button for a new window')
        # Connects the button to the callback
        self.button.clicked.connect(self.show_new_window)
        # Sets the button as the central widget
        self.setCentralWidget(self.button)

    # Callback function for the button
    def show_new_window(self, checked):
        # If the window is not open, it creates a new window
        if self.w is None:
            self.w = AnotherWindow()
        # shows the window
        self.w.show()


def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createWindow()