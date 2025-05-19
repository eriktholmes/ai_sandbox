import numpy as np


class TicTacToe:
    def __init__(self, transcript=False):
        self.board = np.zeros((3,3), dtype=int)
        self.current_player = 1 # Player 1 'X' goes first
        self.transcript = transcript

    
    def render(self):
        symbols = {1:'X', -1:'O', 0:' '}
        print(f"{symbols[self.board[0][0]]}|{symbols[self.board[0][1]]}|{symbols[self.board[0][2]]}\n"
              f"-----\n"
              f"{symbols[self.board[1][0]]}|{symbols[self.board[1][1]]}|{symbols[self.board[1][2]]}\n"
              f"-----\n"
              f"{symbols[self.board[2][0]]}|{symbols[self.board[2][1]]}|{symbols[self.board[2][2]]}")

    
    def legal_moves(self):
        locations = np.argwhere(self.board==0)
        return [tuple(location) for location in locations]

    
    def make_move(self, move):
        symbols = {1:'X', -1:'O'}
        
        if self.board[move] != 0:
            raise ValueError(f"That is not a valid move")
            
        self.board[move] = self.current_player
        self.current_player *= -1

        if self.transcript == True:
            print(f"Player {self.current_player*-1} put {symbols[self.current_player*-1]} in {move}")
        
            winner = self.get_winner()
            if winner == 1:
                print("Player 1 wins")
            elif winner == -1:
                print("Player 2 wins")

    
    def get_winner(self):
        rowsum = [sum(self.board[i, :]) for i in range(3)]
        colsum = [sum(self.board[:, i]) for i in range(3)]
        diagsum = [sum(self.board[i][i] for i in range(3))]
        offdsum = [sum(self.board[i][2-i] for i in range(3))]
        if 3 in rowsum + colsum + diagsum + offdsum:
            return 1
        elif -3 in rowsum + colsum + diagsum + offdsum:
            return -1
        else:
            return None

    def a_draw(self):
        return self.get_winner() is None and self.legal_moves() == []

    
    def is_over(self):
        return self.get_winner() is not None or self.a_draw()

    
    def clone(self):
        new_game = TicTacToe()
        new_game.board = self.board.copy()
        new_game.current_player = self.current_player
        return new_game
    
