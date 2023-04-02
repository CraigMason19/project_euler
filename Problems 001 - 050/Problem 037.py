#-------------------------------------------------------------------------------
# Name:        Problem 037
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Primes import IsLeftRightTruncatablePrime
from Sieves import Eratosthenes

def main():
    # 2, 3, 5 and 7 are not considered truncatable so skip these four numbers
    primes = Eratosthenes(10**6)[4:]
    answer = sum(p for p in primes if IsLeftRightTruncatablePrime(p))
    print(answer)

if __name__ == '__main__':
    main()

