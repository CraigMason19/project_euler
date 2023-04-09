#-------------------------------------------------------------------------------
# Name:        Problem 119.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from general import sum_of_digits

def main():
    l = []

    # Wasn't sure if this would work so i just made up the boundries and it did!
    for b in range(2, 100+1):
        for e in range(2, 20+1):
            result = b**e
            if sum_of_digits(result) == b:
                l.append(result)

    l.sort()
    print(l[30-1])

if __name__ == '__main__':
    main()


