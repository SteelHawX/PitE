import unittest
import sys
sys.path.append("../Server")
from Server import Server
from Server import Room
from Server import Lobby

class RoomTicTacToeTestCase(unittest.TestCase):
	def SetUp(self):
		self.room = Room(TicTacToe.players(), TicTacToe())

	def test_init_values(self):
		self.assertEqual(self.room.game, TicTacToe(), "incorrect game type" )
		self.assertEqual(self.room.max_players, TicTacToe.players(), "incorrect number of max players")
		self.assertEqual(self.room.players_connected, 0, "incorrect number of connected players")
		self.assertEqual(self.room.players_info, list(), "incorrect players info type")
		self.assertFalse(self.room.has_game_ended, "incorrect game in progress flag value")
		self.assertEqual(self.room.buffer_size, 2024, "incorrect buffer size")

if __name__ == '__main__':
	unittest.main()
