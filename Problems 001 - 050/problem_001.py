#-------------------------------------------------------------------------------
# Name:        problem_001.py
#
# Links:
#
# Notes:       "The longest journey begins with a single step" - Lao Tsu
#
# TODO:
#-------------------------------------------------------------------------------

def main(print_info=False):
    answer = sum(n for n in range(3, 10**3) if n % 5 == 0 or n % 3 == 0)

    if print_info:
        print(answer)

    return answer

if __name__ == '__main__':
    main(print_info=True)