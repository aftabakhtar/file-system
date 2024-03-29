import ast
from open import Open
import threading

"""
This script will be used to perform different actions on the
file management system.
"""
PAGE_SIZE = 16
FILE_SYSTEM = 'sample.fst'
DIR_DELIMITER = '\$dir$'
FILE_DELIMITER = '\$file$'
PROCESS_DELIMITER = '\$process$'
FRAME_DELIMITER = '\$memory$'
CLEAR_DELIMITER = '\$clear$'
CWD = '~/'
DATA = dict()
SYNC = dict()
READERS = []
WRITERS = []
system_lock = threading.Semaphore()


def read_system():
    try:
        with open(FILE_SYSTEM, 'r') as fst:
            file_system_data = fst.read()
            get_data(file_system_data)
            # read_sync_data()

    except IOError:
        fst = open(FILE_SYSTEM, 'w')
        get_data(DIR_DELIMITER + CWD + '\,' + DIR_DELIMITER)
        update_system()
        fst.close()
        # read_sync_data()
        print('File created successfully!')


def update_system():
    global DATA
    directories = DATA['dir']
    files = DATA['files']
    process = DATA['process']
    frames = DATA['frames']
    clears = DATA['clear']

    # print(directories, files, process, frames)

    try:
        with open(FILE_SYSTEM, 'w') as fst:
            fst.write(DIR_DELIMITER)
            for directory in directories:
                fst.write("%s\," % directory)
            fst.write(DIR_DELIMITER + '\n')

            fst.write(FILE_DELIMITER)
            for file in files:
                fst.write("%s\," % file)
            fst.write(FILE_DELIMITER + '\n')

            fst.write(PROCESS_DELIMITER)
            fst.write(str(process))
            fst.write(PROCESS_DELIMITER + '\n')

            fst.write(FRAME_DELIMITER)
            fst.write(str(frames))
            fst.write(FRAME_DELIMITER + '\n')

            fst.write(CLEAR_DELIMITER)
            for c in clears:
                fst.write("%s\," % c)
            fst.write(CLEAR_DELIMITER)
    except IOError as e:
        raise e
        print('Cannot update system due to some error')


def get_data(file_system_data):
    global DATA

    try:
        DATA['dir'] = file_system_data.split(DIR_DELIMITER)[1].split('\,')[:-1]
    except IndexError:
        DATA['dir'] = []

    try:
        DATA['files'] = file_system_data.split(FILE_DELIMITER)[1].split('\,')[:-1]
    except IndexError:
        DATA['files'] = []

    try:
        DATA['process'] = ast.literal_eval(file_system_data.split(PROCESS_DELIMITER)[1])
    except IndexError:
        DATA['process'] = {}

    try:
        DATA['frames'] = ast.literal_eval(file_system_data.split(FRAME_DELIMITER)[1])
    except IndexError:
        DATA['frames'] = {}

    try:
        DATA['clear'] = file_system_data.split(CLEAR_DELIMITER)[1].split('\,')[:-1]
    except IndexError:
        DATA['clear'] = []


def list_dir():
    global DATA
    directories = DATA['dir']
    files = DATA['files']
    out_list = 'Directories \n'

    for x in directories:
        # x = x.split(CWD)[1]
        # print(u"\U0001F4C2", x)
        out_list += str(x) + '\n'

    out_list += '\nFiles\n'
    for x in files:
        # x = x.split(CWD)[1]
        # print(u"\U0001F5C4", x)
        out_list += str(x) + '\n'

    return out_list


def create(file_name):
    global system_lock
    global DATA
    global SYNC

    system_lock.acquire()

    new_file = CWD + file_name

    if new_file not in DATA['files'] and DATA['dir']:
        DATA['files'] += [new_file]
        DATA['process'][new_file] = []  # IMPORTANT CHANGE: moving to relative paths
        update_system()

        SYNC[new_file] = [threading.Semaphore(), threading.Semaphore(), 0, threading.Semaphore()]
        system_lock.release()
        return 'create(): file created successfully'
    else:
        system_lock.release()
        return 'create(): cannot make file due to duplicate'


def delete(file_name):
    global system_lock
    global DATA
    global SYNC
    # IMPORTANT CHANGE: moving to relative paths
    global CWD

    system_lock.acquire()

    file_name = CWD + file_name

    if file_name in DATA['files']:
        process_storage = DATA['process'][file_name]
        del DATA['process'][file_name]
        for i in process_storage:
            DATA['clear'] += [i]
            del DATA['frames'][i]
        DATA['files'].remove(file_name)
        update_system()

        del SYNC[file_name]
        system_lock.release()
        return 'successfully deleted %s' % file_name
    else:
        system_lock.release()
        return 'delete(): make sure file name or path is correct'


def mk_dir(dir_name):
    global system_lock
    global DATA

    system_lock.acquire()

    new_directory = CWD + dir_name

    if new_directory not in DATA['dir'] and new_directory not in DATA['files']:
        DATA['dir'] += [new_directory]
        update_system()
        system_lock.release()
        return 'mk_dri(): directory created successfully'
    else:
        system_lock.release()
        return 'mk_dir(): cannot make directory due to duplicate'


def ch_dir(dir_name):
    global CWD

    if dir_name in DATA['dir']:
        if dir_name == '~/':
            CWD = dir_name
        else:
            CWD = dir_name + '/'
        return 'successfully changed directory to %s' % dir_name
        # print('cwd: %s' % CWD)
    else:
        return 'ch_dir(): cannot change directory, it does not exist'


def move(source, destination):
    global system_lock
    system_lock.acquire()

    if source in DATA['files'] and destination in DATA['dir']:
        file_name = source.split('/')[-1]

        if destination.endswith('/'):
            file_name = destination + file_name
        else:
            file_name = destination + '/' + file_name

        if file_name not in DATA['dir'] and file_name not in DATA['files']:
            DATA['files'] += [file_name]
            DATA['files'].remove(source)
            DATA['process'][file_name] = DATA['process'].pop(source) # updating to new dictionary key
            update_system()
            system_lock.release()
            return "successfully moved the data from {} to {}".format(source, destination)
        else:
            system_lock.release()
            return "move(): make sure file names are not duplicating"

    else:
        system_lock.release()
        return 'move(): error, make sure that source and destination are correct'


def open_file(file_name, permission):
    # IMPORTANT CHANGE: moving to relative paths
    global SYNC
    global READERS
    global WRITERS
    global CWD
    file_name = CWD + file_name

    if file_name in DATA['files']:
        if str(permission).lower() == 'w':
            # handle the write synchronization here
            # if file_name not in WRITERS:
            #     WRITERS += [file_name]
            # no reader after writer
            SYNC[file_name][3].acquire()

            SYNC[file_name][1].acquire()
            WRITERS += [file_name]

            return Open(file_name, DATA, str(permission).lower())

        elif str(permission).lower() == 'r':
            # handle the read synchronization here

            # no readers after writer
            SYNC[file_name][3].acquire()

            SYNC[file_name][0].acquire()
            SYNC[file_name][2] += 1

            if SYNC[file_name][2] == 1:
                SYNC[file_name][1].acquire()

            SYNC[file_name][0].release()

            # no readers after writer
            SYNC[file_name][3].release()

            return Open(file_name, DATA, str(permission).lower())

        else:
            return 'Invalid permission specified'
    else:
        return 'open_file(): invalid path or file_name'


def close_file(file_name):
    global SYNC
    global WRITERS
    global READERS
    # print(DATA)

    # writer
    if file_name.get_path() in WRITERS:
        SYNC[file_name.get_path()][1].release()
        WRITERS.remove(file_name.get_path())

        # no reader after writer
        SYNC[file_name.get_path()][3].release()

    # reader: we may need to add something in the READER list
    else:
        SYNC[file_name.get_path()][0].acquire()
        SYNC[file_name.get_path()][2] -= 1

        if SYNC[file_name.get_path()][2] == 0:
            SYNC[file_name.get_path()][1].release()

        SYNC[file_name.get_path()][0].release()

    data = file_name.close()
    global DATA
    DATA = data
    update_system()
    return 'system updated successfully!'


def show_memory():
    memory_map = '=' * 40 + '\n'
    memory_map += 'Process / Data Table\n'
    memory_map += '=' * 40 + '\n'

    for p in DATA['process']:
        memory_map += (str(p) + '\t\t' + str(DATA['process'][p])) + '\n'

    memory_map += '\n' + '=' * 40 + '\n'
    memory_map += 'Memory Table' + '\n'
    memory_map += '=' * 40 + '\n'

    for p in DATA['frames']:
        memory_map += (str(p) + '\t\t' + DATA['frames'][p]) + '\n'

    memory_map += '\n' + '=' * 40 + '\n'
    memory_map += 'Cleared Memory Table' + '\n'
    memory_map += '=' * 40 + '\n'

    for p in DATA['clear']:
        memory_map += ('Clear Frames:' + '\t\t' + str(p)) + '\n'

    return memory_map


def read_sync_data():
    global DATA
    global SYNC
    files = DATA['files']
    for file in files:
        SYNC[file] = [threading.Semaphore(), threading.Semaphore(), 0, threading.Semaphore()]


def print_sync_data():
    global SYNC
    return str(SYNC)
