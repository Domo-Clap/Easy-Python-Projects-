import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Creates a label to be placed in the application
        self.label = QLabel("Click in this window")

        # Sets the central widget as the label object from above
        self.setCentralWidget(self.label)

        # All the following callbacks/handlers will change the text of the label given each event being passed

    # Callback function that handles the mouse press events
    def mousePressEvent(self, e):
        # If left click, then it will change the label to specific text
        if e.button() == Qt.LeftButton:

            self.label.setText('Left mouse button pressed')

        # If right click, then it will change the label to specific text
        elif e.button() == Qt.RightButton:

            self.label.setText('Right mouse button pressed')

        # If middle click, then it will change the label to specific text
        elif e.button() == Qt.MiddleButton:

            self.label.setText('Middle mouse button pressed')

    # Callback function that handles the mouse press release events
    def mouseReleaseEvent(self, e):
        # If left click released, then it will change the label to specific text
        if e.button() == Qt.LeftButton:

            self.label.setText('Left mouse button released')

        # If right click released, then it will change the label to specific text
        elif e.button() == Qt.RightButton:

            self.label.setText('Right mouse button released')

        # If middle click released, then it will change the label to specific text
        elif e.button() == Qt.MiddleButton:

            self.label.setText('Middle mouse button released')

    # Callback function that handles the mouse double click events
    def mouseDoubleClickEvent(self, e):
        # If double click left mouse button, then it will change the label to specific text
        if e.button() == Qt.LeftButton:

            self.label.setText('Left mouse button double clicked')

        # If double click right mouse button, then it will change the label to specific text
        elif e.button() == Qt.RightButton:

            self.label.setText('Right mouse button double clicked')

        # If double click middle mouse button, then it will change the label to specific text
        elif e.button() == Qt.MiddleButton:

            self.label.setText('Middle mouse button double clicked')

def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()


if __name__ == '__main__':
    createWindow()