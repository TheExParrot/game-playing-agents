import unittest

import game_playing_agents as gpa


class TicTacToeGameState(gpa.GameState):

    def __init__(self, dimensions: int = 3, board: list = None, current_player: str = "X"):
        if board is None:
            self.board = [['' for _ in range(dimensions)] for _ in range(dimensions)]
            self.dimensions = dimensions
        else:
            self.board = board
            self.dimensions = len(board)
        self.current_player = current_player

    @property
    def state(self) -> any:
        return self.board

    @property
    def active_player(self) -> str:
        return self.current_player

    @property
    def legal_actions(self) -> list:
        actions = []
        for row in range(self.dimensions):
            for col in range(self.dimensions):
                if self.board[row][col] == '':
                    actions.append((row, col))
        return actions

    @property
    def utility(self) -> dict[str, float]:
        winner = self.get_winner()
        if winner == "X":
            return {"X": 1, "O": -1}
        elif winner == "O":
            return {"X": -1, "O": 1}
        else:
            return {"X": 0.5, "O": 0.5}

    @property
    def is_terminal(self) -> bool:
        return self.get_winner() != "" or self.is_board_full()

    def is_board_full(self) -> bool:
        for row in range(self.dimensions):
            for col in range(self.dimensions):
                if self.board[row][col] == '':
                    return False
        return True

    def get_winner(self) -> str:
        # Row Win
        for row in self.board:
            if row[0] != '' and all(x == row[0] for x in row):
                return row[0]

        # Column Win
        for col in range(self.dimensions):
            # Get Player of Column
            player = self.board[0][col]
            if player == '':
                break
            # Check if every row in column is the same
            for row in range(self.dimensions):
                if self.board[row][col] != player:
                    break
                elif row == self.dimensions - 1:
                    return player

        # Diagonal Win (top left -> bottom right)
        player = self.board[0][0]
        if player != '':
            for i in range(self.dimensions):
                if self.board[i][i] != player:
                    break
                if i == self.dimensions - 1:
                    return player

        # Diagonal Win (top right -> bottom left)
        player = self.board[0][self.dimensions - 1]
        if player != '':
            for i in range(self.dimensions):
                if self.board[i][self.dimensions - 1 - i] != player:
                    break
                if i == self.dimensions - 1:
                    return player

        return ""

    def get_next_state(self, action) -> gpa.GameState:
        new_board = self.board.copy()
        new_board[action[0]][action[1]] = self.current_player
        new_state = TicTacToeGameState(self.dimensions, new_board, "O" if self.current_player == "X" else "X")
        return new_state

    def __str__(self):
        string = ""
        for row in range(self.dimensions):
            for col in range(self.dimensions):
                symbol = self.board[row][col]
                if symbol == '':
                    symbol = "_"
                string += symbol + " "
            string += "\n"
        return string

    def __copy__(self):
        return TicTacToeGameState(self.dimensions, self.board.copy(), self.current_player)


if __name__ == '__main__':
    unittest.main()


class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToeGameState()

    def play_game(self, x_agent: gpa.GameAgent, o_agent: gpa.GameAgent, debug: bool = False):
        while not self.game.is_terminal:
            if debug:
                print(self.game)
                print("-------------")
            if self.game.active_player == "X":
                action = x_agent.get_next_action()
                self.game = self.game.get_next_state(action)
                o_agent.update_state(self.game)
            else:
                action = o_agent.get_next_action()
                self.game = self.game.get_next_state(action)
                x_agent.update_state(self.game)
        return self.game.get_winner()

    def test_random_vs_random(self):
        x_agent = gpa.RandomAgent(self.game, "X")
        o_agent = gpa.RandomAgent(self.game, "O")
        winner = self.play_game(x_agent, o_agent)
        self.assertIn(winner, ["X", "O", ""])

    def test_minimax_vs_random(self):
        x_agent = gpa.MiniMaxAgent(self.game, 10, "X")
        o_agent = gpa.RandomAgent(self.game, "0")
        winner = self.play_game(x_agent, o_agent)
        self.assertIn(winner, ["X", "O", ""])

    def test_minimax_vs_minimax(self):
        x_agent = gpa.MiniMaxAgent(self.game, 10, "X")
        o_agent = gpa.MiniMaxAgent(self.game, 10, "O")
        winner = self.play_game(x_agent, o_agent)
        self.assertIn(winner, ["X", "O", ""])
