#-------------------------------------------------------------------------------
# Name:        Problem 020.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Helper import SumOfDigits
from math import factorial

def main():
    print(SumOfDigits(factorial(100)))

if __name__ == '__main__':
    main()