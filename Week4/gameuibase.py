import abc


class GameUIBase(abc.ABC):

    @abc.abstractmethod
    def state_of_the_game(self):
        return ""

    @abc.abstractmethod
    def get_input_values(self, input_values):
        pass

    @abc.abstractmethod
    def validate_input_values(self, input_values):
        pass

    @abc.abstractmethod
    def insert_values(self):
        pass

    @abc.abstractmethod
    def next_turn(self):
        pass

    @abc.abstractmethod
    def check_win_condition(self):
        pass
