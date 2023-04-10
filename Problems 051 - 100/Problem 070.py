#-------------------------------------------------------------------------------
# Name:        Problem 070
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from sieves import phi

# e.g 87109 is a permutation of 79180
def IsPermutation(a, b):
    return ''.join(sorted(str(a))) == ''.join(sorted(str(b)))

def main():
    limit = 10**7
    lowest = (0, 0, limit)
    totients = phi(limit)

    for n, t in enumerate(totients):
        # 0 Would cause divide by zero errors - n=0 p=0 n/p=0/0
        # 1 Also causes a problem as n=1 p=1 p/n=1,1
        if n == 0 or n == 1:
            continue

        if IsPermutation(n, t):
            result = n/t
            if result < lowest[2]:
                lowest = (n, t, result)

    print(lowest)

if __name__ == '__main__':
    main()
