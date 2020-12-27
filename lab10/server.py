"""
The script starts a server instance which is continuously receiving and accepting
connection from the multiple users.
It also takes action according to the protocol specified in the protocol.py file
on the file system created in the sub-sequent labs.
"""
import socket
import multiprocessing
import datetime
import protocol
from file_system import *


def start_server():
    """
    Starts the server and binds it to a port (5000 for me as 95 was unavailable).
    The server is continuously listening for connections from potentially multiple
    users.
    """
    # loading file system
    read_system()

    # socket pre-requisites
    host = socket.gethostname()
    port = 5000

    # binding the socket
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()

    # configuring the number of clients
    while True:
        connection, address = server_socket.accept()
        multiprocessing.Process(target=server_actions, args=(connection, address)).start()


def server_actions(connection, address):
    """
    Handle per-user commands on the file system.
    Modifies the file system according to the commands defined as per protocol and returns
    the response
    """
    files_dict = dict()  # dictionary to keep track of opened files

    print('[{}] Established connection with: '.format(datetime.datetime.now().strftime('%H:%M:%S')) + str(address))

    while True:
        data = connection.recv(2048).decode()
        if not data:
            break
        print('[{}] Message from '.format(datetime.datetime.now().strftime('%H:%M:%S')) + str(address) + ': ' + str(data))
        data = protocol.protocol(data, files_dict)
        connection.send(data.encode())

    print('[{}] Terminated connection with: '.format(datetime.datetime.now().strftime('%H:%M:%S')) + str(address))
    connection.close()


if __name__ == '__main__':
    start_server()
