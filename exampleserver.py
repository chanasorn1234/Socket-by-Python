import socket

HOST = 'localhost'
PORT = 5432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(PORT)

while True:
    print("waiting for connection")

    connection, client_address = s.accept()
    try:
        print("connection from", client_address)
        while True:
            data = connection.recv(1024)
            print("received:", data)

            if data:
                lit = data.split(',')
                print(lit)
                print("sending data back to the client")
                connection.sendall(data+'555555')
                # connection.sendall('555555')
            
            else:
                print("no more data from", client_address)
                break
    finally:
        connection.close()
        print("closed connection")