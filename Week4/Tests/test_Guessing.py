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


    def test_is_guess_smaller(self):
        self.assertTrue(self.game.is_guess_smaller())
        
        self.game.number = 1
        self.game.guess = 50
        self.assertFalse(self.game.is_guess_smaller())
        self.game.number = 1
        self.game.guess = 20
        self.assertFalse(self.game.is_guess_smaller())
        self.game.number = 75
        self.game.guess = 75
        self.assertFalse(self.game.is_guess_smaller())
        self.game.number = 75
        self.game.guess = 100
        self.assertFalse(self.game.is_guess_smaller())
        self.game.number = 100
        self.game.guess = 100
        self.assertFalse(self.game.is_guess_smaller())

        self.game.number = 100
        self.game.guess = 20
        self.assertTrue(self.game.is_guess_smaller())
        self.game.number = 100
        self.game.guess = 90
        self.assertTrue(self.game.is_guess_smaller())
        self.game.number = 100
        self.game.guess = 47
        self.assertTrue(self.game.is_guess_smaller())
        self.game.number = 30
        self.game.guess = 13
        self.assertTrue(self.game.is_guess_smaller())
        self.game.number = 30
        self.game.guess = 29
        self.assertTrue(self.game.is_guess_smaller())


    def test_is_guess_bigger(self):
        self.assertFalse(self.game.is_guess_bigger())

        self.game.guess = 1
        self.game.number = 1
        self.assertFalse(self.game.is_guess_bigger())
        self.game.guess = 53
        self.game.number = 54
        self.assertFalse(self.game.is_guess_bigger())
        self.game.guess = 53
        self.game.number = 84
        self.assertFalse(self.game.is_guess_bigger())
        self.game.guess = 100
        self.game.number = 100
        self.assertFalse(self.game.is_guess_bigger())
        self.game.guess = 97
        self.game.number = 100
        self.assertFalse(self.game.is_guess_bigger())

        self.game.guess = 100
        self.game.number = 99
        self.assertTrue(self.game.is_guess_bigger())
        self.game.guess = 100
        self.game.number = 74
        self.assertTrue(self.game.is_guess_bigger())
        self.game.guess = 2
        self.game.number = 1
        self.assertTrue(self.game.is_guess_bigger())
        self.game.guess = 35
        self.game.number = 31
        self.assertTrue(self.game.is_guess_bigger())
        self.game.guess = 87
        self.game.number = 86
        self.assertTrue(self.game.is_guess_bigger())

        pass

class TestGuessingGameUI(unittest.TestCase):
    def setUp(self):
        self.UI = GuessingGameUI()

    def test_init(self):
        self.assertEqual(self.UI._game_state, 0)

        pass

    def test_players(self):
        self.assertEqual(GuessingGameUI.players(), 1)

        pass

    def test_string_to_input(self):
        self.assertEqual(GuessingGameUI.string_to_input("-15"), -15)
        self.assertEqual(GuessingGameUI.string_to_input("97"), 97)
        self.assertEqual(GuessingGameUI.string_to_input("123131413343424"), 123131413343424)


        pass

    def test_string_is_valid(self):
        self.assertTrue(self.UI.string_is_valid("57"))
        self.assertTrue(self.UI.string_is_valid("0"))
        self.assertTrue(self.UI.string_is_valid("9482423829"))


        self.assertFalse(self.UI.string_is_valid("-1"))
        self.assertFalse(self.UI.string_is_valid("-12&"))
        self.assertFalse(self.UI.string_is_valid("2%54"))
        self.assertFalse(self.UI.string_is_valid(""))
        self.assertFalse(self.UI.string_is_valid("s4a"))
        self.assertFalse(self.UI.string_is_valid("sad"))
        self.assertFalse(self.UI.string_is_valid("\u00B2"))

        pass

    def test_input_values_valid(self):
        self.assertTrue(self.UI.input_values_valid(1))
        self.assertTrue(self.UI.input_values_valid(100))
        self.assertTrue(self.UI.input_values_valid(84))
        self.assertTrue(self.UI.input_values_valid(23))


        self.assertFalse(self.UI.input_values_valid(101))
        self.assertFalse(self.UI.input_values_valid(0))
        self.assertFalse(self.UI.input_values_valid(500231))

        pass

    def test_is_finished(self):
        self.UI._game.has_player_won = MagicMock(return_value=True)
        self.UI._game.can_player_guess_again = MagicMock(return_value=True)

        self.assertTrue(self.UI.is_finished())

        self.UI._game.can_player_guess_again = MagicMock(return_value=False)

        self.assertTrue(self.UI.is_finished())

        self.UI._game.has_player_won = MagicMock(return_value=False)

        self.assertTrue(self.UI.is_finished())

        self.UI._game.can_player_guess_again = MagicMock(return_value=True)

        self.assertFalse(self.UI.is_finished())

        pass





if __name__ == "__main__":
    unittest.main()
