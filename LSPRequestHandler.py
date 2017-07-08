
class LSPRequestHandler(object):
    """Handle the request received from a client
    Extract the content length, content type and the content"""
    def __init__(self, data):
        assert(type(data) == bytes)
        data_str = data.decode("utf-8")
        # read header
        # read one line at a time
        # first non empty line must be Content-type

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

    def _read_conten(self, size):
        """Read content of the query"""
        pass
