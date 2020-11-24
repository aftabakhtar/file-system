"""
This script will be used to test the file system created
"""
from file_system import *

read_system()
# ch_dir('demo')
# create('example')
# mk_dir('demo')
# move('~/demo/example', '~/demo')
test_file = open_file('~/example')
test_file.write_to_file('this is a test file My name is aftab', write_at=4)
test_file.read_from_file()
# list_dir()
