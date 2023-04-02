#-------------------------------------------------------------------------------
# Name:        Problem 100
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------
##
##t = 21, r = 6, b = 15
##p(bb) = (15/21)X(14/20) = 1/2
##p(bb) = 0.7142 X 0.7
##15 / 6 = 2.5
##21 / 15 = 1.4
##21 * sqrt(2) = 21.2132
##
##t = 120, r = 35, b = 85
##p(bb) = (85/120)X(84/119) = 1/2
##p(bb) = 0.708333 X 0.70588
##85 / 35 = 2.42857
##120 / 85 = 1.41176
##120 / sqrt(2) = 84.8528
##85 * sqrt(2) = 120.2081
##
##sqrt(0.5) = 0.70716
##sqrt(2) = 1.4142
##
##756872327473
##10000000000000 /
##a/b=c
##a = c*b
##a/c = b
##
##a046090
##http://www.fq.math.ca/Scanned/6-3/forget.pdf

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
##
##totalDiscGuess = 120
##guess1 = totalDiscGuess
##count = 0
##while True:
##	if count == 2:
##		break
##
###	if guess > 10**12:
###		break
##
##
##	b = totalDiscGuess / sqrt(2)
##	b = ceil(b)
##	if TestCondition(totalDiscGuess, int(b)):
##		print(totalDiscGuess, b, totalDiscGuess-guess1)
##		count += 1
##		totalDiscGuess = int(floor(totalDiscGuess * 5.8))
##		guess1 = totalDiscGuess
##		continue
##	else:
##		totalDiscGuess += 1

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
