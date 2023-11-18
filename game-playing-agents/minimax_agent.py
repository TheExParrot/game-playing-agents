from state import GameState
from game_agent import GameAgent


class MiniMaxAgent(GameAgent):

    def __init__(self, init_state: GameState, depth: int, player: str = None):
        if player is not None:
            super().__init__(init_state, player)
        else:
            super().__init__(init_state, init_state.active_player)
        self.depth = depth

    def get_next_action(self):
        # TO DO
        return
