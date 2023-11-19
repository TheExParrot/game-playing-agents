import unittest
import chess

import game_playing_agents as gpa


class ChessGameState(gpa.GameState):

    def __init__(self, board: chess.Board):
        self.board = board

    @property
    def state(self) -> any:
        return self.board

    @property
    def active_player(self) -> str:
        return "white" if self.board.turn else "black"

    @property
    def legal_actions(self) -> list:
        return list(self.board.legal_moves)

    @property
    def utility(self) -> dict[str, float]:
        # TO DO - IMPLEMENT UTILITY FUNCTION
        return {'white': 0, 'black': 0}

    @property
    def is_terminal(self) -> bool:
        return self.board.is_game_over()

    def get_winner(self) -> str:
        if self.board.is_checkmate():
            return "white" if self.board.turn else "black"
        else:
            return ""

    def get_next_state(self, action) -> gpa.GameState:
        new_board = self.board.copy()
        new_board.push(action)
        return ChessGameState(new_board)


class TestChess(unittest.TestCase):

    def setUp(self):
        self.board = chess.Board()
        self.game_state = ChessGameState(self.board)

    def test_ten_random_moves(self):
        self.white_agent = gpa.RandomAgent(self.game_state, "white")
        self.black_agent = gpa.RandomAgent(self.game_state, "black")

        # Loop through 10 moves
        for i in range(10):
            # Determine White Move
            white_action = self.white_agent.get_next_action()
            self.assertTrue(white_action in self.game_state.legal_actions)

            # Update Game State with White Move
            self.game_state = self.game_state.get_next_state(white_action)
            self.assertTrue(self.game_state.board.is_valid())

            # Update Black Agent with new Game State
            self.black_agent.current_state = self.game_state

            # Determine Black Move
            black_action = self.black_agent.get_next_action()
            self.assertTrue(black_action in self.game_state.legal_actions)

            # Update Game State with Black Move
            self.game_state = self.game_state.get_next_state(black_action)
            self.assertTrue(self.game_state.board.is_valid())

            # Update White Agent with new Game State
            self.white_agent.current_state = self.game_state


if __name__ == '__main__':
    unittest.main()
