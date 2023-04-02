#-------------------------------------------------------------------------------
# Name:        Problem 094
#
# Links:       https://oeis.org/A120893
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from math import sqrt

def NextSideGenerator():
    # The first 2 sides are invalid for this problem but we need them to work
    # out the other sides
    # 1 -> 1,1,0 -> last side is not integral
    # 1 -> 1,1,2 -> area is not integral
    side = [1, 1, 5]
    index = len(side)
    yield side[-1]

    while True:
        # Algorithm from OEIS
        side.append(3*side[index-1] + 3*side[index-2] - side[index-3])
        index = len(side)
        yield side[-1]

# Area of a Heronian triangle
def Area(a, b, c):
    halfP = (a + b + c) / 2
    return sqrt(halfP * (halfP-a) * (halfP-b) * (halfP-c))

def main():
    nsg = NextSideGenerator()
    perimeter = 0

    while True:
        side = next(nsg)

        if side*3 > 10**9:
            break

        # The last side must be +- 1
        tmp = Area(side, side, side - 1)
        if(tmp.is_integer()):
            perimeter += side + side + side-1
            #print(side, side, side-1, tmp)
            continue

        tmp = Area(side, side, side + 1)
        if(tmp.is_integer()):
            perimeter += side + side + side+1
            #print(side, side, side+1, tmp)

    print(perimeter)

if __name__ == '__main__':
    main()
