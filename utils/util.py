import uuid
import datetime


def get_uuid(bit: int=4):
    return str(uuid.uuid4())[:bit]

def get_now():
    return f"{datetime.datetime.now():%Y-%m-%d_%H%M%S}"