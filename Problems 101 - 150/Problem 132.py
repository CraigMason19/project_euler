#-------------------------------------------------------------------------------
# Name:        Problem 132
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

# Repunits
#
# R(1) = 1, R(3) = 111, R(10) = 1111111111
#
#
#         (10 ^ k) - 1
# R(k) = --------------
#              9
#
# To see if a prime number (p) is a factor we check the modulus
# if R(k) = 0 (mod p) -> its a factor
# We the use algebra to remove the 9 from the left hand side which when
# writting out and rearrange the equation to...
#
# (10^k) - 1 = 0 (mod 9p)
# (10^k) = 1 (mod 9p)
#

Primes = Eratosthenes(3000000)

# Memory need, possible memory problems. Tested upto k = 10**6
def RepuintDistinctPrimeFactors(k):
    # Housekeeping
    if k <= 0:
        return 0
    elif k == 1:
        return 1

    n = int("1" * k)
    factors = []
    product = 1

    for p in Primes:
        if product == n:
            break

        if pow(10, k, 9*p) == 1:
            factors.append(p)
            product *= p

    # Maybe there is a prime factor but it is much larger than our prime list
    if not factors:
        return [n]
    # There are bigger prime factors than we have OR a prime is used again
    elif product != n:
        factors.append('->')
        return factors
    # We have found them all
    else:
        return factors

# Won't find them all
def RepuintDistinctPrimeFactorsVeryLarge(k):
    # Housekeeping
    if k <= 0:
        return 0
    elif k == 1:
        return 1

    factors = []

    for p in Primes:
        if pow(10, k, 9*p) == 1:
            factors.append(p)

    # Maybe there is a prime factor but it is much larger than our prime list
    if not factors:
        return [n]
    # There are bigger prime factors than we have OR a prime is used again
    else:
        factors.append('->')
        return factors

def main():
##    for i in range(20):
##        l = RepuintDistinctPrimeFactors(i)
##        print("R(%d)" % i)
##        print(l)
##        print()

    l = RepuintDistinctPrimeFactorsVeryLarge(10**9)
    print(l, len(l))
    print(sum(l[:40]))

if __name__ == '__main__':
    main()
