import socket
import multiprocessing


def start_server():
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
    print('Established connection with: ' + str(address))

    while True:
        data = connection.recv(2048).decode()
        if not data:
            break
        print('Message from ' + str(address) + ': ' + str(data))
        data = 'Sample data from server'
        connection.send(data.encode())

    print('Terminated connection with: ' + str(address))
    connection.close()


if __name__ == '__main__':
    start_server()
