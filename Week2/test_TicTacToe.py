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


    def test_insert_value(self):
        # test player X
        self.game.insert_value(0, 0)
        self.assertEqual(self.game.gameState, [['X', ' ', ' '], [' ', ' ', ' '],
        [' ', ' ', ' ']])
        self.game.insert_value(2, 2)
        self.assertEqual(self.game.gameState, [['X', ' ', ' '], [' ', ' ', ' '],
        [' ', ' ', 'X']])

        # change player to O
        self.game.turn = 'O'

        # test player O
        self.game.insert_value(0, 2)
        self.assertEqual(self.game.gameState, [['X', ' ', 'O'], [' ', ' ', ' '],
        [' ', ' ', 'X']])
        self.game.insert_value(2, 0)
        self.assertEqual(self.game.gameState, [['X', ' ', 'O'], [' ', ' ', ' '],
        ['O', ' ', 'X']])

    def test_end_players_turn(self):
        self.game.end_players_turn()
        self.assertEqual(self.game.turn, 'O')
        self.game.end_players_turn()
        self.assertEqual(self.game.turn, 'X')

        self.game.turn = '0'
        with self.assertRaises(NameError):
            self.game.end_players_turn()


    def test_is_coordinate_in_row_range(self):
        # testing coordinates in range
        self.assertTrue(self.game.is_coordinate_in_row_range(0))
        self.assertTrue(self.game.is_coordinate_in_row_range(1))
        self.assertTrue(self.game.is_coordinate_in_row_range(2))

        # testing coordinates out of range
        self.assertFalse(self.game.is_coordinate_in_row_range(-1))
        self.assertFalse(self.game.is_coordinate_in_row_range(3))
        self.assertFalse(self.game.is_coordinate_in_row_range(100))
        self.assertFalse(self.game.is_coordinate_in_row_range(-200))

    def test_is_coordinate_in_column_range(self):
        # testing coordinates in range
        self.assertTrue(self.game.is_coordinate_in_column_range(0))
        self.assertTrue(self.game.is_coordinate_in_column_range(1))
        self.assertTrue(self.game.is_coordinate_in_column_range(2))

        # testing coordinates out of range
        self.assertFalse(self.game.is_coordinate_in_column_range(-1))
        self.assertFalse(self.game.is_coordinate_in_column_range(3))
        self.assertFalse(self.game.is_coordinate_in_column_range(100))
        self.assertFalse(self.game.is_coordinate_in_column_range(-200))


if __name__ == "__main__":
    unittest.main()
