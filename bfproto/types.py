from bfproto.bytestream import ByteStream

class BFObject:
    def serialize(self: 'BFObject') -> bytes:
        return b''

class Ok(BFObject):
    ID = 0xd4edbe69
    NAME = 'ok'

class Error(BFObject):
    ID = 0x0
    NAME = 'error'

    def __init__(self: 'Error', message: str) -> None:
        self.message = message

    def serialize(self: 'Error') -> bytes:
        buffer = ByteStream()
        buffer.write_int(self.ID)
        buffer.write_string(self.message)
        
        return buffer.bytes

class Vector(BFObject):
    ID = 0xf7b13c2e
    NAME = 'vector'

    def __init__(self: 'Vector', items: list[BFObject]) -> None:
        self.items = items
        self.count = len(self.items)

    def serialize(self: 'Vector') -> bytes:
        buffer = ByteStream()
        buffer.write_int(self.ID)
        buffer.write_int(self.count)

        for item in self.items:
            buffer.bytes += item.serialize()
        
        return buffer.bytes

class Layer(BFObject):
    ID = 0x57588577
    NAME = 'layer'

    def __init__(self: 'Layer', layer: int) -> None:
        self.layer = layer

    def serialize(self: 'Layer') -> bytes:
        buffer = ByteStream()
        buffer.write_int(self.ID)
        buffer.write_int(self.layer)

        return buffer.bytes

class Username(BFObject):
    ID = 0x3b680427
    NAME = 'username'

    def __init__(self: 'Username', username: str) -> None:
        self.username = username

    def serialize(self: 'Username') -> bytes:
        buffer = ByteStream()
        buffer.write_int(self.ID)
        buffer.write_string(self.username)

        return buffer.bytes

class User(BFObject):
    ID = 0x30bf4f2d
    NAME = 'user'

    def __init__(self: 'User', first_name: str, last_name: str, about: str, username: str, boost: bool, usernames: list[Username]) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.about = about
        self.username = username
        self.boost = boost
        self.usernames = usernames
    
    def serialize(self: 'User') -> bytes:
        buffer = ByteStream()
        buffer.write_int(self.ID)
        buffer.write_string(self.first_name)
        buffer.write_string(self.last_name)
        buffer.write_string(self.last_name)
        buffer.write_string(self.about)
        buffer.write_string(self.username)
        buffer.write_bool(self.boost)
        buffer.bytes += Vector(self.usernames).serialize()

        return buffer.bytes

class ErrorEmailAlreadyOccupied(Error):
    def __init__(self: 'Error') -> None:
        super().__init__('EMAIL_ALREADY_OCCUPIED')

class ErrorAuthKeyInvalid(Error):
    def __init__(self: 'Error') -> None:
        super().__init__('AUTH_KEY_INVALID')

class ErrorEmailAlreadyOccupied(Error):
    def __init__(self: 'Error') -> None:
        super().__init__('EMAIL_ALREADY_OCCUPIED')

class ErrorVerifyCodeInvalid(Error):
    def __init__(self: 'Error') -> None:
        super().__init__('VERIFY_CODE_INVALID')

class ErrorEmailUnoccupied(Error):
    def __init__(self: 'Error') -> None:
        super().__init__('EMAIL_UNOCCUPIED')

class ErrorEmailInvalid(Error):
    def __init__(self: 'Error') -> None:
        super().__init__('EMAIL_INVALID')

class ErrorVerifyCodeExpired(Error):
    def __init__(self: 'Error') -> None:
        super().__init__('VERIFY_CODE_EXPIRED')
