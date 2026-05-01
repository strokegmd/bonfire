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

class RequestAuthSendCode(Request):
    ID = 0x95ed005d
    NAME = 'auth.sendCode'

    def __init__(self: 'RequestAuthSendCode', data: ByteStream) -> None:
        self.email = data.read_string()

class RequestAuthSignUp(Request):
    ID = 0x72a70570
    NAME = 'auth.signUp'

    def __init__(self: 'RequestAuthSignUp', data: ByteStream) -> None:
        self.first_name = data.read_string()
        self.last_name = data.read_string()
        self.email = data.read_string()
        self.code = data.read_string()

class RequestAuthSignIn(Request):
    ID = 0xfddda47
    NAME = 'auth.signIn'

    def __init__(self: 'RequestAuthSignIn', data: ByteStream) -> None:
        self.email = data.read_string()
        self.code = data.read_string()

class RequestAuthImport(Request):
    ID = 0xb30f307d
    NAME = 'auth.import'

    def __init__(self: 'RequestAuthImport', data: ByteStream) -> None:
        self.auth_key = data.read_bytes(512)
