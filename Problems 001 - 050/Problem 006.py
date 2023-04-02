#-------------------------------------------------------------------------------
# Name:        Problem 006.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

def main():
    sumOfSquares, squareOfSums = 0, 0

    for n in range(1, 100+1):
        sumOfSquares += n*n
        squareOfSums += n
    squareOfSums *= squareOfSums

    print(squareOfSums - sumOfSquares)

if __name__ == '__main__':
    main()
