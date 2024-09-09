import copy

from tictactoe_class import TicTacToe
from random import choice


class TicTacToeBot:
    def __init__(self, difficulty, player):
        self.difficulty = difficulty
        self.player = player
        self.opponent = "X" if player == "O" else "O"

    def next_move(self, tictactoe: TicTacToe):
        print(f"Making move level \"{self.difficulty}\"")
        if self.difficulty == "easy":
            return self.random_move(tictactoe)
        elif self.difficulty == "medium":
            winning_moves = self.determine_winning_moves(tictactoe)

            if len(winning_moves[self.player]) > 0:
                return winning_moves[self.player][0]
            elif len(winning_moves[self.opponent]) > 0:
                return winning_moves[self.opponent][0]
            else:
                return self.random_move(tictactoe)
        elif self.difficulty == "hard":
            return self.best_move(tictactoe)
        else:
            print("Difficulty unknown.")

    def free_positions(self, board):
        free_positions = [
            (i, j) for i in range(3) for j in range(3)
            if board[i][j] not in ["X", "O"]
        ]
        return free_positions

    # make a random move
    def random_move(self, tictactoe: TicTacToe):
        return choice(self.free_positions(tictactoe.board))

    # checks if for any player a "winning" move is present,
    # i.e. a move which wins the game next turn
    def determine_winning_moves(self, tictactoe: TicTacToe):
        free_positions = self.free_positions(tictactoe.board)
        winning_moves = {"X": [], "O": []}
        # try each position. if it is a winning position, add it
        for x, y in free_positions:
            for player in ["X", "O"]:
                board = copy.deepcopy(tictactoe.board)
                board[x][y] = player
                tictactoe_test = TicTacToe(board)
                if tictactoe_test.check_win():
                    winning_moves[player].append((x, y))

        return winning_moves

    def best_move(self, tictactoe: TicTacToe):

        return self.min_max_recursion(copy.deepcopy(tictactoe.board), self.player, return_type="move")

    def min_max_recursion(self, board, player, return_type="value"):
        tictactoe = TicTacToe(board)
        # if the game is in a final state return evaluation
        if tictactoe.check_win():
            if self.player != player:
                return 10
            else:
                return -10
        elif tictactoe.check_end():
            return 0

        # if no final state was reached, try each position:
        results = dict()
        next_player = "X" if player == "O" else "O"
        for x, y in self.free_positions(board):
            new_board = copy.deepcopy(board)
            new_board[x][y] = player
            results[(x, y)] = self.min_max_recursion(new_board, next_player, return_type="value")

        # if the return type is value, we want to calculate the value of each move
        # else, we want to return one move having the highest value
        if return_type == "value":
            if player == self.player:
                return max(results.values())
            else:
                return min(results.values())
        else:
            print(results)
            return max(results, key=results.get)


