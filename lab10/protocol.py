"""
Protocol to modify and manipulate the file system is provided in this file.
The script contains a single function which is used by the server to translate
the user entered commands to carry out operations on the file system developed
as a result of previous labs.
The function returns the string returned by the file system.
"""
from file_system import *


def protocol(action, files_opened):
    """
    Defines a translation protocol.
    Takes the command as a parameter and query the file system according to the
    command entered by the user.
    Returns the string or values returned by the file system
    """
    display_string = ''

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
        file_opened = open_file(filename)  # IMPORTANT CHANGE: moving to relative paths
        if isinstance(file_opened, Open):
            try:
                files_opened[filename] = file_opened
                display_string += 'File opened successfully'
                display_string += '\n'

            except KeyError:
                display_string += 'Exception occurred while opening'
                display_string += '\n'
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

                display_string += 'File written successfully'
                display_string += '\n'

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
                display_string += 'Successfully moved within the file'
                display_string += '\n'

            elif 'truncate' in file_action:
                size = file_action[file_action.find("(") + 1: file_action.find(")")].split(',')[0]
                file.truncate_file(size)
                display_string += 'Successfully truncated the file'
                display_string += '\n'

        except KeyError:
            display_string += 'The file required does not exists or is not opened'
            display_string += '\n'

    else:
        display_string = 'Invalid command'
        display_string += '\n'

    return display_string
