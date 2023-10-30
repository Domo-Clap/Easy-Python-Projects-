import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Sets the window title
        self.setWindowTitle("First Layout Example")

        # Creates a vertical box layout for the app
        layout = QHBoxLayout()

        # Adds color widgets to the vertical layout.
        layout.addWidget(Color('red'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('purple'))
        layout.addWidget(Color('pink'))

        # Creates a overall widget that can hold the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Sets the central widget to the widget variable
        self.setCentralWidget(widget)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()

        # Sets it so the background auto fills with a single color
        self.setAutoFillBackground(True)

        # Creates a variable to hold the current palette/background color
        palette = self.palette()

        # Changes the new color to whatever is passed in when the color is made
        palette.setColor(QPalette.Window, QColor(color))

        # Changes the color of the current object to the new color stored in the palette variable
        self.setPalette(palette)


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