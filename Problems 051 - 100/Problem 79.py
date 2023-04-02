#-------------------------------------------------------------------------------
# Name:        Problem 79.py
#
# Notes:       Assumes there are only unique numbers. Also assumes each part of
#              the password was entered at least once.
#              Did mainly by hand 73162890. 4 and 5 are never used, 7 is only in
#              the first row, 0 is only in the last row. 3 is never in a higher
#              position than 1 when they occur and 1 is never higher than 6
#              when they both occur etc...
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

ValidLogins = []
UsedDigits = None

def main():
    with open("keylog.txt", "r") as f:
        ValidLogins = f.read().split()

    # Find which numbers are in the password. (Has been entered in the file, an
    # assumption)
    UsedDigits = set()
    for login in ValidLogins:
        for c in str(login):
            UsedDigits.add(int(c))

    # Create sets for each number in the file, put them in a dictionary showing
    # which numbers come after them in the password.
    # e.g. {1 : 9 8 0 2 6) -> 1 therefore must be before 9 8 0 2 and 6
    successorsDict = dict()
    for num in UsedDigits:
        successorsDict[num] = set()

    # Find which numbers appear after other numbers and put those into a set
    for login in ValidLogins:
        digits = [int(c) for c in str(login)]
        successorsDict[digits[0]].add(digits[1]) # Column 2 follows column 1
        successorsDict[digits[0]].add(digits[2]) # Column 3 follows column 1
        successorsDict[digits[1]].add(digits[2]) # Column 3 follows column 2

    # The item with the most numbers in the set is the first number of the
    # password, the number with the least is the last one
    successorsDictSorted = sorted(successorsDict, key=successorsDict.get, reverse=True)
    Password = int(''.join(map(str, successorsDictSorted)))
    print(Password)

if __name__ == '__main__':
    main()
