import json

global_config = None

def get_config() -> dict:
    with open('config.json', 'r') as file:
        config = json.loads(file.read())

    return config

def get_key(key: str) -> any:
    global global_config

    if not global_config:
        global_config = get_config()
    
    return global_config[key]
    