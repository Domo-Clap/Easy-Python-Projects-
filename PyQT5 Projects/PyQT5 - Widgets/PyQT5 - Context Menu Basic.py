import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Context Menu Basic')

        self.setFixedSize(QSize(800, 600))

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction('test action 1', self))
        context.addAction(QAction('test action 2', self))
        context.addAction(QAction('test action 3', self))
        context.addAction(QAction('test action 40', self))

        context.exec(e.globalPos())

def createWindow():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Start the event loop.
    app.exec()


if __name__ == '__main__':
    createWindow()