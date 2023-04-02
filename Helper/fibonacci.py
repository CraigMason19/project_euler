from math import sqrt
from math import floor
from math import ceil
from math import log10

GoldenRatio = (1 + sqrt(5)) / 2 # 1.6180339887
SQRT_FIVE = sqrt(5)

def FibonacciGenerator():
    a, b = 0, 1

    while True:
        a, b = b, a+b
        yield a

def LengthOfFib(n):
    # e.g. 1000 * LOG(Phi) - (LOG 5)/2 ~= 208.638155
    result = n * log10(GoldenRatio) - (log10(5)/2)
    # Take the whole part of the number and add one
    return int(result)+1

def BinetFormula(n):
    PHI = (1 + sqrt(5)) / 2
    phi = (1 - sqrt(5)) / 2
    result = (PHI**n - phi**n) / sqrt(5)
    return int(result)

def FirstDigitsOfFib(n, d):
    """
    For the fibonacci number Fib(n), return the first d digits
    """
    # http://blog.singhanuvrat.com/problems/get-first-few-digits-of-a-fibonacci-number
    temp = n * 0.20898764024997873 - 0.3494850021680094
    return int( pow( 10, temp - int( temp ) + d - 1 ) )

def IsFib(n):
    if n == 0 or n == 1:
        return True

    # take the square root, round it to the nearest integer and then square the result. If this is the same as the original whole number then the original was a perfect square
    rootA = sqrt(5 * (n*n) + 4)
    rootB = sqrt(5 * (n*n) - 4)

    if int(rootA + 0.5) ** 2 == n or int(rootB + 0.5) ** 2 == n:
        return True

    return False


##def mul(A, B):
##    a, b, c = A
##    d, e, f = B
##    return a*d + b*e, a*e + b*f, b*e + c*f
##
##def pow(A, n):
##    if n == 1:
##        return A
##    if n & 1 == 0:
##        return pow(mul(A, A), n//2)
##    else:
##        return mul(A, pow(mul(A, A), (n-1)//2))
##
##def fib(n):
##    if n < 2:
##        return n
##    return pow((1,1,0), n-1)[0]

##def FirstFibonacciTermFromLength(n):
##
##
##
##
##
### Binet's Fibonacci Number Formula
##def GetFibonacciTerm(n):
##    tmp = pow(GOLDEN_RATIO, n) - pow((1-GOLDEN_RATIO), n)
##    return int(tmp/SQRT_FIVE)
##
##
##
##def GetFirstTermByDigitLength(n):
##    tmp = n + (log10(5)/2) - 1
##    tmp2 = log10(GOLDEN_RATIO)
##    return int(ceil(tmp/tmp2))
##
##print(GetLengthOfNumber(1032654))
