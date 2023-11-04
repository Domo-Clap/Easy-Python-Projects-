import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QAction, QStatusBar
from PyQt5.QtGui import QPalette, QColor

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Sets the window title
        self.setWindowTitle("PyQT5 Toolbar Example")

        # Creates a label to be shown in the app and sets the text alignment to center
        mainLabel = QLabel('Welcome to the new app!')
        mainLabel.setAlignment(Qt.AlignCenter)

        # Sets the label as the central widget for the app
        self.setCentralWidget(mainLabel)

        # Creates a toolbar
        toolbar = QToolBar('Main Toolbar')
        # Adds the toolbar to the main window object
        self.addToolBar(toolbar)

        #Creates a button for the toolbar called Test Button
        buttonAction1 = QAction('Test Button', self)
        # Sets the hover tip to This is a button
        buttonAction1.setStatusTip('This is a button')
        # Connects the process of clicking the button to a callback
        buttonAction1.triggered.connect(self.onMyToolBarButtonClick)
        # Makes it so the button remains checked after being clicked
        buttonAction1.setCheckable(True)
        # Adds the button to the toolbar
        toolbar.addAction(buttonAction1)

    # Callback function for when the button is clicked
    def onMyToolBarButtonClick(self, s):
        print('clicked', s)

# Used to create the window and show it
def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createWindow()
