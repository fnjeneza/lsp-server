import socket

class Client(object):
    def __init__(self, host="localhost", port = 8888):
        self._server_address = (host, port)
        self._encoding = "utf-8"

    # TODO make this a wrapper
    def send(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
            s.connect(self._server_address)
            s.sendall(bytes(message, self._encoding))
            data = str(s.recv(1024), self._encoding)
            print("Received: {}".format(data))

    def on_recv():
        """
        callback called when there is incoming data
        """
        pass


if __name__ == "__main__":
    client = Client()
    client.send("hello test")



