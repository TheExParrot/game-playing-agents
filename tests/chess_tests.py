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
        if self.board.is_checkmate():
            if self.board.turn:
                return {'white': -1, 'black': 1}
            else:
                return {'white': 1, 'black': -1}

        if self.board.is_stalemate():
            return {'white': 0, 'black': 0}

        white_material_count = self.get_material_count(chess.WHITE)
        black_material_count = self.get_material_count(chess.BLACK)
        return {'white': white_material_count, 'black': black_material_count}

    def get_material_count(self, color: chess.Color) -> int:
        return len(self.board.pieces(chess.PAWN, color)) \
               + len(self.board.pieces(chess.KNIGHT, color)) * 3 \
               + len(self.board.pieces(chess.BISHOP, color)) * 3 \
               + len(self.board.pieces(chess.ROOK, color)) * 5 \
               + len(self.board.pieces(chess.QUEEN, color)) * 9

    @property
    def is_terminal(self) -> bool:
        return self.board.is_game_over()

    def get_winner(self) -> str:
        if self.board.is_checkmate():
            return "black" if self.board.turn else "white"
        else:
            return ""

    def get_next_state(self, action) -> gpa.GameState:
        new_board = self.board.copy()
        new_board.push(action)
        return ChessGameState(new_board)

    def __str__(self):
        return str(self.board)

    def __hash__(self):
        return hash(str(self.board))


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

    def test_simple_max_vs_random(self):
        white_agent = gpa.SimpleMaxAgent(self.game_state, "white")
        black_agent = gpa.RandomAgent(self.game_state, "black")

        # Play until game is over
        while not self.game_state.is_terminal:

            # White Turn
            if self.game_state.board.turn:
                # Determine White Action
                white_action = white_agent.get_next_action()
                self.assertTrue(white_action in self.game_state.legal_actions)

                # Update Game State with White Move
                self.game_state = self.game_state.get_next_state(white_action)
                self.assertTrue(self.game_state.board.is_valid())

                # Update Black Agent with new Game State
                black_agent.current_state = self.game_state

            # Black Turn
            else:
                # Determine Black Action
                black_action = black_agent.get_next_action()
                self.assertTrue(black_action in self.game_state.legal_actions)

                # Update Game State with Black Move
                self.game_state = self.game_state.get_next_state(black_action)
                self.assertTrue(self.game_state.board.is_valid())

                # Update White Agent with new Game State
                white_agent.current_state = self.game_state

    def test_minimax_vs_random(self):
        white_agent = gpa.MiniMaxAgent(self.game_state, 1, "white")
        black_agent = gpa.RandomAgent(self.game_state, "black")

        # Play until game is over
        while not self.game_state.is_terminal:

            # White Turn
            if self.game_state.board.turn:
                # Determine White Action
                white_action = white_agent.get_next_action()
                self.assertTrue(white_action in self.game_state.legal_actions)

                # Update Game State with White Move
                self.game_state = self.game_state.get_next_state(white_action)
                self.assertTrue(self.game_state.board.is_valid())

                # Update Black Agent with new Game State
                black_agent.current_state = self.game_state

            # Black Turn
            else:
                # Determine Black Action
                black_action = black_agent.get_next_action()
                self.assertTrue(black_action in self.game_state.legal_actions)

                # Update Game State with Black Move
                self.game_state = self.game_state.get_next_state(black_action)
                self.assertTrue(self.game_state.board.is_valid())

                # Update White Agent with new Game State
                white_agent.current_state = self.game_state

    def test_monte_carlo_vs_random(self):
        white_agent = gpa.MonteCarloAgent(self.game_state, 10, "white")
        black_agent = gpa.RandomAgent(self.game_state, "black")

        # Play until game is over
        while not self.game_state.is_terminal:
            print("------")
            print(self.game_state.board)


            # White Turn
            if self.game_state.board.turn:
                print("White Turn")
                # Determine White Action
                white_action = white_agent.get_next_action()
                self.assertTrue(white_action in self.game_state.legal_actions)

                # Update Game State with White Move
                self.game_state = self.game_state.get_next_state(white_action)
                self.assertTrue(self.game_state.board.is_valid())

                # Update Black Agent with new Game State
                black_agent.current_state = self.game_state

            # Black Turn
            else:
                print("Black Turn")
                # Determine Black Action
                black_action = black_agent.get_next_action()
                self.assertTrue(black_action in self.game_state.legal_actions)

                # Update Game State with Black Move
                self.game_state = self.game_state.get_next_state(black_action)
                self.assertTrue(self.game_state.board.is_valid())

                # Update White Agent with new Game State
                white_agent.current_state = self.game_state


if __name__ == '__main__':
    unittest.main()
