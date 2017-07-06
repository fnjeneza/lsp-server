import json
import jsonrpc
import socket
import uuid

class LSPRequestHandler(object):
    def __init__(self):
        pass

    def _content_length(self, line):
        """ Extract the content lenght from a the header"""
        if not line.startswith("Content-Length: "):
            print("Content is not conforment to the standard")
            return 0

        content_length = line.split(':')[-1]
        return int(content_length)

    def _content_type(self, line):
        """ Extract the content type from the header"""
        if not line.startswith("Content-Type: "):
            print("Content is not conforment to the standard")
            return None

        _, content_type = line.split("Content-Type: ")
        return content_type
