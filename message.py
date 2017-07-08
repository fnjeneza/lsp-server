class Message(object):
    jsonrpc = ""

    def is_valid(self):
        """Check if it is a JsonRpc version 2.0"""
        return jsonrpc == "2.0"
