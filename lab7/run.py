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


def spawn_window(n, data):
    app = QtWidgets.QApplication(sys.argv)
    window = text_window.TextAreaWindow(n)
    window.show()
    window.display_data(data)
    sys.exit(app.exec_())


def command_translation(path):
    files_opened = dict()
    full_path = 'thread_operations/' + str(path)
    with open(full_path) as file_name:
        file_data = file_name.read()

    display_string = ''
    for action in file_data.split('\n'):
        if action == 'ls':
            display_string += list_dir()
            display_string += '\n'

        elif 'create' in action:
            filename = action.split(' ')[1]
            display_string += create(filename)
            display_string += '\n'

        elif 'delete' in action:
            filename = action.split(' ')[1]
            display_string += delete(filename)
            display_string += '\n'

        elif 'mkdir' in action:
            dir_name = action.split(' ')[1]
            display_string += mk_dir(dir_name)
            display_string += '\n'

        elif 'cd' in action:
            dir_name = action.split(' ')[1]
            display_string += ch_dir(dir_name)
            display_string += '\n'

        elif 'move' in action:
            source = action.split(' ')[1]
            destination = action.split(' ')[2]
            display_string += move(source, destination)
            display_string += '\n'

        elif 'open' in action:
            filename = action.split(' ')[1]
            file_opened = open_file(filename) # IMPORTANT CHANGE: moving to relative paths
            if isinstance(file_opened, Open):
                try:
                    files_opened[filename] = file_opened
                except KeyError:
                    raise KeyError
            else:
                display_string += file_opened
                display_string += '\n'

        elif 'close' in action:
            filename = action.split(' ')[1]
            try:
                file_to_close = files_opened[filename]
                display_string += close_file(file_to_close)

            except KeyError:
                display_string += 'Cannot close a file that is not opened'
            display_string += '\n'

        elif action == 'mem':
            display_string += show_memory()
            display_string += '\n'

        elif '.' in action:
            filename = action.split('.')[0]
            file_action = action.split('.')[1]

            try:
                file = files_opened[filename]
                if 'write' in file_action:
                    if len(file_action[file_action.find("(") + 1: file_action.find(")")].split(',')) > 1:
                        text = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[0]
                        offset = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[1]
                        file.write_to_file(text, int(offset))
                    else:
                        text = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[0]
                        file.write_to_file(text)

                elif 'read' in file_action:
                    if file_action[file_action.find("(") + 1: file_action.find(")")] != '':
                        start = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[0]
                        end = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[1]
                        display_string += file.read_from_file(start, end)
                        display_string += '\n'
                    else:
                        display_string += file.read_from_file()
                        display_string += '\n'

                elif 'move' in file_action:
                    start = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[0]
                    size = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[1]
                    target = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[2]
                    file.move_within_file(start=start, size=size, target=target)

                elif 'truncate' in file_action:
                    size = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[0]
                    file.truncate_file(size)

            except KeyError:
                display_string += 'The file required does not exists or is not opened'

    spawn_window(str(path), display_string)


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
            multiprocessing.Process(target=command_translation, args=(i,)).start()
