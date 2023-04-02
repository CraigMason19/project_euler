#-------------------------------------------------------------------------------
# Name:        Problem 100
#
# Links:       https://oeis.org/A046090
#               -> (total discs)
#              http://oeis.org/A011900
#               -> (blue discs)
#              https://oeis.org/A001109
#               -> (red discs)
#
# Notes:       I really like the OEIS; What a great idea
#
# TODO:
#-------------------------------------------------------------------------------

from math import sqrt, ceil, floor
from fractions import Fraction

def PellNumberGenerator():
    yield 0
    yield 1

    a, b = 0, 1
    while True:
        pell = a + b + b
        yield pell
        a, b = b, pell

PNG = PellNumberGenerator()
PellNumbers = [next(PNG) for i in range(20)]

def TotalDiscsCalculator(n):
    t = 2 * PellNumbers[n] * PellNumbers[n+1]
    if n % 2 == 0:
        return t+1
    else:
        return t

def TestArrangement(t, b):
    # pbb -> Probability of blue, blue
	pbb = Fraction(b, t) * Fraction(b-1, t-1)
	if pbb == Fraction(1, 2):
		return True

	return False

def main():
    arrangementCount = 1
    t = 0

    while True:
        # Exit condition
        if t > 10**12:
            break

        # Calculate t,b and r
        t = TotalDiscsCalculator(arrangementCount)
        b = int(ceil(t / sqrt(2)))
        r = t - b

        # Should be a 50/50 chance of 2 blue counters
        if TestArrangement(t, b):
            print("t:%d, b:%d, r:%d" % (t, b, r))

        arrangementCount += 1

if __name__ == '__main__':
    main()
