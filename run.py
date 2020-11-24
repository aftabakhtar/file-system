"""
This script will be used to test the file system created
"""
from file_system import *

read_system()
# ch_dir('demo')
# create('lab.txt')
create('demo.txt')
# mk_dir('demo')
# move('~/demo/example', '~/demo')
# test_file = open_file('~/demo.txt')
# test_file.write_to_file(' Aftab ')
test_file = open_file('~/lab.txt')
test_file.write_to_file(' Akhtar')
# print(test_file.read_from_file(20020,5))
close_file(test_file)
list_dir()
