from bfproto.bytestream import ByteStream

class Request:
    def get_log_string(self: 'Request') -> str:
        return 'empty log string'

class RequestHelpGetLayer(Request):
    ID = 0x720d904a
    NAME = 'help.getLayer'

    def __init__(self: 'RequestHelpGetLayer', _: ByteStream) -> None:
        pass

class RequestHelpGetConfig(Request):
    ID = 0xc4f9186b
    NAME = 'help.getConfig'

    def __init__(self: 'RequestHelpGetConfig', _: ByteStream) -> None:
        pass

class RequestAuthSignUp(Request):
    ID = 0x8e571749
    NAME = 'auth.signUp'

    def __init__(self: 'RequestAuthSignUp', data: ByteStream) -> None:
        self.first_name = data.read_string()
        self.last_name = data.read_string()
        self.email = data.read_string()
        self.code = data.read_string()
