import database
import config
import logger

from bfproto.types import *
from bfproto.requests import *

async def get_layer(_: RequestHelpGetLayer) -> Layer:
    return Layer(config.get_key('layer'))

async def send_code(request: RequestAuthSendCode) -> Ok | Error:
    if False:
        return ErrorEmailInvalid() # TODO: email check not implemented

    await database.send_verify_code(request.email)
    return Ok()

async def sign_up(request: RequestAuthSignUp) -> Authorization | Error:
    if False:
        return ErrorEmailInvalid() # TODO: email check not implemented

    if await database.is_email_registered(request.email):
        return ErrorEmailAlreadyOccupied()
    
    if not await database.is_verify_code_valid(request.email, request.code):
        return ErrorVerifyCodeInvalid()

    if len(request.first_name) > config.get_key('username_max_length') or len(request.last_name) > config.get_key('username_max_length'):
        return ErrorStringTooLong()
    
    if not request.first_name or not request.last_name:
        return ErrorStringEmpty()
    
    await database.create_user(request.first_name, request.last_name, request.email)
    return Authorization(b'123', User(request.first_name, request.last_name, '', False, []))

async def sign_in(request: RequestAuthSignIn) -> Authorization | Error:
    if False:
        return ErrorEmailInvalid() # TODO: email check not implemented

    if not await database.is_email_registered(request.email):
        return ErrorEmailUnoccupied()

    if not await database.is_verify_code_valid(request.email, request.code):
        return ErrorVerifyCodeInvalid()
    
    return Authorization(b'123', User(request.first_name, request.last_name, '', False, []))

async def import_authorization(request: RequestAuthImport) -> Authorization | Error:
    authorization = await database.find_authorization(request.auth_key)
    if not authorization:
        return ErrorAuthKeyInvalid()

    return Authorization(b'123', User(request.first_name, request.last_name, '', False, []))

handlers_map = {
    RequestHelpGetLayer: get_layer,
    RequestAuthSendCode: send_code,
    RequestAuthSignUp: sign_up,
    RequestAuthSignIn: sign_in,
    RequestAuthImport: import_authorization
}

for request in handlers_map:
    logger.info(f'Registered a new handler: {request.NAME} ({hex(request.ID)}).')

logger.info(f'Total count of handlers registered: {len(handlers_map)}.')
