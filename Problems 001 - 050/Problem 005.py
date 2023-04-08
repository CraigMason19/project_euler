#-------------------------------------------------------------------------------
# Name:        Problem 005
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from primes import PrimeFactors
from collections import Counter

def main():
    # All primes below the limit (20 in this case) represented in a dict. The
    # key is a prime number and the value is how many times we will use it in
    # the final calculation
    d = { 2:1, 3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1 }

    # Now look at the composites below 20
    for i in range(4, 20+1):
        if i not in d:
            # Counter class counts how many times a prime was used in its prime
            # factorization
            factorCounter = Counter(PrimeFactors(i))
            for prime in factorCounter:
                #
                ussage = factorCounter[prime]
                if ussage > d[prime]:
                    d[prime] = ussage

    # Get the product of the dictionary # e.g. { 2:4, 3:2 } -> (2*2*2*2) * (3*3)
    answer = 1
    for key, value in d.items():
        answer *= key**value

    # 232792560 = 2*2*2*2 * 3*3 * 5 * 7 * 11 * 13 * 17 * 19
    print(answer)

if __name__ == '__main__':
    main()
