import socket

HOST=''
PORT=8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)
    # run server forever
    while True:
        # wait for a connection
        conn, addr = s.accept()

        with conn:
            print("connected to {}".format(addr))
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)