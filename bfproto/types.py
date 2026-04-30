from bfproto.bytestream import ByteStream

class Layer:
    ID = 0x57588577
    NAME = 'layer'

    def __init__(self: 'Layer', layer: int) -> None:
        self.layer = layer

    def serialize(self: 'Layer') -> bytes:
        buffer = ByteStream()
        buffer.write_int(self.ID)
        buffer.write_int(self.layer)

        return buffer.bytes
