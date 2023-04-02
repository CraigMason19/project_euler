#-------------------------------------------------------------------------------
# Name:        Problem 030.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

def main():
    answer = 0
    for i in range(2, 10**6):
        tmp = sum(pow(int(c), 5) for c in str(i))
        if tmp == i:
            answer += tmp

    print(answer)

if __name__ == '__main__':
    main()




