#-------------------------------------------------------------------------------
# Name:        Problem 076
#
# Links:
#
# Notes:       Need to take the 1 off at the end because each number is a single
#              partition. Question asks for SUMS of partitions
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('..\..\Helper')
from Partitions import NumberOfPartitions

def main():
    p = NumberOfPartitions
    print(p(100) - 1)

if __name__ == '__main__':
    main()

