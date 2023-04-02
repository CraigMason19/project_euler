#-------------------------------------------------------------------------------
# Name:        Problem 121
#
# Links:
#
# Notes:
#
# TODO:        (7).zfill(3), use generator not a list?
#-------------------------------------------------------------------------------

import fractions

# To solve this we need to get all possible win results for n turns then we
# take the sum of the probabilities of each win condition.
#
# For example, for 3 turns...
# bbb -> 1/2 * 1/3 * 1/4 -> 1/24
# bbr -> 1/2 * 1/3 * 3/4 -> 3/24
# brb -> 1/2 * 2/3 * 1/4 -> 2/24
# rbb -> 1/2 * 1/3 * 1/4 -> 1/24
# win probability = 1/24 + 3/24 + 2/24 + 1/24 = 7/24
# prize fund = 24/7 = 3.4285714

def ProbabiltyOfResult(result):
    f = fractions.Fraction(1, 1)
    denominator = 2

    for c in result:
        if c == '0':
            f *= fractions.Fraction(1, denominator)
        else:
            f *= fractions.Fraction(denominator-1, denominator)

        denominator += 1

    return(f)

# In order to generate the win conditions we will use binary numbers. As there
# are only two outcomes (r or b) we can use binary representations of numbers
# and replace 0's and 1's with b's and r's. Then only take results where there
# are more blue discs than red
#
# For example,
# 0000 -> bbbb
# 0001 -> bbbr
# 0010 -> bbrb
# 0100 -> brbb
def GetWinResults(n):
    bToWin = (n // 2) + 1
    l = []

    # 2 ^ 3 = 8
    # 0111 = 7
    for i in range(2**n):
        # We use [2:] to ignore the "0b" part of the binary string. zfill ensures
        # that we don't lose leading zeros as we count 0's as blue tokens
        x = bin(i)[2:].zfill(n)
        if x.count("0") >= bToWin:
            l.append(x)

    return(l)

def main():
    l = GetWinResults(15)
    #print(l, len(l))
    f = sum(ProbabiltyOfResult(x) for x in l)
    print(f, f.denominator / f.numerator)

if __name__ == '__main__':
    main()
