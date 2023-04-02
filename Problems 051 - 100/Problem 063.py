#-------------------------------------------------------------------------------
# Name:        Problem 063
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

def main():
    answer = 0

    for base in range(1, 100):
        for exponent in range(1, 100):
            tmp = base ** exponent
            if len(str(tmp)) == exponent:
                print(base, " ^ ", exponent, tmp)
                answer += 1

    print(answer)

if __name__ == '__main__':
    main()



