#-------------------------------------------------------------------------------
# Name:        Problem 046
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Sieves import Eratosthenes
from math import sqrt

Primes = Eratosthenes(10**4)
Squares = [i*i for i in range(1, 10**3)]

def TestConjecture(n):
    for prime in Primes:
        if prime < n:
            result = n - prime
            square = result / 2
            if square in Squares:
                return "%d = %d + 2x%d^2" % (n, prime, int(sqrt(square)))
        else:
            return None

def main():
    i = 9 # First odd composite number
    while True:
        if i not in Primes:
            s = TestConjecture(i)
            if s != None:
                print(s)
            else:
                print(i)
                break
        i += 2 # We only want odd numbers

if __name__ == '__main__':
    main()
