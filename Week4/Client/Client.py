import socket
import pickle
import sys
sys.path.append("../Games")
sys.path.append('../Helpers')
from Handlers import MessageHandler

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

    # closes socket
    def close(self):
        self.s.close()

if __name__ == '__main__':
    c = Client()
    c.connect()
    mh = MessageHandler(c.s, c.buffer_size)
    try:
        while True:
            if mh.handle():
                break
    except KeyboardInterrupt:
        c.close()
        sys.exit(0)

    c.close()
    sys.exit(0)

