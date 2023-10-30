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

    #All the following callbacks/handlers will change the text of the label given each event being passed

    # Callback/handler for whenever the mouse moves
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    # Callback/handler for whenever a mouse button is clicked
    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    # Callback/handler for whenever a mouse button is released after being clicked
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    # Callback/handler for whenever a mouse button is double-clicked
    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()


if __name__ == '__main__':
    createWindow()