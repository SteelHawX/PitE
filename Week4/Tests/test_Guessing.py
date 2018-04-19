import unittest
import sys
sys.path.append("../Games")
from unittest.mock import MagicMock
from Guessing import GuessingGame
from Guessing import GuessingGameUI

class TestGuessingGame(unittest.TestCase):
    def setUp(self):
        self.game = GuessingGame()

    def test_init(self):
        self.assertIn(self.game.number, range(1, 101), "Number drew by computer is not in range")
        self.assertEqual(self.game.guess, 0)
        self.assertEqual(self.game.number_of_guesses, 0)

        pass

    def test_insert_value(self):
        self.game.insert_value(10)
        self.assertEqual(self.game.guess, 10)
        self.game.insert_value(47)
        self.assertEqual(self.game.guess, 47)
        self.game.insert_value(1)
        self.assertEqual(self.game.guess, 1)
        self.game.insert_value(100)
        self.assertEqual(self.game.guess, 100)

        pass

    def test_increase_number_of_guesses(self):
        self.game.increase_number_of_guesses()
        self.assertEqual(self.game.number_of_guesses, 1)
        self.game.increase_number_of_guesses()
        self.game.increase_number_of_guesses()
        self.assertEqual(self.game.number_of_guesses, 3)

        for i  in range(11):
            self.game.increase_number_of_guesses()

        self.assertEqual(self.game.number_of_guesses, 14)
        self.game.increase_number_of_guesses()
        self.assertEqual(self.game.number_of_guesses, 15)

        pass


    def test_has_player_won(self):
        self.game.number = 1
        self.game.guess = 2
        self.assertFalse(self.game.has_player_won())
        self.game.guess = 100
        self.assertFalse(self.game.has_player_won())
        self.game.guess = 35
        self.assertFalse(self.game.has_player_won())
        self.game.guess = 1
        self.assertTrue(self.game.has_player_won())

        self.game.number = 100
        self.game.guess = 99
        self.assertFalse(self.game.has_player_won())
        self.game.guess = 1
        self.assertFalse(self.game.has_player_won())
        self.game.guess = 78
        self.assertFalse(self.game.has_player_won())
        self.game.guess = 100
        self.assertTrue(self.game.has_player_won())

        self.game.number = 57
        self.game.guess = 56
        self.assertFalse(self.game.has_player_won())
        self.game.guess = 89
        self.assertFalse(self.game.has_player_won())
        self.game.guess = 24
        self.assertFalse(self.game.has_player_won())
        self.game.guess = 57
        self.assertTrue(self.game.has_player_won())

        pass

    def test_can_player_guess_again(self):
        self.assertTrue(self.game.can_player_guess_again())

        self.game.number_of_guesses = GuessingGame.maximum_number_of_guesses - 11
        self.assertTrue(self.game.can_player_guess_again())

        self.game.number_of_guesses = GuessingGame.maximum_number_of_guesses - 4
        self.assertTrue(self.game.can_player_guess_again())

        self.game.number_of_guesses = GuessingGame.maximum_number_of_guesses - 1
        self.assertTrue(self.game.can_player_guess_again())

        self.game.number_of_guesses = GuessingGame.maximum_number_of_guesses
        self.assertFalse(self.game.can_player_guess_again())



if __name__ == "__main__":
    unittest.main()