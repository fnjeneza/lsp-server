class Message(object):
    def __init__(self):
        self._jsonrpc = "2.0"

    def is_valid(self):
        """Check if it is a JsonRpc version 2.0"""
        return self._jsonrpc == "2.0"

class RequestMessage(Message):
    """Request message"""
    def __init__(self, id=None, method=None, params=None):
        self._id = id,
        self._method = method
        self.params = params

    def id(self):
        return self._id

    def method(self):
        return self._method

    def params(self):
        return self._params

class ResponseMessage(Message):
    """Response message"""
    def __init__(self, id=None, result=None, error=None):
        self._id = id
        self._result = result
        self._error = error

    def id(self):
        return self._id

    def result(self):
        return self._result

    def error(self):
        return self._error

