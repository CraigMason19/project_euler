
import sys
sys.path.append('..\..\Helper')
from Sieves import Eratosthenes

Limit = 100
primes = Eratosthenes(Limit)

lenOfPrimes = len(primes)
sumOfPrimes = sum(i for i in primes)

print(sumOfPrimes)
for i in range(1, lenOfPrimes):
    sumOfPrimes -= primes[lenOfPrimes-i]
    if(sumOfPrimes < Limit):
        print(sumOfPrimes, i)
        break

print(sumOfPrimes)

# remove beginning primes until is prime itself
for n in primes:
    sumOfPrimes -= n
    if sumOfPrimes in primes:
        print(sumOfPrimes)
        break

