#-------------------------------------------------------------------------------
# Name:        Problem 003.py
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

def main():
    pf = PrimeFactors(600851475143)
    print(pf[-1])

if __name__ == '__main__':
    main()
