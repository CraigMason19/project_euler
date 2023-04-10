#-------------------------------------------------------------------------------
# Name:        Problem 066
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from continued_fractions import ContinuedFraction
from math import sqrt

def PellEquationString(n, h, k):
    return "%d^2 - %d * %d^2 = 1" % (h, n, k)

def IsPellEquation(n, h, k):
    return (h*h) - (n * (k*k)) == 1

def main():
    limit = 1000
    answer, largest = 0, 0

    for square in range(2, limit+1):
        # No need to check perfect squares
        if sqrt(square).is_integer():
            continue
        else:
            cf = ContinuedFraction()
            cf.CreateFromSquare(square)
            cg = cf.ConvergentsGenerator()

            while True:
                h, k = next(cg)
                if IsPellEquation(square, h, k):
                    print(PellEquationString(square, h, k))
                    if h > largest:
                        answer, largest = square, h
                    break

    print(answer)

if __name__ == '__main__':
    main()
