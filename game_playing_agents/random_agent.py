from .state import GameState
from .game_agent import GameAgent
import random


class RandomAgent(GameAgent):

    def __init__(self, init_state: GameState, player: str = None):
        if player is not None:
            super().__init__(init_state, player)
        else:
            super().__init__(init_state, init_state.active_player)

    def get_next_action(self):
        return random.choice(self.current_state.legal_actions)
