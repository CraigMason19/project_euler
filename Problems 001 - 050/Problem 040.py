#-------------------------------------------------------------------------------
# Name:        Problem 040
#
# Links:
#
# Notes:       1 * 1 * 5 * 3 * 7 * 2 * 1
#
# TODO:
#-------------------------------------------------------------------------------

def ChampernowneConstantGenerator():
    n = 1

    while(True):
        for c in str(n):
            yield int(c)

        n += 1

def main():
    ccg = ChampernowneConstantGenerator()
    answer, indices = 1, [1, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6]

    for i in range(1, 10**6+1):
        digit = next(ccg)
        if i in indices:
            answer *= digit

    print(answer)

if __name__ == '__main__':
    main()