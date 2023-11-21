from .state import GameState
from .game_agent import GameAgent


class MiniMaxAgent(GameAgent):

    def __init__(self, init_state: GameState, depth: int, player: str = None):
        if player is not None:
            super().__init__(init_state, player)
        else:
            super().__init__(init_state, init_state.active_player)
        self.max_depth = depth

    def get_next_action(self):
        root = MiniMaxNode(self.current_state, self.max_depth, self.player)
        max_action = root.minimax_search()
        return max_action


class MiniMaxNode:

    def __init__(self, state: GameState, max_depth: int, max_player: str,
                 node_depth: int = 0, parent: 'MiniMaxNode' = None):
        self.state = state
        self.max_depth = max_depth
        self.node_depth = node_depth
        self.max_player = max_player
        self.parent = parent
        self.alpha = float('-inf')
        self.beta = float('inf')

    def minimax_search(self):
        # Base Case: If at depth or terminal state, return utility
        if self.node_depth == self.max_depth or self.state.is_terminal:
            return self.state.utility[self.max_player]

        # Recursive Maximise Case:
        if self.state.active_player == self.max_player:
            max_value = float('-inf')
            for action in self.state.legal_actions:
                next_state = self.state.get_next_state(action)
                next_node = MiniMaxNode(next_state, self.max_depth, self.max_player, self.node_depth + 1, self)
                max_value = max(max_value, next_node.minimax_search())
                self.alpha = max(self.alpha, max_value)
                if self.alpha >= self.beta:
                    break
            return max_value

        # Recursive Minimise Case:
        else:
            min_value = float('inf')
            for action in self.state.legal_actions:
                next_state = self.state.get_next_state(action)
                next_node = MiniMaxNode(next_state, self.max_depth, self.max_player, self.node_depth + 1, self)
                min_value = min(min_value, next_node.minimax_search())
                self.beta = min(self.beta, min_value)
                if self.alpha >= self.beta:
                    break
            return min_value


        
