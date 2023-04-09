#-------------------------------------------------------------------------------
# Name:        Problem 007.py
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

def main():
    primes = eratosthenes(10**6)
    print(primes[10001-1])

if __name__ == '__main__':
    main()



