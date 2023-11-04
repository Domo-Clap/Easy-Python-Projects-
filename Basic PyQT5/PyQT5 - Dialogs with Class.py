import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QAction, QStatusBar, QCheckBox, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Sets the window title
        self.setWindowTitle("PyQT5 Dialogs with Class Example")

        # Creates button in app
        testButton = QPushButton('Click me!')
        # Connects button to callback
        testButton.clicked.connect(self.button_clicked)
        # Sets button as central widget
        self.setCentralWidget(testButton)

    def button_clicked(self, s):
        print("click", s)

        dlg = CustomDialogObj()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

class CustomDialogObj(QDialog):
    def __init__(self):

        super().__init__()

        self.setWindowTitle('Example window')

        btn = QDialogButtonBox.Yes | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(btn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createWindow()
