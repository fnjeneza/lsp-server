
class Service:
    def __init__(self):
        session = ""

    def initialize(self, params):
        print(params)

from jsonrpc.socketserver import ThreadedTCPServiceServer

ThreadedTCPServiceServer(Service()).serve(("localhost", 5766))

