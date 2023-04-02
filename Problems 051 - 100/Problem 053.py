#-------------------------------------------------------------------------------
# Name:        Problem 053
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from math import factorial

def main():
    answer = 0

    for n in range(1, 100+1):
        for r in range(1, n):
            tmp = factorial(n) / (factorial(r) * (factorial(n-r)))
            if tmp > 10**6:
                answer += 1

    print(answer)

if __name__ == '__main__':
    main()


