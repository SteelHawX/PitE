from Message import Message
from Message import StateFlag
from enum import Enum
from Wrapper import Wrapper
import ClientService

class MessageHandler(object):
    def __init__(self, socket):
        self.response_data = ""
        self.socket = socket


    def handle(self, message):
        if message is not Message:
            print("message is not of type Message")
            raise TypeError

        if message.header == StateFlag.server_received_valid_response or message.header ==  StateFlag.server_send_info:
            ClientService.show_info(message.data)
        elif message.header == StateFlag.server_end_connection:
            ClientService.show_info(message.data)
            #end game
            return False
        elif message.header == StateFlag.server_waiting_for_response or message.header == StateFlag.server_received_invalid_response:
            self.response_data = ClientService.ask_user_for_input(message.data)
            self.respond_server()
        elif message.header == StateFlag.server_didnt_receive_response:
            self.respond_server()


        #continue game
        return True

    def respond_server(self):
        data = Wrapper.wrap(self.response_data)
        self.socket.send(data)

