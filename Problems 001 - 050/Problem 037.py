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
sys.path.append('Helper')

from primes import is_left_right_truncatable_prime
from sieves import eratosthenes

def main():
    # 2, 3, 5 and 7 are not considered truncatable so skip these four numbers
    primes = eratosthenes(10**6)[4:]
    answer = sum(p for p in primes if is_left_right_truncatable_prime(p))
    print(answer)

if __name__ == '__main__':
    main()

