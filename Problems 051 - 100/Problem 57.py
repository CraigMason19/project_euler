from fractions import Fraction

def HasMoreDigits(x, y):
    return len(str(x)) > len(str(y))

numer, denom, answer = 3, 2, 0

for i in range(2, 1000+1):
    numer, denom = denom*2 + numer, numer + denom
    if HasMoreDigits(numer, denom):
        answer += 1

print answer
    