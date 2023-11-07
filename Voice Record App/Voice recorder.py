import sounddevice as sd

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit

from scipy.io.wavfile import write

# Abstracted record audio function
def recordAudio():
    # Sampling frequency
    # Can be from 44100 to 48000
    freq = 44100

    # Recording Duration
    dur = 5

    # Starts the recorder
    recording = sd.rec(int(dur * freq),
                       samplerate=freq, channels=2)

    sd.wait()

    # Returns the frequency and recording array for later use
    return freq, recording

# Main class to make dialog after user has recorded audio
class MainDialog(QDialog):
    dialogClosed = QtCore.pyqtSignal()

    # Initialization function with arguments for frequency and the recording array
    def __init__(self, freq, recording):
        super().__init__()

        # Sets the freq and recording to be used later in the filename setting
        self.freq = freq
        self.recording = recording

        # Sets window title and size
        self.setWindowTitle('Finsihed!')
        self.setFixedSize(250, 150)

        # Creates layout
        self.layout = QVBoxLayout()

        # Main label creation and setup
        self.mainLabel = QLabel('Recording has finished')
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Adds a label and edit text box for the file name
        self.fileNameLabel = QLabel('Enter the file name:')
        self.fileNameEdit = QLineEdit()

        # Adds a save button for the file name
        self.saveBtn = QPushButton('Save')

        # Adds labels, edit text box, and button to layout
        self.layout.addWidget(self.mainLabel)
        self.layout.addWidget(self.fileNameLabel)
        self.layout.addWidget(self.fileNameEdit)
        self.layout.addWidget(self.saveBtn)

        # Attaches the save button to the saveFile callback
        self.saveBtn.clicked.connect(self.saveFile)

        # sets the dialogs layout to display the widgets
        self.setLayout(self.layout)

    # Save button callback
    def saveFile(self):

        # Gets file name from the edit text box and changes it into text
        fileName = self.fileNameEdit.text()

        # If the fileName is good, then it will be used to create a new wav file. Then the dialog will close
        if fileName:
            newFileName = fileName + '.wav'
            write(newFileName, self.freq, self.recording)
            self.accept()

        else:
            pass

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Sets the window title
        self.setWindowTitle("VBox Layout Example")
        self.setFixedSize(400, 200)

        # Creates a vertical box layout for the app
        layout = QVBoxLayout()

        # Creates label for the layout
        self.titleLabel = QLabel('Audio Recording Program')
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setStyleSheet('border: 2px solid black;')

        # Creates a record button
        self.startRecordBtn = QPushButton('Record')

        # Adds color widgets to the vertical layout.
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.startRecordBtn)

        # Connects the record button to the buttonAudioStart callback
        self.startRecordBtn.clicked.connect(self.buttonAudioStart)

        # Creates a overall widget that can hold the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Sets the central widget to the widget variable
        self.setCentralWidget(widget)

    # Callback for the record button
    def buttonAudioStart(self):
        # Assigns the frequency and recording array to the returned values from the recordAudio function
        freq, recording = recordAudio()
        # Sets the button text and disables it for the time being
        self.startRecordBtn.setText('Recorded')
        self.startRecordBtn.setEnabled(False)

        # Creates a mainDialog to let the user set the file name
        dialog = MainDialog(freq, recording)
        dialog.exec()

        # Used to check if the dialog is still open
        result = dialog.exec()

        # If the dialog is closed, then the enableRecordBtn callback is called
        if result == QDialog.Accepted:
            self.enableRecordBtn()

    # Used to reenable the record button after the dialog closes
    def enableRecordBtn(self):
        self.startRecordBtn.setText('Record')
        self.startRecordBtn.setEnabled(True)


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
