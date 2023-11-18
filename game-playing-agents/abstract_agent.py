from abc import ABC, abstractmethod


class AbstractAgent(ABC):

    @abstractmethod
    def get_next_action(self):
        """
        :return: the action to take
        """
        pass
