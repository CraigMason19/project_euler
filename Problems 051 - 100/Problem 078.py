#-------------------------------------------------------------------------------
# Name:        Problem 078
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Partitions import NumberOfPartitionsGenerator

def main():
    p, n = NumberOfPartitionsGenerator(), 0

    while True:
        # The first partition returned is p(0)
        partitions = next(p)

        if partitions % 10**6 == 0:
            print("p(%d) = %d" % (n, partitions))
            break

        n += 1

if __name__ == '__main__':
    main()
