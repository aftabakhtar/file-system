"""
This python script is used to spawn multiple windows to test
the multi-threaded (multi-processed) interface to our file-
system developed in the last lab.
"""
import sys
import tkinter as tk
import multiprocessing
import threading
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit
from file_system import *


class TextAreaWindow(QMainWindow):
    def __init__(self, n, text):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(800, 520))
        self.setWindowTitle("Thread " + str(n))

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText(text)
        self.b.move(10, 10)
        self.b.resize(780, 500)
        self.b.setReadOnly(True)


def operation(n):
    create('file1')
    file_opened = open_file('~/file1')
    file_opened.write_to_file('This is some sample content written by thread ' + str(n), 0)
    data = file_opened.read_from_file()
    close_file(file_opened)
    app = QtWidgets.QApplication(sys.argv)
    window = TextAreaWindow(n, data)
    window.show()
    sys.exit(app.exec_())
    # root = tk.Tk()
    # t = tk.Text(root, height=10, width=50)
    # t.pack()
    # t.insert(tk.END, data)
    # tk.mainloop()


if __name__ == "__main__":
    read_system()
    argument = None
    if len(sys.argv) == 1:
        print("correct usage: python3 run_threaded.py <number of threads>")
    elif len(sys.argv) == 2:
        argument = int(sys.argv[1])
    else:
        print("correct usage: python3 run_threaded.py <number of threads>")

    if argument is not None:
        for i in range(argument):
            multiprocessing.Process(target=operation, args=(i,)).start()
