from abc import ABC, abstractmethod


class GameState(ABC):

    @property
    def state(self) -> any:
        """
        :return: the current game state
        """
        return

    @property
    def active_player(self) -> str:
        """
        :return: the active player
        """
        return ""

    @property
    def legal_actions(self) -> list:
        """
        :return: a list of legal actions from the current game state based on the active player
        """
        return []

    @property
    def utility(self) -> dict[str, float]:
        """
        :return: a dictionary of utility values for each player
        """
        return dict()

    @property
    def is_terminal(self) -> bool:
        """
        :return: True if the game is over, False otherwise
        """
        return False

    @abstractmethod
    def get_winner(self) -> str:
        """
        :return: the winner of the game if the game is over, or None if the game is not terminal
        """
        return ""

    @abstractmethod
    def get_next_state(self, action) -> 'GameState':
        """
        param action: the action to take
        :return: the next game state after the action is taken
        """
        pass
