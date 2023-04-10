#-------------------------------------------------------------------------------
# Name:        Problem 069
#
# Links:
#
# Notes:       ?? 2 * 3 * 5 * 7 * 11 * 13 * 17 ??
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from sieves import phi

def main():
    maxPhi, answer = 0, 0

    for i, p in enumerate(phi(10**6+1)):
        # Prevent divide by zero error
        if i == 0:
            continue

        if i/p > maxPhi:
            maxPhi, answer = i/p, i

    print(answer)


if __name__ == '__main__':
    main()
