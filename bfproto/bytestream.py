import struct

class ByteStream:
    def __init__(self: 'ByteStream', bytes: bytes = b'', offset: int = 0) -> None:
        self.bytes = bytes
        self.offset = offset

    def read_int(self: 'ByteStream') -> int:
        result = struct.unpack_from('<I', self.bytes, self.offset)[0]
        self.offset += 4

        return result

    def read_bytes(self: 'ByteStream', amount: int) -> bytes:
        result = self.bytes[self.offset:self.offset+amount]
        self.offset += amount

        return result

    def read_string(self: 'ByteStream') -> str:
        length = self.read_int()
        return self.read_bytes(length).decode()
    
    def write_int(self: 'ByteStream', value: int) -> None:
        self.bytes += struct.pack('<I', value)
    
    def write_string(self: 'ByteStream', string: str) -> None:
        self.write_int(len(string))
        self.bytes += string.encode()

    def write_bool(self: 'ByteStream', value: bool) -> None:
        self.write_int(1 if value else 0)
