import unittest
import sys
sys.path.append("../Server")
sys.path.append("../Games")
sys.path.append("../Exceptions")
from Server import Server
from Server import Room
from Server import Lobby
import ServerExceptions as se
from TicTacToe import TicTacToeUI
from Guessing import GuessingGameUI
from unittest.mock import MagicMock
from socket import socket


class RoomTicTacToeTestCase(unittest.TestCase):
    def setUp(self):
        self.room = Room(TicTacToeUI.players(), TicTacToeUI())

    def test_init_values(self):
        self.assertTrue(isinstance(self.room.game, type(TicTacToeUI())), "incorrect game type")
        self.assertEqual(self.room.max_players, TicTacToeUI.players(), "incorrect number of max players")
        self.assertEqual(self.room.players_connected, 0, "incorrect number of connected players")
        self.assertEqual(self.room.players_info, list(), "incorrect players info type")
        self.assertFalse(self.room.has_game_ended, "incorrect game in progress flag value")
        self.assertEqual(self.room.buffer_size, 2024, "incorrect buffer size")

    def test_empty_slots_check(self):

        self.room.players_connected = 0
        self.assertTrue(self.room.has_empty_slots())

        self.room.players_connected = 1
        self.assertTrue(self.room.has_empty_slots())

        self.room.players_connected = 2
        self.assertFalse(self.room.has_empty_slots())

        self.room.players_connected = 3
        self.assertRaises(se.TooManyPlayersError)

    def test_add_player(self):
        pass

    def test_next_player(self):
        self.room.current_player = 0
        self.room._next_player()
        self.assertEqual(self.room.current_player, 1)

        self.room.current_player = 1
        self.room._next_player()
        self.assertEqual(self.room.current_player, 0)


class RoomGuessingTestCase(unittest.TestCase):
    def setUp(self):
        self.room = Room(GuessingGameUI.players(), GuessingGameUI())

    def test_init_values(self):
        self.assertTrue(isinstance(self.room.game, type(GuessingGameUI())), "incorrect game type")
        self.assertEqual(self.room.max_players, GuessingGameUI.players(), "incorrect number of max players")
        self.assertEqual(self.room.players_connected, 0, "incorrect number of connected players")
        self.assertEqual(self.room.players_info, list(), "incorrect players info type")
        self.assertFalse(self.room.has_game_ended, "incorrect game in progress flag value")
        self.assertEqual(self.room.buffer_size, 2024, "incorrect buffer size")

    def test_empty_slots_check(self):
        self.room.players_connected = 0
        self.assertTrue(self.room.has_empty_slots())

        self.room.players_connected = 1
        self.assertFalse(self.room.has_empty_slots())

        self.room.players_connected = 2
        self.assertRaises(se.TooManyPlayersError)

    def test_add_player(self):
        pass

    def test_next_player(self):
        self.room.current_player = 0
        self.room._next_player()
        self.assertEqual(self.room.current_player, 0)


if __name__ == '__main__':
    unittest.main()
