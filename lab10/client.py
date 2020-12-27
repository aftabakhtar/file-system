"""
Provide user with an interface where they can enter an IP to connect
to the remote file system which was developed in the subsequent labs.
A wide array of commands can be queried to the file system, look at
the command translation table for commands.
The output from the server is also displayed through this script.
"""
import socket


def client():
    """
    Starts a client where user can enter commands and see the responses
    from the remote or local server.
    """
    # pre-requisites
    host = socket.gethostname()
    port = 5000

    # setting up the connection
    client_socket = socket.socket()
    client_socket.connect((host, port))

    print('Connection successfully established')
    print('Type disconnect or leave an empty line to disconnect at any time')
    message = input('->')

    while message.lower().strip() != 'disconnect' and message != '':
        client_socket.send(message.encode())
        data = client_socket.recv(2048).decode()
        print('Received from server: ' + data)
        message = input('->')

    client_socket.close()


if __name__ == '__main__':
    client()
