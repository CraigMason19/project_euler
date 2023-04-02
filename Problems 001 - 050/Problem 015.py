#-------------------------------------------------------------------------------
# Name:        Problem 015.py
#
# Notes:       Related to Pascal's triangle
#
# Links:       http://mathforum.org/advanced/robertd/manhattan.html
#
# TODO:
#-------------------------------------------------------------------------------

from math import factorial

def NChooseK(n, k):
    if n == 1:
        return n

    return factorial(n) // (factorial(k) * factorial(n-k))

def main():
##    print(NChooseK(2, 1)) # 1x1 grid
##    print(NChooseK(4, 2)) # 2x2 grid
##    print(NChooseK(6, 3)) # 3x3 grid
##    print(NChooseK(8, 4)) # 4x4 grid

    print(NChooseK(20*2, 20)) # 20x20 grid

if __name__ == '__main__':
    main()



