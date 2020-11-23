from open import Open

"""
This script will be used to perform different actions on the
file management system.
"""
PAGE_SIZE = 4096
FILE_SYSTEM = 'sample.fst'
DIR_DELIMITER = '\$dir$'
FILE_DELIMITER = '\$file$'
PROCESS_DELIMITER = '\$process$'
FRAME_DELIMITER = '\$memory$'
CWD = '~/'
DATA = dict()


def read_system():
    try:
        with open(FILE_SYSTEM, 'r') as fst:
            file_system_data = fst.read()
            get_data(file_system_data)

    except IOError:
        fst = open(FILE_SYSTEM, 'w')
        get_data(DIR_DELIMITER + CWD + '\,' + DIR_DELIMITER)
        update_system()
        fst.close()
        print('File created successfully!')


def update_system():
    global DATA
    directories = DATA['dir']
    files = DATA['files']
    process = DATA['process']
    frames = DATA['frames']

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
            for p in process:
                fst.write('%s\,' % p)
            fst.write(PROCESS_DELIMITER + '\n')

            fst.write(FRAME_DELIMITER)
            for f in frames:
                fst.write("%s\," % f)
            fst.write(FRAME_DELIMITER)
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
        DATA['process'] = file_system_data.split(PROCESS_DELIMITER)[1].split('\,')[:-1]
    except IndexError:
        DATA['process'] = []

    try:
        DATA['frames'] = file_system_data.split(FRAME_DELIMITER)[1].split('\,')[:-1]
    except IndexError:
        DATA['frames'] = []


def list_dir():
    global DATA
    directories = DATA['dir']
    files = DATA['files']

    for x in directories:
        # x = x.split(CWD)[1]
        print(u"\U0001F4C2", x)

    for x in files:
        # x = x.split(CWD)[1]
        print(u"\U0001F5C4", x)


def create(file_name):
    global DATA
    new_file = CWD + file_name

    if new_file not in DATA['files']:
        DATA['files'] += [new_file]
        update_system()
    else:
        print('create(): cannot make file due to duplicate')


def delete(file_name):
    pass


def mk_dir(dir_name):
    global DATA
    new_directory = CWD + dir_name

    if new_directory not in DATA['dir'] and new_directory not in DATA['files']:
        DATA['dir'] += [new_directory]
        update_system()
    else:
        print('mk_dir(): cannot make directory due to duplicate')


def ch_dir(dir_name):
    global CWD

    if CWD + dir_name in DATA['dir']:
        CWD = CWD + dir_name + '/'
        print('successfully changed directory to %s' % dir_name)
        print('cwd: %s' % CWD)
    else:
        print('ch_dir(): cannot change directory, it does not exist')


def move(source, destination):
    if source in DATA['files'] and destination in DATA['dir']:
        file_name = source.split('/')[-1]

        if destination.endswith('/'):
            file_name = destination + file_name
        else:
            file_name = destination + '/' + file_name

        if file_name not in DATA['dir'] and file_name not in DATA['files']:
            DATA['files'] += [file_name]
            DATA['files'].remove(source)
            update_system()
            print("successfully moved the data from {} to {}".format(source, destination))
        else:
            print("move(): make sure file names are not duplicating")

    else:
        print('move(): error, make sure that source and destination are correct')



def open_file(file_name):
    return Open(file_name)


def close_file(file_name):
    pass


def show_memory():
    pass
