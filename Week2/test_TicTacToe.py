import unittest
from TicTacToe import TicTacToeGame
from TicTacToe import TicTacToeUI

class TestTicTacToeGame(unittest.TestCase):
    """docstring forTestTicTacToeGame."""
    def setUp(self):
        self.game = TicTacToeGame()

    def test_init(self):
        self.assertEqual(self.game.gameState, [[' ', ' ', ' '], [' ', ' ', ' '],
        [' ', ' ', ' ']])
        self.assertEqual(self.game.turn, 'X')






if __name__ == "__main__":
    unittest.main()
