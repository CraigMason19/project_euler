#-------------------------------------------------------------------------------
# Name:        Problem 047
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Sieves import Eratosthenes
from Primes import DistinctPrimeFactorsCount, IsPrime
##
##def HasPrimeFactors(n, factors):
##    tmp = n//2+1
##    primeList = []
##    for i in range(2, tmp):
##        if n%i == 0 and IsPrime(i):
##            primeList.append(i)
##
##    print (primeList, n)
##    return (len(primeList) >= factors)
##
##L = []
##for n in range(134040, 134500):
##    dpf = 4 # Distinct prime factors
##    if HasPrimeFactors(n, dpf):
##        if HasPrimeFactors(n+1, dpf):
##            if HasPrimeFactors(n+2, dpf):
##                if HasPrimeFactors(n+3, dpf):
##                    print( n, n+1, n+2, n+3)
##                    break

##[2, 3, 5, 1117] 134040
##[311, 431] 134041
##[311, 431] 134041
##[2, 67021] 134042
##[3, 7, 13, 491] 134043
##[2, 23, 31, 47] 134044
##[5, 17, 19, 83] 134045
##[2, 3, 11, 677] 134046
##134043 134044 134045 134046

def Do(n):
    primfac = set()

    if n == 0 or n == 1:
        return {0}

    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.add(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.add(n)
    return primfac

def main():
    i = 1
    dpf = 2

    primes = Eratosthenes(10**5)
    for i in range(10, 10**5):
        x, y =  i, DistinctPrimeFactorsCount(i)

    print("hello")




##    l = [0, 0]
##    answer = 0
##
##    for i in range(14, 20):
##        tmp = DistinctPrimeFactorsCount(i)
##        l[1] = tmp
##
##        if l[0] == l[1] == 2:
##            print(i-1, i)
##            break
##
##        l[0] = l[1]
##
##    l = [0, 0, 0, 0]
####
##    for i in range(100000, 10**7):
##        #tmp = DistinctPrimeFactorsCount(i, primes)
##        tmp = Do(i)
##        l[3] = tmp
##
##
##
##        if l[0] == l[1] == l[2] == l[3] == 4:
##            print(i-3, i-2, i-1, i)
##            break
##
##        l[0] = l[1]
##        l[1] = l[2]
##        l[2] = l[3]
##
if __name__ == '__main__':
    main()
