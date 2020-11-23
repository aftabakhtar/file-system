from open import Open

"""
This script will be used to perform different actions on the
file management system.
"""
PAGE_SIZE = 4096
FILE_SYSTEM = 'sample.fst'
DIR_DELIMITER = '\#dir#'
FILE_DELIMITER = '\#file#'


def read_system():
    try:
        with open(FILE_SYSTEM, 'r') as fst:
            print(fst.readline())
    except IOError:
        fst = open(FILE_SYSTEM, 'w')
        # fst.write(DIR_DELIMITER + '[test, test/test.txt]' + DIR_DELIMITER)
        fst.close()
        print('File created successfully!')


def update_system():
    pass


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


# TESTING SECTION
read_system()
