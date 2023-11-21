from .state import GameState
from .game_agent import GameAgent

import math
import random


class MonteCarloAgent(GameAgent):

    def __init__(self, init_state: GameState, rollouts: int, player: str = None):
        if player is not None:
            super().__init__(init_state, player)
        else:
            super().__init__(init_state, init_state.active_player)
        self.rollouts = rollouts

    def get_next_action(self):
        root = MonteCarloNode(self.current_state, self.player)

        while True:
            # Selection
            selected_node = root.selection()
            # Expansion
            expanded_node = selected_node.expansion(selected_node)
            # Simulation
            simulation_result = expanded_node.simulation(expanded_node)
            # Backpropagation
            expanded_node.backpropagation(simulation_result)


class MonteCarloNode:

    def __init__(self, init_state: GameState, player: str, parent: 'MonteCarloNode' = None):
        self.state = init_state
        self.children = set()  # type: set[MonteCarloNode]
        self.player = player
        self.parent = parent
        self.N = 0
        self.n = 0
        self.v = 0

    def ucb(self):
        return self.v / self.n + 2 * math.sqrt(math.log(self.N) / self.n)

    def selection(self):
        """Select highest UCB until leaf node is reached"""
        current_node = self
        while len(current_node.children) > 0:
            max_ucb = float('-inf')
            max_ucb_node = None
            for child in current_node.children:
                child_ucb = child.ucb()
                if child_ucb > max_ucb:
                    max_ucb = child_ucb
                    max_ucb_node = child
            current_node = max_ucb_node
        return current_node

    def expansion(self, selected_node: 'MonteCarloNode'):
        """Expand Leaf Node with a new child"""
        random_action = random.choice(self.state.legal_actions)
        next_state = self.state.get_next_state(random_action)
        new_node = MonteCarloNode(next_state, self.player, selected_node)
        selected_node.children.add(new_node)
        return new_node

    def simulation(self, child_node: 'MonteCarloNode'):
        """Simulate from new child"""
        simulation_state = child_node.state
        while not simulation_state.is_terminal:
            random_action = random.choice(simulation_state.legal_actions)
            simulation_state = simulation_state.get_next_state(random_action)
        return simulation_state.utility[self.player]

    def backpropagation(self, simulation_result: float):
        """Update all nodes from leaf to root"""
        current_node = self
        while current_node is not None:
            current_node.N += 1
            current_node.n += 1
            current_node.v += simulation_result
            current_node = current_node.parent
