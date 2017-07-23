class ClientCapabilities(object):
    def __init__(self, workspace=None,textDocument=None, experimental=None):
        if workspace is not None:
            assert isinstance(workspace, WorkspaceClientCapabilities)
            _workspace = workspace

        if textDocument is not None:
            assert isinstance(textDocument, TextDocumentClientCapabilities)
            _textDocument = textDocument

        _experimental = experimental

