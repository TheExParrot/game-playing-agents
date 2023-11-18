from abc import ABC, abstractmethod


class AbstractAgent(ABC):

    @abstractmethod
    def get_next_action(self):
        """
        :param state: the current state of the game
        :return: the action to take
        """
        pass

