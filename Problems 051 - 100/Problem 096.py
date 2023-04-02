#-------------------------------------------------------------------------------
# Name:        Problem 096
#
# Links:       
#
# Notes:       
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\\..\\Python Experiments')

import sudoku

def main():
    sudoku_grids, answer = [], 0

    # Load all the grids from the text file
    with open('sudoku.txt', 'r') as f:
        while True:
            # Grid number
            line = f.readline()
            # EOF
            if not line:
                break

            grid = [f.readline().strip() for i in range(9)]
            sudoku_grids.append(grid)

    # Loop through all our grids and collate the answer
    for grid in enumerate(sudoku_grids):
        s = sudoku.Sudoku3x3.from_grid(grid)
        s.solve()

        # Add the top 3-digits in the top-left corner
        number = int(''.join(map(str, s.row(0)[0:3])))
        answer += number

        # If we want to print them out
        # print(f'grid {i + 1}: moves to solve: {s.moves_to_solve}')
        # print(s)

    print('answer:', answer)

if __name__ == '__main__':
    main()