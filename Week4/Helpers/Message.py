from enum import Enum

class MessageType(Enum):
    coordinate_question = 0
    game_board = 1
    info = 2
    game_ending_result = 3

class Message:
    def __init__(self, type, data):
        self.type = type
        self.data = data
