import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1

    def print_board(self):
        symbols = {0: ' ', 1: 'X', -1: 'O'}
        for row in self.board:
            print("|".join(symbols[val] for val in row))
            print("-----")

    def check_winner(self):

        for i in range(3):
            if sum(self.board[i, :]) == 3 or sum(self.board[:, i]) == 3:
                return 1
            elif sum(self.board[i, :]) == -3 or sum(self.board[:, i]) == -3:
                return -1
        if sum(self.board.diagonal()) == 3 or sum(np.fliplr(self.board).diagonal()) == 3:
            return 1
        elif sum(self.board.diagonal()) == -3 or sum(np.fliplr(self.board).diagonal()) == -3:
            return -1
        # Check for a draw
        if not np.any(self.board == 0):
            return 0
        # Game is not over yet
        return None

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def make_move(self, move):
        self.board[move] = self.player
        self.player *= -1

    def undo_move(self, move):
        self.board[move] = 0
        self.player *= -1

    def minimax(self, depth, alpha, beta, maximizing_player):
        winner = self.check_winner()
        if winner is not None:
            return winner * 10 / depth

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_available_moves():
                self.make_move(move)
                eval = self.minimax(depth + 1, alpha, beta, False)
                self.undo_move(move)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_available_moves():
                self.make_move(move)
                eval = self.minimax(depth + 1, alpha, beta, True)
                self.undo_move(move)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self):
        best_move = None
        best_eval = float('-inf')
        for move in self.get_available_moves():
            self.make_move(move)
            eval = self.minimax(0, float('-inf'), float('inf'), False)
            self.undo_move(move)
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move

def play_tic_tac_toe(): # Main Function For Game Play
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe!")
    print("The board is numbered as follows:")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")
    print("You are playing as X.")
    print("Enter the number where you want to place your move.")

    while True:
        game.print_board()
        if game.check_winner() is not None:
            if game.check_winner() == 1:
                print("You win!")
            elif game.check_winner() == -1:
                print("AI wins!")
            else:
                print("It's a draw!")
            break

        if game.player == 1:
            move = int(input("Enter your move (0-8): "))
            while move < 0 or move > 8 or game.board[move // 3, move % 3] != 0:
                print("Invalid move! Try again.")
                move = int(input("Enter your move (0-8): "))
            game.make_move((move // 3, move % 3))
        else:
            ai_move = game.get_best_move()
            print("AI's move:", ai_move[0] * 3 + ai_move[1])
            game.make_move(ai_move)

play_tic_tac_toe()
