#-------------------------------------------------------------------------------
# Name:        Problem 033.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from fractions import *

def IsCuriousFraction(n, d):
    nStr, dStr = str(n), str(d)

    # See if it is trivial. e.g. 30/50
    if(nStr[1] and dStr[1] == '0'):
        return False

    # e.g. 49/98 = 4/8
    elif(nStr[1] == dStr[0]):
        return(Fraction(n,d) == Fraction(nStr[0] + '/' + dStr[1]))

def main():
    answer = 0
    fractions = []

    # Must have 2 digits in numerator and denominator
    for numer in range(10, 100):
        for denom in range(10, 100):
            f = Fraction(numer, denom)
            if f < 1.0:
                if IsCuriousFraction(numer, denom):
                    fractions.append([numer, denom, f])

    answer = Fraction(1, 1)
    for f in fractions:
        answer *= Fraction(f[0], f[1])
        print(f)

    print(answer)

if __name__ == '__main__':
    main()

