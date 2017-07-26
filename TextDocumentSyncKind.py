class TextDocumentSyncKind(object):
    None_ = 0
    Full = 1
    Incremental = 2

class CompletionOptions(object):
    resolveProvider = False
    triggerCharacters = []

class SignatureHelp(object):
    triggerCharacters = []

class CodeLensOptions(object):
    resolverProvider = False

class DocumentOnTypeFormattingOptions(object):
    #Need to be initialized
    firstTriggerCharacter
    moreTriggerCharacter = []

class DocumentLinkOptions(object):
    resolveProvide = False

class ExecuteCommandOptions(object):
    commands = []

class SaveOptions(object):
    includeText = False

class TextDocumentOptions(object):
    def __init__(self,
            openClose=False,
            change=None,
            willSave=False,
            willSaveWaitUntil=False
            save=None
            ):
        self._openClose = openClose
        self._change = change
        self._willSave = willSave
        self._willSaveWaitUntil = willSaveWaitUntil
        if save is not None:
            assert isinstance(save, SaveOptions)
            self._save = save

