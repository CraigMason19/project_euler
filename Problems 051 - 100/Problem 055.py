#-------------------------------------------------------------------------------
# Name:        Problem 055
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

import math

def IsPalindrome(s):
    return (s == s[::-1])

def IsLychrelNumber(n):
    for i in range(1, 50+1):
        s = str(n)
        n = int(s) + int(s[::-1])
        if IsPalindrome(str(n)):
            return True

    return False

def main():
    L = [i for i in range(1, 10000) if IsLychrelNumber(i)]
    print (10000-1 - len(L))

if __name__ == '__main__':
    main()


