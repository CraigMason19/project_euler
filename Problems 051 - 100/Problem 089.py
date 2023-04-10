#-------------------------------------------------------------------------------
# Name:        Problem 089
#
# Links:
#
# Notes:       Deva Semper
#
# TODO:
#-------------------------------------------------------------------------------

Numerals = { 'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000  }

# e.g. IX, XC
def UsesSubtractivePairRule(s):
    for i in range(1, len(s)):
        if Numerals[s[i]] > Numerals[s[i-1]]:
            return True
    return False

# Works bellow 5000 (V with overscore).
def MinimalNumeral(n):
    s = str(n)
    length = len(s)
    # 1600 -> [1000, 600, 00, 0]
    l = [s[i].ljust(length-i, '0') for i in range(0, length)]

    numeral = ''
    for item in l:
        if item[0] != '0':
            # Determine digits, tens, hundreds, thousands
            length = len(item)
            if length == 1:
                small, mid, big = 'I', 'V', 'X'
            if length == 2:
                small, mid, big = 'X', 'L', 'C'
            if length == 3:
                small, mid, big = 'C', 'D', 'M'
            if length == 4:
                numeral += 'M' * int(item[0])
                continue

            n = int(item[0])
            if n == 1:
                numeral += small
            if n == 2:
                numeral += small+small
            if n == 3:
                numeral += small+small+small
            if n == 4:
                numeral += small+mid
            if n == 5:
                numeral += mid
            if n == 6:
                numeral += mid+small
            if n == 7:
                numeral += mid+small+small
            if n == 8:
                numeral += mid+small+small+small
            if n == 9:
                numeral += small+big
    return numeral

def NumeralToInt(s):
    if UsesSubtractivePairRule(s) == False:
        return sum(Numerals[c] for c in s)
    else:
        total = 0
        for i in range(0, len(s)-1):
            if Numerals[s[i]] < Numerals[s[i+1]]:
                total -= Numerals[s[i]]
            else:
                total += Numerals[s[i]]
    return total + int(Numerals[s[-1:]])

def main():
    l = list(line.rstrip('\n') for line in open("./Problems 051 - 100/roman.txt"))
    a = sum(len(x) for x in l)
    b = sum(len(MinimalNumeral(NumeralToInt(x))) for x in l)

    print(a, b, a-b)

if __name__ == '__main__':
    main()











