from open import Open

"""
This script will be used to perform different actions on the
file management system.
"""
PAGE_SIZE = 4096
FILE_SYSTEM = 'sample.fst'
DIR_DELIMITER = '\$dir$'
FILE_DELIMITER = '\$file$'
PROCESS_TABLE = '\$process$'
MEMORY_TABLE = '\$memory$'
CWD = '~/'


def read_system():
    try:
        with open(FILE_SYSTEM, 'r') as fst:
            file_system_data = fst.read()
            list_dir(file_system_data)

    except IOError:
        fst = open(FILE_SYSTEM, 'w')
        fst.write(DIR_DELIMITER + CWD + DIR_DELIMITER)
        fst.close()
        print('File created successfully!')


def update_system():
    pass


def list_dir(file_system_data):
    try:
        directories = file_system_data.split(DIR_DELIMITER)[1].split(',')

    except IndexError:
        directories = ''

    try:
        files = file_system_data.split(FILE_DELIMITER)[1].split(',')

    except IndexError:
        files = ''

    print('Directories')
    for x in directories:
        print(x)

    print()

    for x in files:
        print(x)


def create(file_name):
    pass


def delete(file_name):
    pass


def mk_dir(dir_name):
    pass


def ch_dir(dir_name):
    pass


def move(source, destination):
    pass


def open_file(file_name):
    return Open(file_name)


def close_file(file_name):
    pass


def show_memory():
    pass
