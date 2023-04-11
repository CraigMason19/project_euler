#-------------------------------------------------------------------------------
# Name:        problem_102.py
#
# Notes:
#
# Links:       http://www.blackpawn.com/texts/pointinpoly/default.html
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('Helper')

from vector2 import Vector2, dot

# Simple class containing 3 2D-Vectors
class Triangle:
    def __init__(self, l):
        self.mA = Vector2(l[0], l[1])
        self.mB = Vector2(l[2], l[3])
        self.mC = Vector2(l[4], l[5])

    def __str__(self):
        return str(self.mA) + str(self.mB) + str(self.mC)

    def __repr__(self):
        return str(self.mA) + str(self.mB) + str(self.mC)

# Returns true if a point is inside a triangle
def TriangleContainsPoint(t, p):
    t.mA.normalise()
    t.mB.normalise()
    t.mC.normalise()
    p.normalise()

    # Compute vectors
    v0 = t.mC - t.mA
    v1 = t.mB - t.mA
    v2 = p - t.mA

    # Compute dot products
    dot00 = dot(v0, v0)
    dot01 = dot(v0, v1)
    dot02 = dot(v0, v2)
    dot11 = dot(v1, v1)
    dot12 = dot(v1, v2)

    # Compute barycentric coordinates
    invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom

    # Check if point is in triangle
    return (u > 0) and (v > 0) and (u + v < 1)


def main(print_info=False):
    origin = Vector2(0.0, 0.0)
    answer = 0

    File = open("./Problems 101 - 150/triangles.txt")
    for line in File:
        t = Triangle([int(n) for n in line.split(",")])
        if TriangleContainsPoint(t, origin):
            answer += 1

    if print_info:
        print(answer)

    return answer
    
if __name__ == '__main__':
    main(print_info=True)
