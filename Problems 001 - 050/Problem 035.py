#-------------------------------------------------------------------------------
# Name:        Problem 035
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from sieves import eratosthenes
from primes import is_circular_prime

def main():
    answer = len([i for i in eratosthenes(10**6) if is_circular_prime(i)])
    print(answer)

if __name__ == '__main__':
    main()








