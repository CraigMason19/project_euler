#-------------------------------------------------------------------------------
# Name:        Problem 010.py
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

def main():
    answer = sum(p for p in Eratosthenes(2 * (10**6)))
    print(answer)

if __name__ == '__main__':
    main()
