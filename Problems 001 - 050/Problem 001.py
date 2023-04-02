#-------------------------------------------------------------------------------
# Name:        Problem 001
#
# Links:
#
# Notes:       "The longest journey begins with a single step" - Lao Tsu
#
# TODO:
#-------------------------------------------------------------------------------

def main():
    answer = sum(n for n in range(3, 10**3) if n%5 == 0 or n%3 == 0)
    print(answer)

if __name__ == '__main__':
    main()