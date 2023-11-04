import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QAction, QStatusBar
from PyQt5.QtGui import QPalette, QColor

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Sets the window title
        self.setWindowTitle("PyQT5 Menus Example 1")

        testLabel = QLabel('Hello there! Test 1, 2, 3')
        testLabel.setAlignment(Qt.AlignCenter)

        # Sets the label as the central widget for the app
        self.setCentralWidget(testLabel)

        # Creates a toolbar
        toolbar = QToolBar('Main Toolbar')
        # Adds the toolbar to the main window object
        self.addToolBar(toolbar)

        # Creates a button for the toolbar called Test Button
        buttonAction1 = QAction('Test Button', self)
        # Sets the hover tip to This is a button
        buttonAction1.setStatusTip('This is a button')
        # Connects the process of clicking the button to a callback
        buttonAction1.triggered.connect(self.onMyToolBarButtonClick)
        # Makes it so the button remains checked after being clicked
        buttonAction1.setCheckable(True)
        # Adds the button to the toolbar
        toolbar.addAction(buttonAction1)

        toolbar.addSeparator()

        # Creates a button for the toolbar called Test Button
        buttonAction2 = QAction('Test Btn 2', self)
        # Sets the hover tip to This is a button
        buttonAction2.setStatusTip('This is the 2nd button')
        # Connects the process of clicking the button to a callback
        buttonAction2.triggered.connect(self.onMyToolBarButtonClick)
        # Makes it so the button remains checked after being clicked
        buttonAction2.setCheckable(True)
        # Adds the button to the toolbar
        toolbar.addAction(buttonAction2)

        self.setStatusBar(QStatusBar(self))

        # Creates a menu bar in the app
        menu = self.menuBar()

        # Adds a menu bar called File
        file_menu = menu.addMenu('&File')
        # Adds an action to file menu bar option
        file_menu.addAction(buttonAction1)

        file_menu.addSeparator()

        file_menu.addAction(buttonAction2)

    # Callback function for when the button is clicked
    def onMyToolBarButtonClick(self, s):
        print('clicked', s)



def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createWindow()
