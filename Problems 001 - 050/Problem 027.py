#-------------------------------------------------------------------------------
# Name:        Problem 027
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from Primes import IsPrime

# Produces primes for n = 0 to 39
def EulerFormula(n):
    return n*n + n + 41

# Produces primes for n = 0 to 79
def IncredibleFormula(n):
    return n*n - 79*n + 1601

def QuadraticFormula(a, b, n):
    return n*n + a*n + b

def ConsecutivePrimeCount(f=None, a=None, b=None):
    # No function
    if f == None:
        return 0

    n = 0
    while True:
        # Which formula are we using? The quadratic formula takes more arguments
        if a != None and b != None:
            result = f(a, b, n)
        else:
            result = f(n)

        # Check for primes
        if IsPrime(result):
            n += 1
        else:
            break

    return n

def main():
    l = []

    # Find all sequences bigger than 0
    for a in range(-1000, 1000):
        for b in range(-999, 1000, 2): # b MUST be a prime therefore search odd numbers
            result = ConsecutivePrimeCount(QuadraticFormula, a, b)
            if result != 0:
                l.append((a, b, result))

    # Now search these to find the best answer
    best = (0, 0, 0)
    for x in l:
        if x[2] > best[2]:
            best = x

    print(best, best[0]*best[1])

if __name__ == '__main__':
    main()
