#-------------------------------------------------------------------------------
# Name:        Problem 056
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import math

def SumNumberString(ns):
    return sum(int(s) for s in ns)

def main():
    answer = 0
    for a in range(1, 100+1):
        for b in range(1, 100+1):
            answer = max(SumNumberString(str(pow(a, b))), answer)

    print(answer)

if __name__ == '__main__':
    main()







