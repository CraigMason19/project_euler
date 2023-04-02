#-------------------------------------------------------------------------------
# Name:        Problem 045.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from math import sqrt

def IsTriangleNumber(n):
    tmp = (sqrt((8*n)+1)-1) / 2
    return tmp == int(tmp)

def IsPentagonalNumber(n):
    tmp = (sqrt((24*n)+1)+1) / 6
    return tmp == int(tmp)

def IsHexagonalNumber(n):
    tmp = (sqrt((8*n)+1)+1) / 4
    return tmp == int(tmp)

def main():
    n = 165
    while(True):
        n += 1
        hex = n * (2*n-1)
        if IsPentagonalNumber(hex):
            print(hex)
            break;

if __name__ == '__main__':
    main()




