#-------------------------------------------------------------------------------
# Name:        Problem 024.py
#
# Notes:       Sort of cheating by using Python?
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import itertools

def main():
    l = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
    print(''.join(str(n) for n in l[1000000-1]))

if __name__ == '__main__':
    main()



