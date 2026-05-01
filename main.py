import asyncio
import config
import logger

from bfproto.bytestream import ByteStream
from handlers import handlers_map

async def handle_client(reader, writer) -> None:
    length = ByteStream(await reader.read(4)).read_int()
    if length > 4096:
        return # TODO: log

    data = ByteStream(await reader.read(length))
    constructor_id = data.read_int()
    for request in handlers_map:
        handler = handlers_map[request]
        if request.ID == constructor_id:
            request = request(data)
            logger.info(f'Received an {request.NAME} ({hex(request.ID)}) call; {request.get_log_string()}')
            
            result = await handler(request)
            response = ByteStream()
            response.write_int(len(result.serialize()))
            response.bytes += result.serialize()
            writer.write(response.bytes)

            break
    
    await writer.drain()

async def main() -> None:
    host = config.get_key('host')
    port = config.get_key('port')
    layer = config.get_key('layer')

    server = await asyncio.start_server(handle_client, host, port)
    async with server:
        logger.info(f'Started Bonfire server layer {layer} on {host}:{port}...')
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
