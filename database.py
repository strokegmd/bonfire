import pymongo
import config
import random
import time
import os

client = pymongo.AsyncMongoClient(config.get_key('mongo_uri'))
db = client['bonfire']

async def get_next_user_id() -> int:
    ret = await db.counters.find_one_and_update({'_id': 'user_id'}, {'$inc': {'sequence': 1}}, upsert=True, return_document=pymongo.ReturnDocument.AFTER)
    return ret['sequence']

async def get_next_chat_id() -> int:
    ret = await db.counters.find_one_and_update({'_id': 'chat_id'}, {'$inc': {'sequence': 1}}, upsert=True, return_document=pymongo.ReturnDocument.AFTER)
    return ret['sequence']

async def get_next_message_id() -> int:
    ret = await db.counters.find_one_and_update({'_id': 'message_id'}, {'$inc': {'sequence': 1}}, upsert=True, return_document=pymongo.ReturnDocument.AFTER)
    return ret['sequence']

async def is_email_registered(email: str) -> bool:
    user = await db.users.find_one({'email': email})
    return True if user else False

async def find_authorization(auth_key: bytes) -> bool:
    authorization = await db.authorizations.find_one({'auth_key': auth_key})
    return authorization

async def is_verify_code_valid(email: str, code: str) -> bool:
    code = await db.authcodes.find_one_and_delete({'email': email, 'code': code})
    return True if code and code['expiry_after'] > time.time() else False

async def send_verify_code(email: str) -> None:
    if not config.get_key('fixed_verify_code_enabled'):
        digits = int(config.get_key('verify_code_digits'))
        verify_code = str(random.randint(10 ** (digits - 1), 10 ** digits - 1))
    else:
        verify_code = config.get_key('fixed_verify_code')

    expiry_after = int(time.time()) + int(config.get_key('verify_code_expire_seconds'))
    await db.authcodes.insert_one({'email': email, 'code': verify_code, 'expiry_after': expiry_after})

async def create_user(first_name: str, last_name: str, email: str) -> None:
    await db.users.insert_one({'user_id': await get_next_user_id(), 'first_name': first_name, 'last_name': last_name, 'email': email, 'boost': False, 'username': '', 'usernames': []})

async def create_authorization(user_id: int) -> None:
    await db.authorizations.insert_one({'user_id': user_id, 'auth_key': os.urandom(512)})

async def remove_authorization(auth_key: bytes) -> None:
    await db.authorizations.delete_one({'auth_key': auth_key})

async def create_chat(owner_id: int, title: str) -> None:
    await db.chats.insert_one({'chat_id': await get_next_chat_id(), 'owner_id': owner_id, 'title': title})
