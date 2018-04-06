import socket
import pickle
import TicTacToe

class Client:

    # constructor
    def __init__(self):
        self.tcp_ip = '127.0.0.1'
        self.tcp_port = 5005
        self.buffer_size = 1024
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ending_messages = ['Game ends with a draw!', 'You won the game!', 'You lost the game!']
        self.input_asking_messages = ['Insert index of row (0 to 2)', 'Insert index of column (0 to 2)']

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

if __name__ == '__main__':
    c = Client()
    c.connect()
    c.send('I want play a game!')
    end = False
    while not end:
        mssg = c.receive()

        if mssg in c.input_asking_messages:
            response = input(mssg)
            c.send(response)
        else:
            print(mssg)

        if mssg in c.ending_messages:
            end = True
