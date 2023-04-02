from collections import Counter
from Helper import Product

def IsPrime(n):
    # 2 is the first prime
    if n < 2:
        return False
    if n == 2:
        return True

    # And the only even prime
    if n % 2 == 0:
        return False

    # So only search odd numbers lower than it's sqrt. Every prime has a sqrt
    # but this is not integer division, therefore check every odd integer below
    # this threshold for division.
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True

def IsCircularPrime(n):
    s = str(n)
    for i in range(0, len(s)):
        s = s[1:]+s[0] # e.g 197 = digit 1 to end plus beginning ( 97+1 = 91)
        if not IsPrime(int(s)):
            return False

    return True

def IsLeftRightTruncatablePrime(n):
    l = len(str(n))
    for i in range(0, l):
        if not IsPrime(int(str(n)[i:])):
            return False
        if not IsPrime(int(str(n)[0:l-i])):
            return False

    return True

def PrimeFactors(n):
    primeFactors = []
    d = 2

    while(n > 1):
        while(n % d == 0):
            primeFactors.append(d)
            n = n / d
        d += 1
    return primeFactors



# prime list less than sqrt
def PrimeFactors2(n, primeList):
    l = []
    for prime in primeList:
        if prime > n:
            break
        if n % prime == 0:
            l.append(prime)
    return l


# //////////////////////////////////////////////////////////////////////////////
# Distinct Prime Factors
# //////////////////////////////////////////////////////////////////////////////

# todo add a get distint ct prime factors and exponents
# def DistinctPrimeFactorsWithExponents(n, primeList=None):
#def DistinctPrimeFactorsWithExponents(n):

#def NumberOfDivisors(n, primeList=None):
      # def DistinctPrimeFactorsCount

# TODO
def DistinctPrimeFactors(n, primeSeq = None):
    # Can supply a list of precalculated primes to speed things up
    if primeSeq != None:
        primeFactors = []
        for p in primeSeq:
            if p > n:
                break
            elif n % p == 0:
                primeFactors.append(p)
        return primeFactors

    #
    else:
        primeFactors = set([])
        d = 2
        while(n > 1):
            while(n % d == 0):
                primeFactors.add(d)
                n = n / d
            d += 1

        return list(primeFactors)

def DistinctPrimeFactorsSum(n, primeSeq = None):
    if primeSeq == None:
        return sum(DistinctPrimeFactors(n))
    else:
        return sum(DistinctPrimeFactors(n, primeSeq))

def DistinctPrimeFactorsCount(n, primeSeq = None):
    if primeSeq == None:
        return len(DistinctPrimeFactors(n))
    else:
        return len(DistinctPrimeFactors(n, primeSeq))

# returns with tuple
def DistinctPrimeFactorsWithExponents(n):
    # Primes start at 2 obviously
    dpf = []
    d = 2

    while(n > 1):
        while(n % d == 0):
            dpf.append(d)
            n = n / d
        d += 1

    return [(p, e) for p, e in Counter(dpf).items()]



# To get the number of divisors for a number: take the exponents of the distinct
# prime factors, add one, and then multiply together
# e.g. 24 = 2^3 * 3^1
#      nDivisors(24) = (3+1) * (1+1) = 8
def NumberOfDivisors(n):
    dpfwe = DistinctPrimeFactorsWithExponents(n)
    return Product([exponent[1]+1 for exponent in dpfwe])
    
    
    
    #def getDivisors(n):
     #   divisors = [1]
      #  for i in xrange(2, int(n**0.5)+1):
       #         if n % i == 0:
        #                divisors.append(i)
        #return divisors + map(lambda x: n / x, reversed(divisors))
