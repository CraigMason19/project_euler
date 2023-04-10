#-------------------------------------------------------------------------------
# Name:        Sudoku3x3.py
#
# Links:       https://projecteuler.net/problem=96
#              http://www.math.cornell.edu/~mec/Summer2009/meerkamp/Site/Solving_any_Sudoku_I.html
#
# Notes:       Similar to 'Latin Squares' by Leonhard Euler
#              Code used for project Euler 096
#
# TODO:
#-------------------------------------------------------------------------------

import math

MAX_VALUE = 45 # (1+2+3+4+5+6+7+8+9)

def are_unique(seq):
    return len(seq) == len(set(seq))

class Sudoku3x3:
    """ A representation of the 'Classic' Sudoku shape as a 2D array """
    def __init__(self):
        """ Create an empty 2D array that will represent the grid """
        self.grid = [[0] * 9] * 9
        self.fixed = [[False] * 9] * 9 # Was the square a fixed clue?
        self.solved, self.moves_to_solve = False, 0

    # An alternate constructor
    @classmethod
    def from_grid(cls, text_array):
        """ Constructs and returns a 3x3 Sudoku grid from a text array """
        s = cls()
        s.load(text_array)

        return s

    def load(self, text_array):
        """ Loads a text array representation of a Sudoku grid """
        self.solved, self.moves_to_solve = False, 0

        for square, row in enumerate(text_array):
            self.grid[square] = [int(square) for square in row]
            self.fixed[square] = [True if int(square) != 0 else False 
                                  for square in row]

    def row(self, row):
        """ Returns a row from the grid (0-8) """
        return self.grid[row]

    def column(self, col):
        """ Returns a column from the grid (0-8) """
        return [row[col] for row in self.grid]

    def square(self, row, col):
        """ Returns a specific square in the grid (0-8), (0-8) """
        return self.grid[row][col]

    def subgrid(self, row, col):
        """ Returns a subgrid from a square location (0-8), (0-8) """
        start_row = math.floor(row / 3) * 3
        start_col = math.floor(col / 3) * 3

        l = []
        for offset in range(0, 3):
            l.extend(self.grid[start_row + offset][start_col : start_col + 3])
                
        return l

    def find_first_empty(self):
        """ Finds the first space from the start that is a zero AND not fixed """
        for row in range(9):
            for col in range(9):
                if self.fixed[row][col] == False and self.grid[row][col] == 0:
                    return row, col

        return None, None

    def find_previous_space(self, row, col):
        """ Find a previous space that is not fixed """
        while True:
            # Walk backwards through the grid
            col -= 1

            # Go to the top right on the next line
            if col < 0:
                col = 8
                # Go to the row above
                row -= 1

            # Out of bounds
            if row < 0:
                return None, None

            if self.fixed[row][col] == False:
                return row, col

    def solve(self):
        """ Solves the grid, assumes it is a possible solve """
        backtracking, valid_square = False, False
        row, col = self.find_first_empty()
        self.grid[row][col] = 1

        while(True):
            self.moves_to_solve += 1

            # If we're on the last square and it's fixed go back, otherwise
            # validate the square
            if self.fixed[8][8]:
                x, y = self.find_previous_space(8,8)
            else:
                x, y = 8, 8
            # If the square validates - SUCCESS!
            if self.validate_square(x, y):
                break

            # If we are not backtracking we can check the squares validity.
            # If we are, we can cancel backtracking now and mark the square as
            # invalid
            if not backtracking:
                valid_square = self.validate_square(row, col)
            else:
                backtracking, valid_square = False, False

            # We have a succesful placement, so put a 1 in the next empty square
            if valid_square:
                row, col = self.find_first_empty()
                self.grid[row][col] = 1
                backtracking = False

            # We have a problem, so we first try increasing the square's value. 
            # If unsuccessful we need to reset the square's value to 0 and go to
            # the previous square we calculated (backtracking)
            if not valid_square:
                self.grid[row][col] += 1
                if self.grid[row][col] > 9:
                    self.grid[row][col] = 0
                    row, col = self.find_previous_space(row, col)
                    backtracking = True

        self.solved = True

    def validate_square(self, row, col):
        """ Checks for a square's validity in a row, column and subgrid """
        if self.grid[row][col] == 0:
            return False

        # Check the rows for duplicates. Remove 0's or they will be counted as
        # duplicates
        r = [_ for _ in self.row(row) if _ != 0]
        if not are_unique(r):
            return False

        # Check the columns for duplicates
        c = [_ for _ in self.column(col) if _ != 0]
        if not are_unique(c):
            return False

        # Check the subgrid for duplicates
        sg = [_ for _ in self.subgrid(row, col) if _ != 0]
        if not are_unique(sg):
            return False

        return True

    def __str__(self): 
        """ Produces a string representation row by row """
        s = ""
        for row in self.grid:
            s += str(row) + "\n"

        # Remove last '\n'
        return(s.rstrip())

    def __repr__(self):
        return "Sudoku3x3()"