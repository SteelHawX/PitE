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

    def test_is_empty(self):
        self.game.gameState = [['X', ' ', 'O'], [' ', ' ', ' '],
        ['O', ' ', 'X']]

        # testing empty boxes
        self.assertTrue(self.game.is_empty(0, 1))
        self.assertTrue(self.game.is_empty(1, 2))

        # testing not empty boxes
        self.assertFalse(self.game.is_empty(0, 0))
        self.assertFalse(self.game.is_empty(2, 0))

    def test_is_board_full(self):
        self.assertFalse(self.game.is_board_full())

        self.game.gameState = [['X', ' ', 'O'], [' ', ' ', ' '],
        ['O', ' ', 'X']]

        self.assertFalse(self.game.is_board_full())

        self.game.gameState = [[' ', 'X', 'O'], ['O', 'X', 'X'],
        ['O', 'O', 'X']]

        self.assertFalse(self.game.is_board_full())

        self.game.gameState = [['X', 'X', 'O'], ['O', 'X', 'X'],
        ['O', 'O', ' ']]

        self.assertFalse(self.game.is_board_full())

        self.game.gameState = [['X', 'X', 'O'], ['O', 'X', 'X'],
        ['O', 'O', 'X']]

        self.assertTrue(self.game.is_board_full())

        self.game.gameState = [['O', 'O', 'O'], ['O', 'O', 'O'],
        ['O', 'O', 'O']]

        self.assertTrue(self.game.is_board_full())

        self.game.gameState = [['X', 'X', 'X'], ['X', 'X', 'X'],
        ['X', 'X', 'X']]

        self.assertTrue(self.game.is_board_full())

    def test_is_vertical_win_condition(self):
        self.assertFalse(self.game.is_vertical_win_condition())

        self.game.gameState = [[' ', ' ', 'O'],
                               ['O', 'X', 'X'],
                               ['O', 'O', 'X']]

        self.assertFalse(self.game.is_vertical_win_condition())

        self.game.gameState = [[' ', 'X', 'X'],
                               ['X', 'O', 'X'],
                               ['O', 'O', 'O']]

        self.assertFalse(self.game.is_vertical_win_condition())

        self.game.gameState = [[' ', 'X', 'O'],
                               ['X', 'X', 'X'],
                               ['O', 'O', 'O']]

        self.assertFalse(self.game.is_vertical_win_condition())

        self.game.gameState = [['X', 'X', 'X'],
                               ['O', 'O', 'X'],
                               ['O', 'O', 'X']]

        self.assertTrue(self.game.is_vertical_win_condition())

        self.game.gameState = [['X', 'O', 'X'],
                               ['O', 'O', 'X'],
                               ['X', 'O', 'X']]

        self.assertTrue(self.game.is_vertical_win_condition())

        self.game.gameState = [['X', ' ', ' '],
                               ['X', 'O', ' '],
                               ['X', 'O', ' ']]

        self.assertTrue(self.game.is_vertical_win_condition())

        self.game.gameState = [[' ', 'X', 'O'],
                               ['X', 'X', 'O'],
                               ['O', 'X', 'O']]

        self.assertTrue(self.game.is_vertical_win_condition())


    def test_is_horizontal_win_condition(self):
        self.assertFalse(self.game.is_horizontal_win_condition())

        self.game.gameState = [[' ', ' ', 'O'],
                               ['O', 'X', 'X'],
                               ['O', 'O', 'X']]

        self.assertFalse(self.game.is_horizontal_win_condition())

        self.game.gameState = [[' ', 'O', 'X'],
                               ['X', 'O', 'X'],
                               ['O', 'X', 'O']]

        self.assertFalse(self.game.is_horizontal_win_condition())

        self.game.gameState = [[' ', 'X', 'O'],
                               ['X', 'X', '0'],
                               ['O', 'X', 'O']]

        self.assertFalse(self.game.is_horizontal_win_condition())

        self.game.gameState = [['X', 'X', 'X'],
                               ['O', 'O', 'X'],
                               ['O', 'O', 'X']]

        self.assertTrue(self.game.is_horizontal_win_condition())

        self.game.gameState = [['X', 'O', 'X'],
                               ['O', 'O', 'O'],
                               ['X', ' ', 'X']]
        self.game.turn = 'O'

        self.assertTrue(self.game.is_horizontal_win_condition())

        self.game.gameState = [['X', 'O', 'O'],
                               [' ', 'O', ' '],
                               ['X', 'X', 'X']]
        self.game.turn = 'X'

        self.assertTrue(self.game.is_horizontal_win_condition())

        self.game.gameState = [[' ', 'X', 'O'],
                               ['X', 'X', 'X'],
                               ['O', 'O', 'O']]

        self.assertTrue(self.game.is_horizontal_win_condition())

    def test_is_diagonal_win_condition(self):
        self.assertFalse(self.game.is_diagonal_win_condition())

        self.game.gameState = [[' ', ' ', 'O'],
                               ['O', 'X', 'X'],
                               ['O', 'O', 'X']]

        self.assertFalse(self.game.is_diagonal_win_condition())

        self.game.gameState = [[' ', 'O', 'X'],
                               ['X', 'O', 'X'],
                               ['O', 'X', 'O']]

        self.assertFalse(self.game.is_diagonal_win_condition())

        self.game.gameState = [[' ', 'X', 'O'],
                               ['X', 'X', '0'],
                               ['O', 'X', 'O']]

        self.assertFalse(self.game.is_diagonal_win_condition())

        self.game.gameState = [['X', 'X', 'X'],
                               ['O', 'X', 'O'],
                               ['O', 'O', 'X']]

        self.assertTrue(self.game.is_diagonal_win_condition())

        self.game.gameState = [['O', 'X', 'X'],
                               ['X', 'O', 'O'],
                               ['X', ' ', 'O']]
        self.game.turn = 'O'

        self.assertTrue(self.game.is_diagonal_win_condition())

        self.game.gameState = [['X', 'O', 'O'],
                               [' ', 'X', ' '],
                               ['X', 'O', 'X']]
        self.game.turn = 'X'

        self.assertTrue(self.game.is_diagonal_win_condition())

        self.game.gameState = [['O', 'X', 'O'],
                               ['X', 'O', 'X'],
                               ['O', 'X', 'O']]
        self.game.turn = 'O'

        self.assertTrue(self.game.is_diagonal_win_condition())



if __name__ == "__main__":
    unittest.main()
