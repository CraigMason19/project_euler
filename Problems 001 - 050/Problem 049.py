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
sys.path.append('..\..\Helper')
from Sieves import Eratosthenes
from Helper import IsPermutation

# Only use 4 digit primes
Primes = [p for p in Eratosthenes(10000) if len(str(p)) == 4]

def main():
    for p in Primes:
        tmp = p + 3330
        if IsPermutation(p, tmp) and tmp in Primes:
            if IsPermutation(tmp, tmp+3330) and tmp+3330 in Primes:
                print(str(p) + str(tmp) + str(tmp+3330))

if __name__ == '__main__':
    main()




