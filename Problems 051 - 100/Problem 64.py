#-------------------------------------------------------------------------------
# Name:        Problem 64
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from math import sqrt, floor

class ContinuedFraction:
    def __init__(self, square):
        self.square = square
        self.repeatedSeq = []

        a0 = int(floor(sqrt(self.square)))
        self.startOfSeq = a0

        # Algorithm from wikipedia
        m, d, a = 0, 1, a0

        while a != 2 * a0:
            m1 = d * a - m
            d1 = int((self.square - m1 * m1) / d)
            a1 = (a0 + m1) / d1
            a1 = int(floor(a1))
            self.repeatedSeq.append(a1)

            m, d, a = m1, d1, a1

        self.period = len(self.repeatedSeq)

    def __repr__(self):
        return "ContinuedFraction(%d)" % (self.sqaure)

    # For example, âˆš23 = [4;(1,3,1,8)]
    def __str__(self):
        # Convert list to tuple, this means the string conversion uses
        # parentheses not square brackets
        if len(self.repeatedSeq) > 1:
            seqStr = str(tuple(self.repeatedSeq))
        else:
            seqStr = "(%d)" % self.repeatedSeq[0]
        seqStr = seqStr.replace(" ", "")
        return "[%d;%s]" % (self.startOfSeq, seqStr)

def main():
    limit, answer = 10**4, 0

    for square in range(2, limit+1):
        # No need to check perfect squares
        if sqrt(square).is_integer():
            continue
        else:
            cf = ContinuedFraction(square)
            print("sqrt(%d) = %s" % (square, cf))
            # Does it have an odd peroid?
            if cf.period % 2 != 0:
                answer += 1

    print(answer, "Odd periods")

if __name__ == '__main__':
    main()
