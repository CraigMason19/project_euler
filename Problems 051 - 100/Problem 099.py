#-------------------------------------------------------------------------------
# Name:        Problem 099
#
# Links:       http://math.stackexchange.com/questions/8308/working-with-large-exponents
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

# ab > cd
# log(ab) > log(cd)
# blog(a) > dlog(c)

from math import log

class LargePower:
    def __init__(self, b=None, e=None):
        self.mBase = b
        self.mExponent = e

    def __str__(self):
        return "["+str(self.mBase)+"^"+str(self.mExponent)+"]"

    def __repr__(self):
        return "LargePower(%d, %d)" % (self.mBase, self.mExponent)

    def CreateFromList(l):
        return LargePower(l[0], l[1])

def IsBigger(a, b):
    return (a.mExponent*log(a.mBase) > b.mExponent*log(b.mBase))

def main():
    biggestNum, lineNumber = LargePower(1, 1), 0
    i = 0

    with open("./Problems 051 - 100/base_exp.txt") as file:
        for line in file:
            i += 1
            tmpNum = LargePower.CreateFromList([int(s) for s in line.split(",")])
            if IsBigger(tmpNum, biggestNum):
                biggestNum = tmpNum
                lineNumber = i

    print(biggestNum, "Line", lineNumber)

if __name__ == '__main__':
    main()












