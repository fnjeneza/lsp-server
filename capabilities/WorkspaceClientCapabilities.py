
class WorkspaceEdit:
    documentChanges = False

class DynamicRegistration:
    dynamicRegistration = False

class WorkspaceClientCapabilities(object):
    def __init__(self,
            applyEdit=False,
            workspaceEdit=None,
            didChangeConfiguration=None,
            didChangeWatchedFiles=None,
            symbol=None,
            executeCommand=None):
        self._applyEdit = applyEdit

        if workspace is not None:
            assert(isinstance(WorkspaceEdit, workspaceEdit))
            self._workspaceEdit = workspaceEdit

        if didChangeConfiguration is not None:
            assert(isinstance(DynamicRegistration, didChangeConfiguration))
            self._didChangeConfiguration = didChangeConfiguration

        if didChangeWatchedFiles is not None:
            assert(isinstance(DynamicRegistration, didChangeWatchedFiles))
            self._didChangeWatchedFiles = didChangeWatchedFiles

        if symbol is not None:
            assert(isinstance(DynamicRegistration, symbol))
            self._symbol = symbol

        if executeCommand is not None:
            assert(isinstance(DynamicRegistration,executeCommand))
            self._executeCommand = executeCommand
