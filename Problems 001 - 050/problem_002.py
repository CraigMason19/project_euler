#-------------------------------------------------------------------------------
# Name:        problem_002.py
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

def main(print_info=False):
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

    if print_info:
        print(answer)

    return answer

if __name__ == '__main__':
    main(print_info=True)