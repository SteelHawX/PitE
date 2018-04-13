from Message import Message
from Message import StateFlag
from enum import Enum
from Wrapper import Wrapper
import ClientService


class MessageHandler(object):
    def __init__(self, socket, buffer_size):
        self.socket = socket
        self.response_data = ""
        self.buffer_size = buffer_size

    def handle(self):
        message = self.receive()
        if not isinstance(message, Message):
            print(type(message))
            print("message is not of type Message")
            raise TypeError

        if message.header is StateFlag.server_received_valid_response or message.header is  StateFlag.server_send_info:
            ClientService.show_info(message.data)
        elif message.header is StateFlag.server_end_connection:
            ClientService.show_info(message.data)
            #end game
            return True
        elif message.header is StateFlag.server_waiting_for_response or message.header is StateFlag.server_received_invalid_response:
            self.response_data = ClientService.ask_user_for_input(message.data)
            self.respond_server()
        elif message.header is StateFlag.server_didnt_receive_response:
            self.respond_server()


        #continue game
        return False

    def respond_server(self):
        response_data = Message(0, self.response_data)
        data = Wrapper.wrap(response_data)
        self.socket.send(data)

    # waits for data send from the server
    def receive(self):
        while 1:
            data = self.socket.recv(self.buffer_size)
            if not data:
                break
            mess = Wrapper.unwrap(data)
            return mess

