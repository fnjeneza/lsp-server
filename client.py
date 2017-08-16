import socket

def send(message, host="localhost", port=8888):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        s.connect((host, port))
        s.sendall(bytes(message, "utf-8"))
        data = str(s.recv(1024), "utf-8")
        print("Received: {}".format(data))


if __name__ == "__main__":
    send("test")
