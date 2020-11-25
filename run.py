"""
This script will be used to test the file system created
"""
from file_system import *

read_system()
# ch_dir('demo')
# create('lab.txt')
# create('demo.txt')
# mk_dir('demo')
# move('~/demo/demo.txt', '~/')
test_file = open_file('~/demo.txt')
test_file.write_to_file('Aftab',50)
# test_file = open_file('~/lab.txt')
# test_file.write_to_file('Aftab is my name ')
# test_file.move_within_file(23, 23, 0)
# test_file.truncate_file(11)
# print(test_file.read_from_file())
close_file(test_file)
# delete('~/lab.txt')
# list_dir()
show_memory()
