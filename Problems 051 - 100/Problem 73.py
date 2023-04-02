#-------------------------------------------------------------------------------
# Name:        Problem 71
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

# Slow for a very big number
def FareySequenceGenerator(n):
    a, b, c, d = 0, 1, 1, n
    yield(a, b)

    while c <= n:
        k = int((n + b) / d)
        a, b, c, d = c, d, k * c - a, k * d - b
        yield(a, b)

def main():
    counting = False
    count = 0

    for fraction in FareySequenceGenerator(12000):
        if fraction == (1, 3):
            counting = True
        if fraction == (1, 2):
            break

        if counting:
            count += 1

    print(count-1)

if __name__ == '__main__':
    main()
