import pymongo
import config
import random
import time

client = pymongo.AsyncMongoClient(config.get_key('mongo_uri'))
db = client['bonfire']
authkeys = db['authkeys']
authcodes = db['authcodes']
users = db['users']
chats = db['chats']

async def is_email_registered(email: str) -> bool:
    user = await users.find_one({'email': email})
    return True if user else False

async def is_authkey_exists(auth_key: bytes) -> bool:
    authkey = await authkeys.find_one({'authkey': auth_key})
    return True if authkey else False

async def is_auth_code_valid(email: str, code: str) -> bool:
    code = await authcodes.find_one_and_delete({'email': email, 'code': code})
    return True if code else False

async def send_verify_code(email: str) -> None:
    digits = int(config.get_key('verify_code_digits'))
    verify_code = str(random.randint(10 ** (digits - 1), 10 ** digits - 1))
    expiry_after = int(time.time()) + int(config.get_key('verify_code_expire_seconds'))

    await authcodes.insert_one({'email': email, 'verify_code': verify_code, 'expiry_after': expiry_after})

async def create_user(first_name: str, last_name: str, email: str) -> None:
    await users.insert_one({'first_name': first_name, 'last_name': last_name, 'email': email, 'boost': False, 'username': '', 'usernames': []})
