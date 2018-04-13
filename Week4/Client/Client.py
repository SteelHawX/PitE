import socket
import pickle
import sys
sys.path.append("../Games")
sys.path.append('../Helpers')
from Message import Message
from Wrapper import Wrapper
from Handlers import MessageHandler
from Message import StateFlag

class Client:

    # constructor
    def __init__(self):
        self.tcp_ip = '127.0.0.1'
        self.tcp_port = 5005
        self.buffer_size = 1024
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # connects to server
    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.tcp_ip, self.tcp_port))

    # sends data
    def send(self, message):
        self.s.send(message)

    # waits for data send from the server
    def receive(self):
        while 1:
            data = self.s.recv(self.buffer_size)
            if not data:
                break
            return data

    # closes socket
    def close(self):
        self.s.close()

if __name__ == '__main__':
    c = Client()
    c.connect()
    mh = MessageHandler(c.s)
    try:
        while True:
            byte_server_message = c.receive()
            server_message = Wrapper.unwrap(byte_server_message)
            if mh.handle(server_message):
                break
    except KeyboardInterrupt:
        c.close()
        sys.exit(0)

    c.close()
    sys.exit(0)

