from Message import Message
from Message import MessageType
from enum import Enum
from Wrapper import Wrapper
import ClientService

class MessageHandler(object):
    move = (-1, -1)
    
    @staticmethod
    def handle(message):
        if message.type == MessageType.coordinate_question:
            MessageHandler.move = (ClientService.ask_user_for_row(), ClientService.ask_user_for_column())
            # need to send response to server
            return 1
        elif message.type == MessageType.game_board:
            ClientService.draw_game(message.data)
        elif message.type == MessageType.info:
            ClientService.show_info(message.data)
        elif message.type == MessageType.game_ending_result:
            ClientService.show_info(message.data)
            # end game
            return 0
        
        #continue game
        return True
    
    @staticmethod
    def respond_server(socket, message):
        if message.type == MessageType.coordinate_question:
            data = Wrapper.wrap(MessageHandler.move)
            socket.send(message)

