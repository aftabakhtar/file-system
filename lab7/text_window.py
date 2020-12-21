from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit


class TextAreaWindow(QMainWindow):
    def __init__(self, n):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(800, 600))
        self.setMaximumSize(QSize(800, 600))
        self.setWindowTitle("Thread " + str(n))

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.move(10, 10)
        self.b.resize(780, 580)
        self.b.setReadOnly(True)

    def display_data(self, data):
        self.b.insertPlainText(data)
