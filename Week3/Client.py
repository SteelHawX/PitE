import socket
import pickle


class Client:

    # constructor
    def __init__(self):
        self.tcp_ip = '127.0.0.1'
        self.tcp_port = 5005
        self.buffer_size = 1024
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connects to server
    def connect(self):
        self.s.connect((self.tcp_ip, self.tcp_port))

    # sends data
    def send(self, message):
        byte_message = pickle.dumps(message)
        self.s.send(byte_message)

    # waits for data send from the server
    def receive(self):
        while 1:
            byte_data = self.s.recv(self.buffer_size)
            if not byte_data:
                break
            data = pickle.loads(byte_data)
            return data

    # closes socket
    def close(self):
        self.s.close()

