from enum import Enum

class StateFlag(Enum):
    server_waiting_for_response = 0
    server_received_invalid_response = 1
    server_received_valid_response = 2
    server_didnt_receive_response = 3
    server_send_info = 4
    server_end_connection = 5

class Message:
    def __init__(self, header, data):
        self.header = header
        self.data = data
