from tictactoe_class import TicTacToe
from tictactoeviewer import TicTacToeViewer
from tictactoebot import TicTacToeBot


def play_game(player1, player2):
    # initialize game and set up model and view
    tictactoe_viewer = TicTacToeViewer()
    tictactoe = TicTacToe([["_"] * 3 for _ in range(3)])
    tictactoe_viewer.tictactoe = tictactoe
    # use dictionary to determine if player is a bot or a user
    # and also append the bot for easier user later.
    settings = {
        "X": {"type": player1},
        "O": {"type": player2}
    }
    if player1 != "user":
        settings["X"]["bot"] = TicTacToeBot(player1, "X")
    if player2 != "user":
        settings["O"]["bot"] = TicTacToeBot(player2, "O")
    # print initial board
    tictactoe_viewer.print_board()

    # play board until end is reached
    finished = False
    while not finished:
        # do next move
        next_move(tictactoe, tictactoe_viewer, settings)
        # print updated board
        tictactoe_viewer.print_board()
        # check if game has reached a final state
        finished = tictactoe.check_end()
        if not finished:
            tictactoe.next_player()

    if tictactoe.check_win():
        print(f"{tictactoe.current_player} wins")
    else:
        print("Draw")


def next_move(tictactoe, tictactoe_viewer, settings):
    if settings[tictactoe.current_player]["type"] == "user":
        x, y = tictactoe_viewer.get_next_move().split()
        x = int(x) - 1
        y = int(y) - 1
    else:
        x, y = settings[tictactoe.current_player]["bot"].next_move(tictactoe)
    tictactoe.add_move(x, y)


def game_menu():
    finished = False
    while not finished:
        command = input("Input command:")
        if "exit" in command:
            finished = True
            break
        else:
            try:
                start, player1, player2 = command.split()
                play_game(player1, player2)
            except:
                print("Bad parameters!")


game_menu()
