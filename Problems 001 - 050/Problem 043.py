#-------------------------------------------------------------------------------
# Name:        Problem 043.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from itertools import permutations

def HasSubStringProperty(s):
    primes = [2, 3, 5, 7, 11, 13, 17]

    for i in range(1, 8):
        if int(s[i:i+3]) % primes[i-1] != 0:
            return False

    return True

def main():
    answer = 0

    for x in permutations('0123456789'):
        s = ''.join(x)

        # Ignore leading zero's
        if s[0] == '0':
            continue

        if HasSubStringProperty(s):
            answer += int(s)

    print(answer)

if __name__ == '__main__':
    main()
