"""
This python script is used to spawn multiple windows to test
the multi-threaded (multi-processed) interface to our file-
system developed in the last lab.
"""
import sys
import text_window
import multiprocessing
from PyQt5 import QtWidgets
from file_system import *


def operation(n, data):
    app = QtWidgets.QApplication(sys.argv)
    window = text_window.TextAreaWindow(n)
    window.show()
    window.display_data(data)
    sys.exit(app.exec_())


def process_file(path):
    full_path = 'thread_operations/' + str(path)
    with open(full_path) as file_name:
        file_data = file_name.read()

    for action in file_data.split('\n'):
        exec(action)

    exec('operation(path, data)')


if __name__ == "__main__":
    read_system()
    argument = None
    if len(sys.argv) == 1:
        print("correct usage: python3 run.py <number of threads>")
    elif len(sys.argv) == 2:
        argument = int(sys.argv[1])
    else:
        print("correct usage: python3 run.py <number of threads>")

    if argument is not None:
        for i in range(argument):
            multiprocessing.Process(target=process_file, args=(i,)).start()
