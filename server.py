import socketserver

class RequestHandler(socketserver.BaseRequestHandler):
    """
    The request handler class
    """
    def handle(self):
        """
        Handle the request
        """
        self.data = self.request.recv(1024).strip()
        print("request from {}".format(self.client_address[0]))
        print(self.data)

def run(host="localhost", port=8888):
    """Run the server"""
    server =  socketserver.TCPServer((host, port), RequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    run()
