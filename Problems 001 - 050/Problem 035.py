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
sys.path.append('..\..\Helper')
from Sieves import Eratosthenes
from Primes import IsCircularPrime

def main():
    answer = len([i for i in Eratosthenes(10**6) if IsCircularPrime(i)])
    print(answer)

if __name__ == '__main__':
    main()








