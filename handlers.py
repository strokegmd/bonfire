import database
import config
import logger

from bfproto.types import *
from bfproto.requests import *

async def get_layer(_: RequestHelpGetLayer) -> Layer:
    return Layer(config.get_key('layer'))

async def send_code(request: RequestAuthSendCode) -> Ok:
    return Ok()

async def sign_up(request: RequestAuthSignUp) -> User:
    return User(request.first_name, request.last_name, '', False, [])

handlers_map = {
    RequestHelpGetLayer: get_layer,
    RequestAuthSendCode: send_code,
    RequestAuthSignUp: sign_up
}

for request in handlers_map:
    logger.info(f'Registered a new handler: {request.NAME} ({hex(request.ID)}).')

logger.info(f'Total count of handlers registered: {len(handlers_map)}.')
