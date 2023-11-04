import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QLabel
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Sets the window title
        self.setWindowTitle("Stacked Layout Example")


        pageTestLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pageTestLayout.addLayout(buttonLayout)
        pageTestLayout.addLayout(self.stacklayout)

        # Create a button widget
        button1 = QPushButton('red')
        # Connect the button widget to a callback function
        button1.pressed.connect(self.activate_tab_1)
        # Add the widget to the button layout
        buttonLayout.addWidget(button1)
        # Add a color widget to the stacklayout
        self.stacklayout.addWidget(Color('red'))

        # Create a button widget
        button2 = QPushButton('green')
        # Connect the button widget to a callback function
        button2.pressed.connect(self.activate_tab_2)
        # Add the widget to the button layout
        buttonLayout.addWidget(button2)
        # Add a color widget to the stacklayout
        self.stacklayout.addWidget(Color('green'))

        # Create a button widget
        button3 = QPushButton('blue')
        # Connect the button widget to a callback function
        button3.pressed.connect(self.activate_tab_3)
        # Add the widget to the button layout
        buttonLayout.addWidget(button3)
        # Add a color widget to the stacklayout
        self.stacklayout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(pageTestLayout)
        self.setCentralWidget(widget)


    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)
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