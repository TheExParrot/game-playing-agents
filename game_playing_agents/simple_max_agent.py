from .state import GameState
from .game_agent import GameAgent


class SimpleMaxAgent(GameAgent):

    def __init__(self, init_state: GameState, player: str = None):
        if player is not None:
            super().__init__(init_state, player)
        else:
            super().__init__(init_state, init_state.active_player)

    def get_next_action(self):
        actions = self.current_state.legal_actions
        # get the max action based on the utility of the state after taking the action
        max_action = max(actions, key=lambda action: self.current_state.get_next_state(action).utility[self.player])
        return max_action
