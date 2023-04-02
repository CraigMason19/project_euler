#-------------------------------------------------------------------------------
# Name:        Problem 026.py
#
# Notes:
#
# Links:       http://en.wikipedia.org/wiki/Repeating_decimal
#              http://en.wikipedia.org/wiki/Fermat%27s_little_theorem
#              http://oeis.org/A002371
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Sieves import Eratosthenes

# Solved using wikipedia and Fermat's Little theorem
# From wikipedia...
# "A fraction in lowest terms with a prime denominator other than 2 or 5
# (i.e. coprime to 10) always produces a repeating decimal. The length of the
# repetend (period of the repeating decimal) of 1/p is equal to the order of 10
# modulo p. If 10 is a primitive root modulo p, the repetend length is equal to
# p − 1; if not, the repetend length is a factor of p − 1. This result can be
# deduced from Fermat's little theorem, which states that 10^p−1 = 1 (mod p)".
#
# So, we need to look at the factors of p-1. If one of these factors satisfies
# the equation then we return that factor otherwise, if no factors satisfy the
# equation the result is p-1.
#
# Fermat's little theorem, which states that 10p−1 = 1 (mod p)
# Search factors of p-1
# 10^1 = 1 (mod p)
# 10^2 = 1 (mod p)
# 10^3 = 1 (mod p)
# etc...

# Returns the period of decimal expansion of 1/(n-th prime)
# (0 by convention for the primes 2 and 5)
def PrimeCycleLength(p):
    for n in range(1, p):
        if 10**n % (p) == 1:
            return n

    return 0

def main():
    answer, period = 0, 0

    for prime in Eratosthenes(10**3):
        tmp = PrimeCycleLength(prime)
        if tmp > period:
            answer, period = prime, tmp

    print(answer, period)

if __name__ == '__main__':
    main()
