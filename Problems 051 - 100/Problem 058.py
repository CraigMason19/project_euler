# This problem is closely related to problem 28.
#-------------------------------------------------------------------------------
# Name:        Problem 058
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

import primes

PrimeList = [] # Don't technically need one, but it's
               # intresting to see
DiagonalNumbersCount = 1 # One is a diagonal number, but NOT prime!
PrimePercentage = 1.0 

Offset = 2
Grid = 3
SectionStart = 1

while(PrimePercentage > 0.10):
    for i in range(SectionStart+Offset, (Grid*Grid)+1, Offset):
        if primes.is_prime(i): 
            PrimeList.append(i)
        DiagonalNumbersCount += 1

    PrimePercentage = float(len(PrimeList)) / float(DiagonalNumbersCount)

    SectionStart = Grid*Grid
    Grid += 2
    Offset += 2

print( Grid-2)
print(PrimePercentage)



