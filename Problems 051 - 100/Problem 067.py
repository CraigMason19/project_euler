#-------------------------------------------------------------------------------
# Name:        Problem 067.py
#
# Notes:       Modified version of Problem 018
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

def LoadTriangleFromFile(name):
    l = []

    with open(name) as file:
        for line in file:
            l.append([int(n) for n in line.split(" ")])

    return l

def main():
    # Work backwords (from the bottom)
    triangle = LoadTriangleFromFile("triangle.txt")
    maxRows = len(triangle)

    for r in range(maxRows-1, 1, -1):
        for n in range(0, len(triangle[r-1])):
            triangle[r-1][n] += max(triangle[r][n], triangle[r][n+1])

    print(triangle[0][0] + max(triangle[1]))

if __name__ == '__main__':
    main()







