from datetime import datetime

def info(text: str) -> None:
    print(f'{datetime.now().ctime()} - INFO - {text}')

def warn(text: str) -> None:
    print(f'{datetime.now().ctime()} - WARN - {text}')

def error(text: str) -> None:
    print(f'{datetime.now().ctime()} - ERROR - {text}')
