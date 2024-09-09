from tictactoe_class import TicTacToe


class TicTacToeViewer:
    def __init__(self):
        self.tictactoe = None

    def get_initial_board(self):
        initial_board = input("Enter the cells:")
        while len(initial_board) != 9:
            initial_board = input("Length of initial board must be 9. Enter the cells:")
        initial_board = [list(initial_board[3 * i:3 * i + 3]) for i in range(3)]
        return initial_board

    def print_board(self):
        board = self.tictactoe.board
        # prepare board for printing
        board = ["| " + " ".join(row).replace("_", " ") + " |" for row in board]

        print("---------")
        print(*board, sep="\n")
        print("---------")

    def get_next_move(self):
        next_move = input("Enter the coordinates:")
        if self.next_move_valid(next_move):
            return next_move
        else:
            return self.get_next_move()

    def next_move_valid(self, next_move):
        if all([not x.isdigit() for x in next_move.split()]):
            print("You should enter numbers!")
            return False
        # from here on, we know that x and y are integers
        x, y = next_move.split()
        x = int(x)
        y = int(y)
        if x not in range(1, 4) or y not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            return False
        if self.tictactoe.board[x - 1][y - 1] != "_":
            print("This cell is occupied! Choose another one!")
            return False

        return True
