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

class ServerCapabilities(object):
    def __init__(self,
            textDocumentSync=None,
            hoverProvider=None,
            completionProvider=None,
            signatureHelpProvider=None,
            definitionProvider=None,
            referencesProvider=False,
            documentHighLightProvider=False,
            documentSymbolProvider=False,
            workspaceSymbolProvider=False,
            codeActionProvider=False,
            codeLensProvider=None,
            documentFormattingProvider=False,
            documentRangeFormattingProvider=False,
            documentOnTypeFormattingProvider=None,
            renameProvider=False,
            documentLinkProvider=None,
            executeCommandProvider=None,
            experimental=None
            )
    self._textDocumentSync = textDocumentSync
    self._hoverProvider = hoverProvider
    self._completionProvider = completionProvider
    self._signatureHelpProvider = signatureHelpProvider
    self._definitionProvider = defintionProvider
    self._referencesProvider = referencesProvider
    self._documentHightLightProvider = documentHighLightProvider
    self._documentSymbolProvider = documentSymbolProvider
    self._workspaceSymbolProvider = workspaceSymbolProvider
    self._codeActionProvider = codeActionProvider
    self._codeLensProvider = codeLensProvider
    self._documentFormattingProvider = documentFormattingProvider
    self._documentRangeFormattingProvider = documentRangeFormattingProvider
    self._documentOnTypeFormattingProvider = documentOnTypeFormattingProvider
    self._renameProvider = renameProvider
    self._documentLinkProvider = documentLinkProvider
    self._executeCommandProvider = executeCommandProvider
    self._experimental = experimental
