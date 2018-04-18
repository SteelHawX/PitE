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

if __name__ == "__main__":
    unittest.main()