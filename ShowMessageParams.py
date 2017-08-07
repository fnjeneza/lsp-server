class MessageType(object):
    Error = 1
    Warning = 2
    Info = 3
    Log = 4

class MessageActionItem(object):
    title = ""

class ShowMessageParams(object):
    def __init__(self, type_, message):
        if(type_ is not None):
            assert isinstance(type_, MessageType)
            self._type_ = type_
        if message is not None:
            assert isinstance(message, str)
            self._message = message


class ShowMessageRequestParams(ShowMessageParams):
    def __init__(self, type_, message, actions):
        super(type_, message)

        if actions is not None:
            assert isinstance(actions, MessageActionItem)
            self._actions = actions



