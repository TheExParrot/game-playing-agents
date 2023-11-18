from state import GameState
from abstract_agent import AbstractAgent


class MiniMaxAgent(AbstractAgent):

    def __init__(self, init_state: GameState, depth: int):
        self.current_state = init_state
        self.depth = depth

    def get_next_action(self):
        # TO DO
        return
