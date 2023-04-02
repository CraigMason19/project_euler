#-------------------------------------------------------------------------------
# Name:        Problem 012.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Primes import NumberOfDivisors

def GetTriangleNumberByTerm(t):
    return (t*(t+1)//2)

def main():
    term, limit = 1, 500

    while True:
        tn = GetTriangleNumberByTerm(term)
        if NumberOfDivisors(tn) > limit:
            break
        else:
            term += 1

    print(tn)

if __name__ == '__main__':
    main()












