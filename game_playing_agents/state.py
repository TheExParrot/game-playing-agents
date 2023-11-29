from abc import ABC, abstractmethod


class GameState(ABC):

    @property
    @abstractmethod
    def state(self) -> any:
        """
        :return: the current game state
        """
        ...

    @property
    @abstractmethod
    def active_player(self) -> str:
        """
        :return: the active player
        """
        ...

    @property
    @abstractmethod
    def legal_actions(self) -> list:
        """
        :return: a list of legal actions from the current game state based on the active player
        """
        ...

    @property
    @abstractmethod
    def utility(self) -> dict[str, float]:
        """
        :return: a dictionary of utility values for each player (positive values are good for the player)
        """
        ...

    @property
    @abstractmethod
    def is_terminal(self) -> bool:
        """
        :return: True if the game is over, False otherwise
        """
        ...

    @abstractmethod
    def get_winner(self) -> str:
        """
        :return: the winner of the game if the game is over, or None if the game is not terminal
        """
        ...

    @abstractmethod
    def get_next_state(self, action) -> 'GameState':
        """
        param action: the action to take
        :return: the next game state after the action is taken
        """
        ...

    @abstractmethod
    def __str__(self) -> str:
        """
        :return: a string representation of the game state
        """
        ...

    @abstractmethod
    def __copy__(self):
        """
        :return: a copy of the game state
        """
        ...
