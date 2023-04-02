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
sys.path.append('..\..\Helper')
from Helper import Product
from Sieves import Eratosthenes
from Primes import DistinctPrimeFactors
from operator import itemgetter

def Radical(n, primes):
    if n == 1:
        return 1

    return Product(DistinctPrimeFactors(n, primes))

def main():
    primes = Eratosthenes(10**5)
    l = [[i, Radical(i, primes)] for i in range(1, 10**5+1)]
    l.sort(key=itemgetter(1, 0))
    print(l[10**4-1][0])

if __name__ == '__main__':
    main()
