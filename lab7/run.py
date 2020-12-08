"""
This script will be used to test the file system created
"""
import sys
from file_system import *

# read_system()
# ch_dir('demo')
# create('lab.txt')
# create('demo.txt')
# mk_dir('demo')
# move('~/demo/demo.txt', '~/')
# test_file = open_file('~/demo.txt')
# test_file.write_to_file('Aftab',50)
# test_file = open_file('~/lab.txt')
# test_file.write_to_file('Aftab is my name ')
# test_file.move_within_file(23, 23, 0)
# test_file.truncate_file(11)
# print(test_file.read_from_file())
# close_file(test_file)
# delete('~/lab.txt')
# list_dir()
# show_memory()


def display_menu():
    read_system()
    print()
    print("Please make a selection from the choices below (-1 for exiting)")
    print("-" * 72)
    print("1. Create File")
    print("2. Delete File")
    print("3. Make Directory")
    print("4. Change Directory")
    print("5. Move File")
    print("6. Open File")
    print("7. Show Memory Map")
    print("8. List Directories & Files")
    choice = int(input("Choice: "))
    choice_operation(choice)


def choice_operation(choice):
    if choice == 1:
        name = str(input("Enter File Name: "))
        create(name)
        display_menu()

    elif choice == 2:
        name = str(input("Enter File Name: "))
        delete(name)
        display_menu()

    elif choice == 3:
        name = str(input("Enter File Name: "))
        mk_dir(name)
        display_menu()

    elif choice == 4:
        name = str(input("Enter Directory Name: "))
        ch_dir(name)
        display_menu()

    elif choice == 5:
        source = str(input("Enter Source Path: "))
        destination = str(input("Enter Destination Path: "))
        move(source, destination)
        display_menu()

    elif choice == 6:
        name = str(input("Enter File Name: "))
        file_opened = open_file(name)
        print("File has been opened")
        file_choice = display_file_menu()

        if file_choice == 1:
            print("Enter content")
            content = str(input())
            file_opened.write_to_file(content)
            close_file(file_opened)
            # display_file_menu()

        if file_choice == 2:
            print("Enter content")
            content = str(input())
            location = int(input("Enter location: "))
            file_opened.write_to_file(content, location)
            close_file(file_opened)
            # display_file_menu()

        if file_choice == 3:
            print(file_opened.read_from_file())
            print()
            # display_file_menu()

        if file_choice == 4:
            start = int(input("Enter start location: "))
            size = int(input("Enter size: "))
            print(file_opened.read_from_file(start, size))
            print()
            # display_file_menu()

        if file_choice == 5:
            start = int(input("Enter start location: "))
            size = int(input("Enter size: "))
            target = int(input("Enter target: "))
            file_opened.move_within_file(start, size, target)
            close_file(file_opened)
            # display_file_menu()

        if file_choice == 6:
            size = int(input("Enter truncate size: "))
            file_opened.truncate_file(size)
            close_file(file_opened)
            # display_file_menu()

        display_menu()

    elif choice == 7:
        show_memory()
        display_menu()

    elif choice == 8:
        list_dir()
        display_menu()

    elif choice == -1:
        sys.exit(0)


def display_file_menu():
    print("Select operation to perform from below")
    print("1. Write to File (Append Mode): ")
    print("2. Write to File (Overwrite Mode): ")
    print("3. Read from File (all): ")
    print("4. Read from File (start, limit): ")
    print("5. Move within File (start, size, target): ")
    print("6. Truncate File: ")
    # print("7. Close File")
    file_choice = int(input("Enter Choice: "))
    return file_choice


display_menu()
