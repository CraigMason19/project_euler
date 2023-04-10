#-------------------------------------------------------------------------------
# Name:        Problem 065
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from general import sum_of_digits
from fractions import Fraction

def ContinuedFractionOfEGenerator():
    yield 2
    yield 1

    modifier = 1
    while True:
        yield 2 * modifier
        yield 1
        yield 1
        modifier += 1

def Reciprical(f):
    return Fraction(f.denominator, f.numerator)

# Looking at the drawing in the question description we can see that we need to
# identify the continued fraction sequence and then work backwards to reach a
# final fraction (A convergent). The size of numbers in the continued fraction
# list is the nth convergent that is returned. For example,
# [2; 1, 2, 1, 1, 4, 1, 1, 6, 1] contains 10 digits and 1457/536 is the 10th
# convergent
def NthConvergentOfE(n):
    cfoeg = ContinuedFractionOfEGenerator()
    e = [next(cfoeg) for i in range(n)]

    if n == 1:
        return Fraction(e[0], 1)

    # Work out the continued fraction from the bottom up
    e[-2] = e[-2] + Fraction(1, e[-1])
    e.pop()
    for i in reversed(range(0, len(e)-1)):
        e[i] = e[i] + Reciprical(e[i+1])
        e.pop()

    return Fraction(e[0], 1)

def main():
    convergent = NthConvergentOfE(100)
    print(convergent)
    print(sum_of_digits(convergent.numerator))

if __name__ == '__main__':
    main()
