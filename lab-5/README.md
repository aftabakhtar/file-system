# operating-system
This repository contains different parts for the CS330 Operating System course project.

## File Management System

Page Size = 4KB

The memory structure would look like following, it shows total memory usage:

| Frame Number |       Content (4KB)       |
| :----------: | :-----------------------: |
|      0       |     test.txt content      |
|      1       |    os_lab.docx content    |
|      2       |      lab.pdf content      |
|      .       |             .             |
|      6       | lab.pdf content continued |



There will also be tables for different files stored that will retain the information for all the files stored according to their frames as:

| File Stored | Frame Number |
| :---------: | :----------: |
|  test.txt   |      0       |
| os_lab.docx |      1       |
|   lab.pdf   |     2, 6     |
|      .      |      .       |
|      .      |      .       |



For directories, keep track of the current working directory and in case of mkDir, the new directory gets appended as `current_directory/new_directory`. 