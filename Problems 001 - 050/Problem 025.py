#-------------------------------------------------------------------------------
# Name:        Problem 025.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Fibonacci import FibonacciGenerator

def main():
    fg = FibonacciGenerator()

    fib = next(fg)
    count = 1

    while True:
        fib = next(fg)
        count += 1
        if len(str(fib)) == 1000:
            break

    print(count)

if __name__ == '__main__':
    main()