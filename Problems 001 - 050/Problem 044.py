#-------------------------------------------------------------------------------
# Name:        Problem 044.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from math import sqrt, floor

def IsPentagonal(n):
    tmp = (sqrt((24*n)+1)+1) / 6
    return (tmp == floor(tmp))

def GetPentagonalByTerm(t):
    return t*(3*t-1)//2

def main():
    # I just took a guess at what the upper term might be
    pentagonals = [GetPentagonalByTerm(i) for i in range(1, 10**4)]

    for x in pentagonals:
        for y in pentagonals:
            if y > x:
                break

            if IsPentagonal(y+x) and IsPentagonal(abs(y-x)):
                print(x-y, x, y)
                exit()

if __name__ == '__main__':
    main()


