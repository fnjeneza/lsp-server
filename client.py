import socket
import asyncore

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
            return data

    def on_recv():
        """
        callback called when there is incoming data
        """
        pass

class Client2(asyncore.dispatcher_with_send):
    def __init__(self, host="localhost", port=8888):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.connect((host, port))
        self.out_buffer = bytearray()

    def handle_read(self):
        data = self.recv(1024)
        if data:
            print(data.decode())
        #call callback here
        # on receive
        pass

if __name__ == "__main__":
    #client = Client()
    #print(client.send("hello test"))

    client = Client2()
    client.send("toto2".encode())
    asyncore.loop()



