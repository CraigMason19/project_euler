from decimal import *

def SumDigitsInDecimal(s):
    s = s.replace(".", "")
    return sum(int(c) for c in s)

# Two bigger than 100 to account for rounding of digits
getcontext().prec = 102

irrSum = sum(SumDigitsInDecimal(str(Decimal(i)**Decimal('0.5'))[0:101]) for i in range(1, 99+1))
ratSum = sum(i for i in range(1, 9+1))
print(irrSum-ratSum)

