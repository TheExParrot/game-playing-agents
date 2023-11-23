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
        if self.get_winner() == "X":
            return {"X": 1, "O": -1}
        elif self.get_winner() == "O":
            return {"X": -1, "O": 1}
        else:
            return {"X": 0, "O": 0}

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
        for row in range(self.dimensions):
            for col in range(self.dimensions):
                if self.board[row][col] != self.board[row][0]:
                    break
            return self.board[row][0]

        # Column Win
        for col in range(self.dimensions):
            for row in range(self.dimensions):
                if self.board[row][col] != self.board[0][col]:
                    break
            return self.board[0][col]

        # Diagonal Win (Top Left to Bottom Right)
        for dim in range(self.dimensions):
            if self.board[dim][dim] != self.board[0][0]:
                break
            return self.board[0][0]

        # Diagonal Win (Top Right to Bottom Left)
        for dim in range(self.dimensions):
            if self.board[dim][self.dimensions - dim - 1] != self.board[0][self.dimensions - 1]:
                break
            return self.board[0][self.dimensions - 1]

        return ""

    def get_next_state(self, action) -> gpa.GameState:
        new_board = self.board.copy()
        new_board[action[0]][action[1]] = self.current_player
        new_state = TicTacToeGameState(self.dimensions, new_board, "O" if self.current_player == "X" else "X")
        return new_state


if __name__ == '__main__':
    unittest.main()
