#-------------------------------------------------------------------------------
# Name:        Problem 002.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from fibonacci import fibonacci_generator

def main():
    fg = fibonacci_generator()

    # Ignore the first result. the question starts at 1, 1 our fib sequence
    # starts at 0, 1
    next(fg)

    answer = 0
    while True:
        f = next(fg)

        if f > 10**6 * 4:
            break

        if f%2 == 0:
            answer += f

    print(answer)

if __name__ == '__main__':
    main()















