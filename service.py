
class LSP(object):
    _initialized = False

    def _is_initialized(self):
        """Check if session has been initialized"""
        return self._initialized

    def _is_trace_valid(trace):
        """ Check if trace is valid"""
        traces = ["off", "messages", "verbose"]
        return trace in traces

    def initialize(self,
            processId,
            rootUri,
            initializeOptions,
            capabilities,
            rootPath = None,
            trace = "off"):
        """ Initialize is called first by the client
        Otherwise the respond for a request or notification will be -32002
        """

        assert isinstance(capabilities, ClientCapabilities):
        assert _is_trace_valid(trace):

        self._initialized = True

