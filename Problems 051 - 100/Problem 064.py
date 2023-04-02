#-------------------------------------------------------------------------------
# Name:        Problem 064
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')

from ContinuedFractions import ContinuedFraction
from math import sqrt

def main():
    limit, answer = 10**4, 0

    for square in range(2, limit+1):
        # No need to check perfect squares
        if sqrt(square).is_integer():
            continue
        else:
            cf = ContinuedFraction()
            cf.CreateFromSquare(square)
            print("sqrt(%d) = %s" % (square, cf))
            # Does it have an odd peroid?
            if cf.period % 2 != 0:
                answer += 1

    print(answer, "Odd periods")

if __name__ == '__main__':
    main()
