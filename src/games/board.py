'''
a 2D board is randomly divided between two playes (0 and 1)
players can move to adjacent cells to capture territory
a player wins by completing a row, column, or diagonal
'''

import numpy as np


class Board:
    def __init__(self, size: int = 50):
        '''
        Initialize the board with two colors (0 and 1) randomly assigned.
        size: size of the board (size x size)
        '''
        self.size = size
        self.grid = np.random.choice([0, 1], size=(size, size))
        self.row_sums = np.sum(self.grid, axis=1)
        self.col_sums = np.sum(self.grid, axis=0)
        self.diag_sum = np.sum(np.diag(self.grid))
        self.anti_diag_sum = np.sum(np.diag(np.fliplr(self.grid)))

    def display(self):
        '''
        Print the board to the console.
        '''
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))

    def check_winner(self) -> int:
        '''
        Check if there is a winner (0 or 1), else return None.
        '''
        for player in [0, 1]:
            # Check rows
            if np.any(np.all(self.grid == player, axis=1)):
                return player
            # Check columns
            if np.any(np.all(self.grid == player, axis=0)):
                return player
            # Check main diagonal
            if np.all(np.diag(self.grid) == player):
                return player
            # Check anti-diagonal
            if np.all(np.diag(np.fliplr(self.grid)) == player):
                return player
        return None

    def move(self,player):
        pass  # TODO

    def find_best_move(self, player):
        pass  # TODO

if __name__ == '__main__':
    board = Board(size=10)
    board.display()
    winner = board.check_winner()
    if winner is not None:
        print(f"Player {winner} wins!")
    else:
        print("No winner yet.")
