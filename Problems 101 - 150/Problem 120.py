#-------------------------------------------------------------------------------
# Name:        Problem 120
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

# To solve this problem i first used the brute force code below to find the rMax
# in the range 3 -> 10. These values are [6, 8, 20, 24, 42, 48, 72, 80].
# Then i tried finding the difference between each number to see if i could find
# a pattern and i did! The differences between them are [2, 12, 4, 18, 6, 24, 8]
# and the pattern is [2*1, 6*2, 2*2, 6*3, 2*3, 6*4, 2*4] with this pattern it is
# easy to see how we can determine rMax without even using the R equation above
# For example:
# a                        rMax
# 3  -> 0  + (6*1 -> 6 ) = 6
# 4  -> 6  + (2*1 -> 2 ) = 8
# 5  -> 8  + (6*2 -> 12) = 20
# 6  -> 20 + (2*2 -> 4 ) = 24
# 7  -> 24 + (6*3 -> 18) = 42
# 8  -> 42 + (2*3 -> 6 ) = 48
# 9  -> 48 + (6*4 -> 24) = 72
# 10 -> 72 + (2*4 -> 8 ) = 80
def NextInPatternGenerator():
    six, two = 6, 2
    counter = 1

    while True:
        yield six * counter
        yield two * counter
        counter += 1

def PrintEquation(a, n, r):
    print("%d^%d + %d^%d = %d (mod %d)" % (a-1, n, a+1, n, r, a**2))

def R(a, n):
    tmp = ((a-1)**n) + ((a+1)**n)
    q, r = divmod(tmp, a**2)
    return r

def main():
##    # Brute force code
##    l = []
##
##    for a in range(3, 10+1):
##        rMax = (0, 0, 0)
##        for n in range(1, (a**2)+1):
##            r = R(a, n)
##
##            if r > rMax[2]:
##                rMax = (a, n, r)
##
##        l.append(rMax)
##
##    for element in l:
##        PrintEquation(element[0], element[1], element[2])

    # Solution
    nipg = NextInPatternGenerator()
    rTotal, rCurrent = 0, 0

    for i in range(3, 1000+1):
        rCurrent += next(nipg)
        rTotal += rCurrent

    print(rTotal)

if __name__ == '__main__':
    main()
