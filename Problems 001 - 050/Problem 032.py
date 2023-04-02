#-------------------------------------------------------------------------------
# Name:        Problem 032.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

def IsPandigital(x, y):
    s = str(x) + str(y) + str(x*y)
    return (''.join(sorted(s)) == '123456789')

def main():
    d = {}

    for x in range(1, 99):
        for y in range(1, 10000):
            if IsPandigital(x, y):
                d[x*y] = "%d x %d" % (x, y)

    answer = 0
    for k,v in d.items():
        print(v, " = ", k)
        answer += k

    print(answer)

if __name__ == '__main__':
    main()

