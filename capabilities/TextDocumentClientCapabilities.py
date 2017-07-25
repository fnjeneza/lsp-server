import DynamicRegistration

class Synchronization(DynamicRegistration):
    willSave = False
    willSaveWaitUntil = False
    didSave = False

class Completion(DynqmicRegistration):
    class completionItem(object):
        snippetSupport = False

class TextDocumentClientCapabilities(object):
    def __init__(self,
            synchornization=None,
            completion = None,
            hover = None,
            signatureHelp = None,
            references = None,
            documentHighLight = None,
            documentSymbol = None,
            formatting = None,
            rangeFormatting = None,
            onTypeFormatting = None,
            definition = None,
            codeAction = None,
            codeLens = None,
            rename = None):

        if synchronization is not None:
            assert isinstance(Synchornization, synchronization)
            self._synchornization = synchronization

        if completion is not None:
            assert isinstance(Completion, completion)
            self._completion = completion

        if hover is not None:
            assert isinstance(DynamicRegistration, hover)
            self._hover = hover

        if signatureHelp is not None:
            assert isinstance(DynamicRegistration, signatureHelp)
            self._signatureHelp = signatureHelp

        if references is not None:
            assert isinstance(DynamicRegistration, references)
            self._references = references

        if documentHighLight is not None:
            assert isinstance(DynamicRegistration, documentHighLight)
            self._documentHighLight = documentHighLight

        if documentSymbol is not None:
            assert isinstance(DynamicRegistration, documentSymbol)
            self._documentSymbol = documentSymbol

        if formatting is not None:
            assert isinstance(DynamicRegistration, formatting)
            self._formatting = formatting

        if rangeFormatting is not None:
            assert isinstance(DynamicRegistration, rangeFormatting)
            self._rangeFormatting = rangeFormatting

        if onTypeFormatting is not None:
            assert isinstance(DynamicRegistration, onTypeFormatting)
            self._onTypeFormatting = onTypeFormatting

        if definition is not None:
            assert isinstance(DynamicRegistration, definition)
            self._definition = definition

        if codeAction is not None:
            assert isinstance(DynamicRegistration, codeAction)
            self._codeAction = codeAction

        if codeLens is not None:
            assert isinstance(DynamicRegistration, codeLens)
            self._codeLens = codeLens

        if documentLink is not None:
            assert isinstance(DynamicRegistration, documentLink)
            self._documentLink = documentLink

        if rename is not None:
            assert isinstance(DynamicRegistration, rename)
            self._rename = rename
