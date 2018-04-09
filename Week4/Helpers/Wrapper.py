import pickle
from Message import Message


class Wrapper(object):
    @staticmethod
    def wrap(message):
        data = pickle._dumps(message)
        return data

    @staticmethod
    def unwrap(data):
        message = pickle._loads(data)
        return message
