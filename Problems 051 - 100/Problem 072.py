#-------------------------------------------------------------------------------
# Name:        Problem 072
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

def main():

    # Farey sequence F1 = (0/1), (1,1), but they are not counted in the redued
    # proper fraction set
    # limit = 10**6
    # result = 0
    # totients = Phi(limit+1)

    # Start at F2
    # for i in range(2, limit+1):
        # The farey length (Fn) is equal to the previous farey length (Fn-1)
        # plus the totient of n. e.g. Fn = Fn-1 + Phi(n)
        # result += totients[i]

    # print(result)

    # OR, it is the equivalent of Sum of Phi(2) -> Phi(1,000,000)
    print(sum(phi(10**6+1)[2:]))

if __name__ == '__main__':
    main()
