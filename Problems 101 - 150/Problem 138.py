#-------------------------------------------------------------------------------
# Name:        Problem 138
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from math import sqrt

class Triangle:
    def __init__(self, base):
        self.base = base
        self.h = 0
        self.leg = 0
        self.special = False
        if base > 1:
            self.CalculateHeight()

    def CalculateHeight(self):
        halfBase = int(self.base/2)
        estimateHeights = [self.base - 1, self.base + 1]

        for h in estimateHeights:
            result = sqrt(h*h + halfBase*halfBase)
            if float(result).is_integer():
                self.h = h
                self.leg = result
                self.special = True
                break

    def __str__(self):
        return "(%d, %d, %d, %s)" % (self.base, self.leg, self.h, self.special)

    def __repr__(self):
        return "Triangle(%d, %d)" % (self.base, self.leg)

def main():
    triangles = []

    for i in range(2, 20**6, 2):
        t = Triangle(i)
        if t.special:
            triangles.append(t)

    print(triangles)





    s = [17, 305, 5473, 98209, 1762289, 31622993, 567451585, 10182505537, 182717648081, 3278735159921, 58834515230497, 1055742538989025]
    print(sum(s))



if __name__ == '__main__':
    main()
