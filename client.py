import socket

HOST= 'localhost'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.connect((HOST, PORT))
    s.sendall(b'test')
    data = s.recv(1024)
    print("Received: {}".format(data))

