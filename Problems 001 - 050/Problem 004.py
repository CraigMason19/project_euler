#-------------------------------------------------------------------------------
# Name:        Problem 004.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from general import is_palindrome

def main():
    limit = 999
    palindromes = []

    # Work backwards from 999 -> 100
    for i in range(limit, 100, -1):
        for j in range(limit, 100, -1):
            n = i*j
            if is_palindrome(n):
               palindromes.append(n)
               break

    palindromes.sort()
    print(palindromes[-1])

if __name__ == '__main__':
    main()
