import numpy as np
import torch
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class ConnectFour:
    def __init__(self):
        self.board = torch.zeros(6,7, dtype=int)
        self.current_player = 1
        
    def render(self):
        return render(self.board)

    def legal_moves(self):
        return [col for col in range(7) if self.board[0, col] == 0]

    def make_move(self, column):
        if column not in self.legal_moves():
            raise ValueError(f'Column {column} is full, pick a new move.')
            
        for row in reversed(range(6)):
            if self.board[row, column] == 0:
                self.board[row, column] = self.current_player
                self.current_player *= -1
                return

    def get_winner(self):
        rows, cols = self.board.shape
        
        # rows
        for row in range(rows):
            for col in range(cols-3):
                window = self.board[row, col:col+4] 
                window_sum = window.sum()
                if window_sum == 4:
                    return 1
                elif window_sum == -4:
                    return -1
                
        # cols
        for col in range(cols):
            for row in range(rows-3):
                window = self.board[row:row+4, col]
                window_sum = window.sum()
                if window_sum == 4:
                    return 1
                elif window_sum == -4:
                    return -1
                    
        # diagonals
        for row in range(3, rows):
            for col in range(cols - 3):
                window = [self.board[row - i, col + i] for i in range(4)]
                total = sum(window)
                if total == 4:
                    return 1
                elif total == -4:
                    return -1

        
        for row in range(rows - 3):
            for col in range(cols - 3):
                window = [self.board[row + i, col + i] for i in range(4)]
                total = sum(window)
                if total == 4:
                    return 1
                elif total == -4:
                    return -1
        
        return None
        

    def is_over(self):
        return len(self.legal_moves()) == 0 or self.get_winner() is not None

    def is_draw(self):
        return self.get_winner() is None and len(self.legal_moves())==0

    def get_result(self):
        if self.is_over() and not self.get_winner():
            return 0
        elif self.is_over():
            return self.get_winner()

    def clone(self):
        new_game = ConnectFour()
        new_game.board = self.board.clone()
        new_game.current_player = self.current_player
        return new_game










## ----------------- ##
## Render Game State ##
## ----------------- ##

def render(tensor):
    array = tensor.numpy()
    rows, cols = array.shape

    fig, ax = plt.subplots(figsize=(cols, rows))
    ax.set_aspect(1)
    ax.set_xlim(-0.5, cols - 0.5)
    ax.set_ylim(-0.5, rows - 0.5)
    array = np.flipud(array)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('blue')

    
    def get_color(val):
        if val == 1:
            return 'red'
        elif val == -1:
            return 'yellow'
        else:
            return 'white'

    for row in range(rows):
        for col in range(cols):
            color = get_color(array[row, col])
            circle = plt.Circle((col, row), 0.4, color=color, alpha=0.9, ec='black', linewidth=1)
            ax.add_patch(circle)


    for row in range(rows + 1):
        ax.axhline(row - 0.5, color='gray', lw=0.5)
    for col in range(cols + 1):
        ax.axvline(col - 0.5, color='gray', lw=0.5)
    
    plt.show()
            
