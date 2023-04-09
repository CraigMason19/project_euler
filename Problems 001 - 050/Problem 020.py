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
sys.path.append('Helper')

from general import sum_of_digits
from math import factorial

def main():
    print(sum_of_digits(factorial(100)))

if __name__ == '__main__':
    main()