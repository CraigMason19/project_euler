#-------------------------------------------------------------------------------
# Name:        Problem 022.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

def main():
    with open("p022_names.txt") as f:
        # Read all the data in the file, replace all quotation marks with
        # nothing and split into a list
        data = f.read().replace('"', '').split(",")

    data.sort()

    answer = 0
    for i, name in enumerate(data):
        # A (upper case) is in ASCII poition 65
        alphabetScore = sum(ord(char) - 64 for char in name)
        positionScore = i+1
        nameScore = alphabetScore * positionScore
        answer += nameScore

    print(answer)

if __name__ == '__main__':
    main()