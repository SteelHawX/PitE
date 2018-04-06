import socket
import pickle
import TicTacToe

# instances of this class registers number of clients and can send or receive data from them one at
# the time and alter between them
class Server:
    # constructor
    def __init__(self):
        self.tcp_ip = '127.0.0.1'
        self.tcp_port = 5005
        self.buffer_size = 200
        self.client_info = list()
        self.clients_number = 2
        self.current_client = 0

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.tcp_ip, self.tcp_port))
        self.s.listen(1)

    # registers clients and stores their info
    def wait_for_clients(self):
        print("Waiting for players...")
        while len(self.client_info) < self.clients_number:
            conn, addr = self.s.accept()
            if addr not in self.client_info:
                self.client_info.append((addr, conn))
        print("Players found: ", self.client_info[0][0], self.client_info[1][0])

    # waits for data send by current client
    def receive(self):
        while 1:
            self.s = self.client_info[self.current_client][1].recv(self.buffer_size)
            if not self.s:
                break
            data = pickle.loads(self.s)
            return data

    # sends data to current client
    def send(self, message):
        byte_message = pickle.dumps(message)
        self.client_info[self.current_client][1].send(byte_message)

    # chooses next client as 'current'
    def next_client(self):
        self.current_client = (self.current_client + 1) % self.clients_number

    # closes all connections
    def close(self):
        for conn in self.client_info:
            conn[1].close()


if __name__ == '__main__':
    s = Server()
    s.wait_for_clients()
    s.s = s.receive()

    s.send("Welcome, you connected as first")
    s.next_client()
    s.send("Welcome, you connected as second")
    gameUI = TicTacToe.TicTacToeUI(s)
    gameUI.run()
    s.close()
