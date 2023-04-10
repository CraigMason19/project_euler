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
sys.path.append('Helper')

from partitions import number_of_partitions

def main():
    p = number_of_partitions
    print(p(100) - 1)

if __name__ == '__main__':
    main()

