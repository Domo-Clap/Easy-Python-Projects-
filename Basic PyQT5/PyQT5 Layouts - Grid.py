import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Sets the window title
        self.setWindowTitle("Grid Layout Example")

        # Creates two buttons to be added to layout
        button = QPushButton('Click me!!!')
        button2 = QPushButton('Or Click me!!!')

        # Creates label for layout
        label = QLabel('Look at me though')

        # Creates grid layout
        layout = QGridLayout()

        # Adds all of the widgets to the layout given row/column positions
        layout.addWidget(Color('purple'), 0, 0)
        layout.addWidget(Color('red'), 1, 1)
        layout.addWidget(Color('green'), 2, 2)
        layout.addWidget(button, 3, 0)
        layout.addWidget(button2, 4, 2)
        layout.addWidget(label, 1, 0)


        widget = QWidget()
        widget.setLayout(layout)
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