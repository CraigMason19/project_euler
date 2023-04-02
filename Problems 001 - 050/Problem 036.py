#-------------------------------------------------------------------------------
# Name:        Problem 036
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Helper import IsPalindrome

def main():
    # Binary palindromes must be odd, they have to start with 1 and therefore
    # have to finish with 1. Need to remove "0b" from the binary conversion
    answer = sum(i for i in range(1, 10**6, 2) if IsPalindrome(bin(i)[2:]) and IsPalindrome(i))
    print(answer)

if __name__ == '__main__':
    main()








