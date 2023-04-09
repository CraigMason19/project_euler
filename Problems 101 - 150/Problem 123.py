#-------------------------------------------------------------------------------
# Name:        Problem 123
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from sieves import eratosthenes

def EquationStr(n, p, r):
    return "%d^%d + %d^%d = %d (mod %d)" % (p-1, n, p+1, n, r, p**2)

# r= 2p_nn
def R(n, p):
    #tmp = ((p-1)**n) + ((p+1)**n)
    #q, r = divmod(tmp, p**2)
    #return r
    return 2 * p * n

def main():
    remainderLength = 10**10

    # Extend this array so that it is easier to index
    primes = [0] + eratosthenes(10**6)

    # Even numbers always have a remainder of 2 so we can ignore them
    for i in range(1, len(primes), 2):
        n = i
        p = primes[n]
        r = R(n, p)

        if r > remainderLength:
            print(EquationStr(n, p, r))
            break

    if r < remainderLength:
        print("Need more primes!")

if __name__ == '__main__':
    main()
