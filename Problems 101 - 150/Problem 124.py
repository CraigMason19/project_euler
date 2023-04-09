#-------------------------------------------------------------------------------
# Name:        Problem 124.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from general import product
from sieves import eratosthenes
from primes import distinct_prime_factors
from operator import itemgetter

def Radical(n, primes):
    if n == 1:
        return 1

    return product(distinct_prime_factors(n, primes))

def main():
    primes = eratosthenes(10**5)
    l = [[i, Radical(i, primes)] for i in range(1, 10**5+1)]
    l.sort(key=itemgetter(1, 0))
    print(l[10**4-1][0])

if __name__ == '__main__':
    main()
