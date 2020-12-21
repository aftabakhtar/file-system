## Thread based implementation of the file system

### How to Run
To run the project follow these steps
1. Install the requirements by `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
2. In the `lab7/thread_operations` directory make `k` files named from `0` to `k-1` which contain the commands to execute by these `k` threads (commands can be seen from the tables below)
3. To run do `python run.py <number of threads>` or `python3 run.py <number of threads>` where `number of threads` is an integer 

### Command Translation
Before going into detail, first lets look at the different commands that are passed to multiple threads for execution.
The translation tables below summarize different command, and their mapped functionality respectively.

### Command Translation Table
| Commands | Mapped Functions          | Operations                 |
| -------- | ------------------------- | -------------------------- |
| ls       | `list_dir()`              | list all directories       |
| create   | `create(file_name)`         | create a new file          |
| delete   | `delete(file_name)        ` | deletes a file             |
| mkdir    | `mk_dir(dir_name)         ` | makes a new directory      |
| cd       | `ch_dir(dir_name)          `| change directory           |
| move     | `move(source, destination)` | move a file to a directory |
| open     | `open_file(file_path)    `  | opens a file               |
| close    | `close_file(file_object)`   | closes a file              |
| mem      | `show_memory`               | shows a memory map         |

The above table specifies general commands that can be passed to execution from threads. The file specific actions table is shown below.


### File Operations Translation Table
| Commands | Mapped Functions                      | Operations                   |
| -------- | ------------------------------------- | ---------------------------- |
| write    | `write_to_file(text, at=None)         ` | write data to a file         |
| read     | `read_from_file(start=None, end=None) ` | reads data from a file       |
| move     | `move_within_file(start, size, target)` | move data with in a file     |
| truncate | `truncate_file(max_size) `              | truncate a file to some size |

Once a file is opened the commands to manipulate files would begin with the file name (for the file to modify) like if there is a file named `file1` then the command to write would be `file1.write(text_data)` etc.


### Executing Different Commands in Multiple Threads
To execute multiple different concurrent threads executing multiple different tasks, one has to follow this structure.

A directory `lab7/thread_operations` contains multiple files named from `0` to `n`. These files are used to specify commands that the respective threads would execute.

For example, the commands within the file `0` would be executed by the `thread 0` and respectively `thread 1` would execute commands in a file named `1` in that directory.

### Output of Execution
This part of our project uses a hybrid approach between reading and writing the commands from and to files and GUI. So as specified in the previous section, the threads would execute the instructions from the files
in the `thread_operations` directory, but their output would be displayed in a window which would spawn after execution. A sample window looks like


![Output Window for Threads](static/project_00.png)


**Note:** For `k` threads, `k` files are expected in `lab7/threads_operation` directory numbered from `0` to `k-1` and the program would spawn `k` windows to show execution results of the `k` threads.