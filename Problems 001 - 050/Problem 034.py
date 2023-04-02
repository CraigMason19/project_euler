#-------------------------------------------------------------------------------
# Name:        Problem 034
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from math import factorial

def IsFactorion(n):
    return sum(factorial(int(i)) for i in str(n)) == n

def main():
    answer = sum(i for i in range(3, 100000) if IsFactorion(i))
    print(answer)

if __name__ == '__main__':
    main()
