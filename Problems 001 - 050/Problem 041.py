#-------------------------------------------------------------------------------
# Name:        Problem 041
#
# Links:       http://en.wikipedia.org/wiki/Divisibility_rule#Divisibility_by_3_or_9
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from sieves import eratosthenes
from general import is_pandigital

# Solved using the divisibility rule for 3 or 9 from wikipedia. The rule states
#
# "First, take any number (for this example it will be 492) and add together
# each digit in the number (4 + 9 + 2 = 15). Then take that sum (15) and
# determine if it is divisible by 3. The original number is divisible by 3
# (or 9) if and only if the sum of its digits is divisible by 3 (or 9)."
#
# n  pandigital            sum  divisibilty by 3
# 9  (1+2+3+4+5+6+7+8+9) = 45   45 / 3 = 15
# 8  (1+2+3+4+5+6+7+8) =   36   36 / 3 = 12
# 7  (1+2+3+4+5+6+7) =     28   28 / 3 = 9.333333333333
# 6  (1+2+3+4+5+6) =       21   21 / 3 = 7
# 5  (1+2+3+4+5) =         15   15 / 3 = 5
# 4  (1+2+3+4) =           11   11 / 3 = 3.666666666666
# 3  (1+2+3) =             7    7  / 3 = 2.333333333333
#
# For a 3 digit we would look for divisibity by 7. So we can see that we need
# to look for 4 digit and 7 digit pandigitals.

def main():
    answer = 0

    for p in eratosthenes(10**7):
        if is_pandigital(p):
            answer = p

    print(answer)

if __name__ == '__main__':
    main()