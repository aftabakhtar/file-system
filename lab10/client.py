import socket


def client():
    # pre-requisites
    host = socket.gethostname()
    port = 5000

    # setting up the connection
    client_socket = socket.socket()
    client_socket.connect((host, port))

    print('Connection successfully established')
    print('Type disconnect to disconnect at any time')
    message = input('->')

    while message.lower().strip() != 'disconnect':
        client_socket.send(message.encode())
        data = client_socket.recv(2048).decode()
        print('Received from server: ' + data)
        message = input('->')

    client_socket.close()


if __name__ == '__main__':
    client()
