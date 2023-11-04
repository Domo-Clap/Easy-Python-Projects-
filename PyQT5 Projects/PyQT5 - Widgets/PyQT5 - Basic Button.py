import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt

#Abstract the QMainWindow function call to a class for easier customization
class MainWindow(QMainWindow):
    #Runs when an object instance of the class is created
    def __init__(self):
        super().__init__()

        #Sets the title of the window
        self.setWindowTitle('My First Test App')

        #Places a button in the window with the following text
        button = QPushButton('Press This Button!')

        #Caps the size of the window being created
        self.setFixedSize(QSize(800, 600))

        #Places the button as the central widget of the window
        self.setCentralWidget(button)

#Used to create the window and show it
def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()


if __name__ == '__main__':
    createWindow()

