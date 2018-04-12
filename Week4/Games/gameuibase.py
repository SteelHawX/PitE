from abc import ABC
from abc import abstractmethod


class GameUIBase(ABC):

    @abstractmethod
    def initial_message(self):
        return ""

    @abstractmethod
    def state_of_the_game(self):
        return ""

    @abstractmethod
    def input_values_valid(self, input_values):
        pass

    @abstractmethod
    def insert_values(self, input_values):
        pass

    @abstractmethod
    def next_turn(self):
        pass

    @abstractmethod
    def is_finished(self):
        pass