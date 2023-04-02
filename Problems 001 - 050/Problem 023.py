#-------------------------------------------------------------------------------
# Name:        Problem 023.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Helper import SumInRange

def IsAbundant(n):
    return sum(i for i in range(1, (n//2)+1) if n%i == 0) > n

def main():
    # Limit is defined in the problem question
    limit = 28123
    abundants = [i for i in range(1, limit+1) if IsAbundant(i) == True]

    s = set()
    for a in abundants:
        for b in abundants:
            tmp = a + b
            if tmp <= limit:
                s.add(tmp)

    print(SumInRange(limit) - sum(s))

if __name__ == '__main__':
    main()