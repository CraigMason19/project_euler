#-------------------------------------------------------------------------------
# Name:        Problem 049.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from sieves import eratosthenes
from general import is_permutation

# Only use 4 digit primes
Primes = [p for p in eratosthenes(10000) if len(str(p)) == 4]

def main():
    for p in Primes:
        tmp = p + 3330
        if is_permutation(p, tmp) and tmp in Primes:
            if is_permutation(tmp, tmp+3330) and tmp+3330 in Primes:
                print(str(p) + str(tmp) + str(tmp+3330))

if __name__ == '__main__':
    main()




