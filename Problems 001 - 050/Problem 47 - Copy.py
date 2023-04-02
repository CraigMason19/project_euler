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


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return set(factors)

# trial division algo
def PrimeFactors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def DistinctPrimeFactors(n):
    return set(PrimeFactors(n))

done = False
num = 646
count = 0

while not done:
    num += 1
    if len(set(PrimeFactors(num))) == 4:
        count += 1
    else:
        count = 0
    if count >= 4:
        done = True
        print(num)

print(PrimeFactors(864))
print(DistinctPrimeFactors(864))