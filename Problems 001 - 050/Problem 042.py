#-------------------------------------------------------------------------------
# Name:        Problem 042
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from math import sqrt, floor

def AlphabeticPositionOfChar(c):
    return (ord(c.lower()) - 96)

def CalculateWordValue(word):
    return sum(AlphabeticPositionOfChar(s) for s in word)

def IsTriangleNumber(n):
    term = (sqrt((8*n)+1)-1) / 2
    return (term == floor(term))

def main():
    answer, words = 0, []

    with open("words.txt") as f:
        for line in f:
            line = line.replace('"', '')
            words = line.split(",")

    for word in words:
        tmp = CalculateWordValue(word)
        if IsTriangleNumber(tmp):
            answer += 1

    print(answer)

if __name__ == '__main__':
    main()


