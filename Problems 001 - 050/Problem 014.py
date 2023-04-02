#-------------------------------------------------------------------------------
# Name:        Problem 014.py
#
# Notes:
#
# Links:
#
# TODO:         add lookup table
#-------------------------------------------------------------------------------

mem = dict()

def CollatzSequenceLength(n):
    current, length = n, 1

    while True:
        if current == 1:
            break

        # If even, half it
        if current%2 == 0:
            current = int(current / 2)
        # If odd, times by 3 and add 1
        else:
            current = (3 * current) + 1
        length += 1

    return length


def main():
    answer, longestLength = 0, 0
    for i in range(2, 10**6):
        tmp = CollatzSequenceLength(i)
        if tmp > longestLength:
            answer, longestLength = i, tmp

    print(answer)

if __name__ == '__main__':
    main()



