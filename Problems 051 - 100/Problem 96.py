#-------------------------------------------------------------------------------
# Name:        Problem 096
#
# Links:       http://www.math.cornell.edu/~mec/Summer2009/meerkamp/Site/Solving_any_Sudoku_I.html
#
# Notes:       Similar to 'Latin Squares' by Euler
#
# TODO:
#-------------------------------------------------------------------------------

from collections import Counter
from math import floor

def Unique(seq):
    counter = Counter(seq)
    for number in seq:
        if counter[number] > 1:
            return False
    return True

class Sudoku3x3:
    """ Representation of the 'Classic' Sudoku shape as a 2D array"""
    def __init__(self):
        self.MaxValue = 45 # (1+2+3+4+5+6+7+8+9)
        self.Rows = 9
        self.Columns = 9
        self.Data = [[0 for x in range(9)] for y in range(9)]
        self.Fixed = [[False for x in range(9)] for y in range(9)]
        self.Solved = False
        self.MovesToSolve = 0

    def GetRow(self, row):
        return self.Data[row]

    def GetColumn(self, col):
        return [row[col] for row in self.Data]

    def GetSubGrid(self, row, col):
        subGridRow = floor(row / 3)
        subGridCol = floor(col / 3)

        startRow = subGridRow * 3
        endRow = startRow + 2

        startCol = subGridCol * 3
        endCol = startCol + 2

        l = []
        for i in range(startRow, endRow+1):
            l.extend(self.Data[i][startCol:endCol+1])

        return l

    def Load(self, textArray):
        self.Solved = False
        self.MovesToSolve = 0

        for i, row in enumerate(textArray):
            self.Data[i] = [int(x) for x in row]
            self.Fixed[i] = [True if int(x) != 0 else False for x in row]

    def FindFirstSpace(self):
        """ First space from the start that is a zero and not fixed """
        for row in range(self.Rows):
            for col in range(self.Columns):
                if self.Data[row][col] == 0:
                    if self.Fixed[row][col] == False:
                        return row, col
        return None, None

    def FindLastSpace(self):
        """ First space from the end that is not zero and not fixed """
        for row in reversed(range(self.Rows)):
            for col in reversed(range(self.Columns)):
                if self.Data[row][col] != 0:
                    if self.Fixed[row][col] == False:
                        return row, col
        return None, None

    def FindPreviousSpace(self, row, col):
        """ Find the next space that is NOT fixed """
        if row < 0 and col < 0:
            return None, None

        x, y = row, col
        while True:
            if row < 0:
                return None, None

            y -= 1
            if y < 0:
                y = 8
                x -= 1
                if x < 0:
                    x = 8

            if self.Fixed[x][y] == False:
                return x, y

    def Solve(self):
        """ Solves the grid, assumes it is a possible solve """

        backtracking, validCell = False, False
        row, col = self.FindFirstSpace()
        self.Data[row][col] = 1

        while(True):
            self.MovesToSolve += 1

            # Exit condition
            if self.Fixed[8][8]:
                x, y = self.FindPreviousSpace(8,8)
            else:
                x, y = 8, 8
            if self.ValidateCell(x, y):
                break

            #
            if not backtracking:
                validCell = self.ValidateCell(row, col)
            else:
                backtracking = False
                validCell = False

            #
            if validCell:
                row, col = self.FindFirstSpace()
                self.Data[row][col] = 1
                backtracking = False

            #
            if not validCell:
                self.Data[row][col] += 1
                if self.Data[row][col] > 9:
                    self.Data[row][col] = 0
                    row, col = self.FindPreviousSpace(row, col)
                    backtracking = True

        self.Solved = True

    def ValidateCell(self, row, col):
        """ Checks if a cells validity in a row, colum and subgrid """
        # If cell is empty then validation has failed
        if self.Data[row][col] == 0:
            return False

        # Check rows for duplicates
        r = self.GetRow(row)
        r = [x for x in r if x != 0]
        if not Unique(r):
            return False

        # Check columns for duplicates
        c = self.GetColumn(col)
        c = [x for x in c if x != 0]
        if not Unique(c):
            return False

        # Check Subgrids for duplicates
        sg = self.GetSubGrid(row, col)
        sg = [x for x in sg if x != 0]
        if not Unique(sg):
            return False

        return True

    def __str__(self): # TODO - remove last "\n"
        s = ""
        for row in self.Data:
            s += str(row) + "\n"
        return(s)

    def __repr__(self):
        return "Sudoku3x3()"

def main():
    # Read our text file of grids
    sudokuGrids = []
    with open("sudoku.txt") as f:
        while True:
            line = f.readline()
            # EOF
            if not line:
                break

            grid = [f.readline().strip() for i in range(9)]
            sudokuGrids.append(grid)

    s, answer = Sudoku3x3(), 0

    for i, grid in enumerate(sudokuGrids):
        s.Load(grid)
        s.Solve()
        number = int(''.join(map(str, s.GetRow(0)[:3])))
        answer += number
        print(i, s.MovesToSolve)
        print(s)

    print(answer)

if __name__ == '__main__':
    main()
