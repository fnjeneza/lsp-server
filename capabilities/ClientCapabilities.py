import TextDocumentClientCapabilities
import WorkspaceClientCapabilities

class ClientCapabilities(object):
    def __init__(self, workspace=None,textDocument=None, experimental=None):
        if workspace is not None:
            assert isinstance(workspace, WorkspaceClientCapabilities)
            self._workspace = workspace

        if textDocument is not None:
            assert isinstance(textDocument, TextDocumentClientCapabilities)
            self._textDocument = textDocument

        self._experimental = experimental

