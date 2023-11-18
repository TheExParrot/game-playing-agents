from abc import ABC, abstractmethod
from state import GameState


class GameAgent(ABC):

    def __init__(self, init_state: GameState, player: str):
        self.current_state = init_state
        self.player = player

    @abstractmethod
    def get_next_action(self):
        """
        :return: the action to take
        """
        ...
