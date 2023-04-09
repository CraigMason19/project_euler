#-------------------------------------------------------------------------------
# Name:        Problem 038
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from general import is_pandigital

def main():
    # Only numbers less than 10,000 could be pandigital because
    # 9999 * 1 = 9999 has a 4 digit result
    # 9999 * 2 = 19998 has a 5 digit result
    # So this is the last way to get a digit length of 9. Once we get to
    # 10,000 the results will have a digit length of 10
    for i in range(1, 10**4):
        s, multipliers = "", []

        for multiplicand in range(1, 9+1):
            result = i * multiplicand
            if len(s) + len(str(result)) <= 9:
                s += str(result)
                multipliers.append(multiplicand)
            else:
                break

        if is_pandigital(s) :
            print(s, i, multipliers)

if __name__ == '__main__':
    main()



