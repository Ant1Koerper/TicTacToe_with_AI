class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.current_player = self.determine_current_player()

    def determine_current_player(self):
        count_x = sum(sublist.count('X') for sublist in self.board)
        count_o = sum(sublist.count('O') for sublist in self.board)

        if count_x <= count_o:
            return 'X'
        else:
            return 'O'

    # add
    def add_move(self, x, y):
        # check if move is valid
        if x not in range(3) or y not in range(3):
            return False

        self.board[x][y] = self.current_player
        return True

    def next_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_win(self):
        possible_winning_pos = list()
        # check rows
        possible_winning_pos.extend(
            [self.board[i] for i in range(3)]
        )
        # check columns
        possible_winning_pos.extend(
            [[row[i] for row in self.board] for i in range(3)]
        )
        # check diagonals
        possible_winning_pos.append(
            [self.board[i][i] for i in range(3)]
        )
        possible_winning_pos.append(
            [self.board[i][2 - i] for i in range(3)]
        )

        check = any(
            all(pos == 'X' for pos in position) or
            all(pos == 'O' for pos in position) for position in possible_winning_pos
        )
        return check

    def check_end(self):
        board_is_full = all([entry in ['X', 'O'] for row in self.board for entry in row])
        return board_is_full or self.check_win()
