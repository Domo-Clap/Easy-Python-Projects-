import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QAction, QStatusBar, QCheckBox, QPushButton, QDialog
from PyQt5.QtGui import QPalette, QColor

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Sets the window title
        self.setWindowTitle("PyQT5 Dialogs Example")

        # Creates button in app
        testButton = QPushButton('Click me!')
        # Connects button to callback
        testButton.clicked.connect(self.button_clicked)
        # Sets button as central widget
        self.setCentralWidget(testButton)

    # Button clicked callback
    def button_clicked(self, s):
        print('click', s)
        # Creates dialog
        dial = QDialog(self)
        # Sets dialog window title
        dial.setWindowTitle('Test Dialog')
        # Creates and runs event loop
        dial.exec()


def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createWindow()
