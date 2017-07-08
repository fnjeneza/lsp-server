from lsp.LSPRequestHandler import LSPRequestHandler

def test_content_length():
    _lsp = LSPRequestHandler()
    # there is a typo in 'Length'. It will not match
    _line = "Content-Lengt: 60"
    _length = _lsp._content_length(_line)
    assert(_length == 0)
    # This time 'Length' is well written
    _line = "Content-Length: 60"
    _length = _lsp._content_length(_line)
    assert(_length == 60)

def test_content_type():
    _lsp = LSPRequestHandler()
    # No conforment line
    _line = "Content-Typ: application/vim;charset=utf-8"
    _resp = _lsp._content_type(_line)
    assert(_resp is None)
    # Conforment line
    _line = "Content-Type: application/vim;charset=utf-8"
    _resp = _lsp._content_type(_line)
    assert(_resp == "application/vim;charset=utf-8")
