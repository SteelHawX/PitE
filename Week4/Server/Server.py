import socket
from copy import copy
import sys
sys.path.append('../Helpers')
sys.path.append('../Games')
from TicTacToe import TicTacToeUI
from Guessing import GuessingGameUI
from Message import Message
from Message import StateFlag
from Wrapper import Wrapper


# play room; handles game - client communication
class Room:
    def __init__(self, players_number, game):
        self.max_players = players_number
        self.players_connected = 0
        self.players_info = list()
        self.game = game
        self.has_game_ended = False
        self.current_player = 0
        self.buffer_size = 2024

    def has_empty_slots(self):
        if self.players_connected < self.max_players:
            return True
        else:
            return False

    def add_player(self, player):
        self.players_info.append(player)
        self.players_connected += 1
        print("Found player ", self.players_connected)
        if self.has_empty_slots() is False:
            self.start_game()

    def _send(self, message, flag):
        info_message = Message(StateFlag(flag), message)
        self.players_info[self.current_player][1].send(Wrapper.wrap(info_message))

    def _listen(self):
        data = self.players_info[self.current_player][1].recv(self.buffer_size)
        if data:
            msg = Wrapper.unwrap(data)
            return msg.data
        else:
            return "-1, -1"

    def receive_validate_insert(self):
        while 1:
            raw_input = self._listen()
            if self.game.string_is_valid(raw_input):
                true_input = self.game.string_to_input(raw_input)
                if self.game.input_values_valid(true_input):
                    self.game.insert_values(true_input)
                    break
            self._send(self.game.state_of_the_game(), 0)

    def _next_player(self):
        self.current_player = (self.current_player + 1) % self.max_players;

    def start_game(self):
        endgame_message = ""
        print("starting a game of: ", self.game.name())
        for player_index in range(self.max_players):
            self._send(self.game.initial_message(), 4)
            self._next_player()
        game_in_progress = True
        while game_in_progress:
            self._send(self.game.state_of_the_game(), 0)
            self.receive_validate_insert()
            self._send(self.game.state_of_the_game(), 4)
            if self.game.is_finished() is True:
                endgame_message = self.game.state_of_the_game()
                game_in_progress = False
            self.game.next_turn()
            self._next_player()
        for player_index in range(self.max_players):
            self._send(endgame_message, 4)
            self._next_player()
        self.has_game_ended = True



# waiting room; handles matching people in multiplayer games
class Lobby:

    def __init__(self, sock):
        self.client_info = list()
        self.s = sock
        self.buffer_size = 1024
        self.games = [TicTacToeUI(), GuessingGameUI()]
        self.game_rooms = list()
        self.s.listen(1)

    def run(self):
        while 1:
            self._clean_game_rooms()
            self.wait_for_new_connection()
            game_index = self.ask_which_game()
            game_class = self.games[game_index].__class__
            self.place_in_room(game_class())

    def wait_for_new_connection(self):
        conn, addr = self.s.accept()
        if addr not in self.client_info:
            self.client_info.append((addr, conn))
            print("Found: ", self.client_info[-1][0])

    def _clean_game_rooms(self):
        for room in self.game_rooms:
            if room.has_game_ended:
                print("Clearing finished game of ", room.game.name())
                self.game_rooms.remove(room)

    def _is_game_choice_valid(self, choice):
        if 0 <= int(choice) <= len(self.games) - 1:
            return True
        else:
            return False

    def _listen(self):
        data = self.client_info[-1][1].recv(self.buffer_size)
        if data:
            msg = Wrapper.unwrap(data)
            return msg.data
        else:
            return "-1"

    def _send(self, message):
        info_message = Message(StateFlag.server_waiting_for_response, message)
        self.client_info[-1][1].send(Wrapper.wrap(info_message))

    def ask_which_game(self):
        list_of_games = "Choose game:\n\n"
        for index in range(len(self.games)):
            list_of_games += str(index)
            list_of_games += " - "
            list_of_games += self.games[index].name()
            list_of_games += "\n"
        self._send(list_of_games)
        game_choice = self._listen()
        while self._is_game_choice_valid(game_choice) is not True:
            self._send(list_of_games)
            game_choice = self._listen()
        return int(game_choice)

    def place_in_room(self, chosen_game):
        found_room = False
        for room in self.game_rooms:
            if isinstance(room.game, type(chosen_game)) and room.has_empty_slots():
                room.add_player(self.client_info[-1])
                found_room = True
        if not found_room:
            self.game_rooms.append(Room(chosen_game.players(), chosen_game))
            self.game_rooms[-1].add_player(self.client_info[-1])



# server
class Server:

    def __init__(self):
        self.tcp_ip = '127.0.0.1'
        self.tcp_port = 5005
        self.buffer_size = 1024
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.tcp_ip, self.tcp_port))
        self.lobby = Lobby(self.s)
        self.lobby.run()


Server()