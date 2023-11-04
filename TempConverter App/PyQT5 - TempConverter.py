from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

import sys


def far_to_cel(faren):
    celsius = (faren - 32) * 5 / 9
    return celsius

class MainWindow(QWidget):
    # Runs when an object instance of the class is created
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Sets the window title
        self.setWindowTitle('Temp Converter')

        # Creates a layout for the label and input box to be placed in
        layout = QVBoxLayout()

        # Creates a label in the application
        self.label1 = QLabel('Enter a Farenheit temp value')
        # Creates an input text box in the application
        self.input = QLineEdit()
        self.actionBtn = QPushButton('Convert')
        self.label2 = QLabel('Converted Temp: ')

        # Connects the action of the text being changed to the setText function for a label widget
        self.actionBtn.clicked.connect(self.convert_temp)

        # Adds the two widgets to the layout
        layout.addWidget(self.label1)
        layout.addWidget(self.input)
        layout.addWidget(self.actionBtn)
        layout.addWidget(self.label2)

        # Sets the container as the central widget for the app
        self.setLayout(layout)

    def convert_temp(self):
        faren = float(self.input.text())
        celsius = far_to_cel(faren)
        self.label2.setText(f'Result: {celsius:.2f} °C')

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