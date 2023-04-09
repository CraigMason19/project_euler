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
sys.path.append('Helper')

from primes import number_of_divisors

def GetTriangleNumberByTerm(t):
    return (t*(t+1)//2)

def main():
    term, limit = 1, 500

    while True:
        tn = GetTriangleNumberByTerm(term)
        if number_of_divisors(tn) > limit:
            break
        else:
            term += 1

    print(tn)

if __name__ == '__main__':
    main()












