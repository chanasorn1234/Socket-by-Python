import socket

HOST = 'localhost'
PORT = 5432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

s.sendall('Hello World')
s.sendall(',')
s.sendall('Hello World2')
s.sendall(',')
s.sendall('Hello World3')

data = s.recv(1024)
print('received:', repr(data))
data = s.recv(1024)
print('received:', repr(data))


    