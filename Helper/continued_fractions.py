#-------------------------------------------------------------------------------
# Name:        ContinuedFractions.py
#
# Links:       http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#section9.4
#              http://www.millersville.edu/~bikenaga/number-theory/continued-fractions/continued-fractions.html
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from math import sqrt, floor

class ContinuedFraction:
    def __init__(self):
        self.startOfSeq = 0
        self.repeatedSeq = []
        self.data = None

    def CreateFromList(self, seq):
        self.data = seq
        self.startOfSeq = seq[0]
        self.repeatedSeq = seq[1:]
        self.period = len(self.repeatedSeq)

    def CreateFromSquare(self, square):
        self.data = square

        a0 = int(floor(sqrt(self.data)))
        self.startOfSeq = a0

        # Algorithm from continued fractions page on wikipedia
        m, d, a = 0, 1, a0

        while a != 2 * a0:
            m1 = d * a - m
            d1 = int((self.data - m1 * m1) / d)
            a1 = (a0 + m1) / d1
            a1 = int(floor(a1))
            self.repeatedSeq.append(a1)

            m, d, a = m1, d1, a1

        self.period = len(self.repeatedSeq)

    def CreateFromRational(self, numerator, denominator):
        self.data = (numerator, denominator)
        l = []

        # Invert our fraction because the first step of our recurring algorithm
        # is to invert the fraction, it ensures we can just use 1 while loop
        # e.g.
        # 17/47 ->
        # 47/17 = 2 + 13/17 ->
        # 17/13 = 1 + 4/13 ->
        # 13/4 = 3 + 1/4 ->
        # 4/1
        f2 = (denominator, numerator)
        while True:
            f1 = (f2[1], f2[0])
            divisor, remainder = divmod(f1[0], f1[1])

            # Eventually the divisor will be 1 and as 1 is a divisor of all numbers,
            # there will be no remainders. So the continued fraction is over
            if remainder == 0:
                l.append(divisor)
                break

            l.append(divisor)
            f2 = (remainder, f1[1])

        self.startOfSeq = l[0]
        self.repeatedSeq = l[1:]
        self.period = len(self.repeatedSeq)

    def __repr__(self):
        if isinstance(self.data, tuple):
            return "ContinuedFraction%s" % (self.data,)

        if isinstance(self.data, list):
            return "ContinuedFraction(%s)" % (self.data)

        return "ContinuedFraction(%d)" % (self.data)

    # For example, sqrt 23 = [4;(1,3,1,8)]
    def __str__(self):
        # Convert list to tuple, this means the string conversion uses
        # parentheses not square brackets
        if len(self.repeatedSeq) > 1:
            seqStr = str(tuple(self.repeatedSeq))
        else:
            seqStr = "(%d)" % self.repeatedSeq[0]
        # Compact the repeated sequence
        seqStr = seqStr.replace(" ", "")
        return "[%d;%s]" % (self.startOfSeq, seqStr)

    def ConvergentsGenerator(self):
        # Will need to store current, previous and previous previous values of
        # n and d
        n2, n1, n = 1, 0, 0
        d2, d1, d = 0, 0, 0

        # a is the non repeating part of the sequence
        # e.g. sqrt(7) = [2;1,1,1,4], a = 2
        a = self.startOfSeq
        n1 = a
        d1 = 1
        yield n1, d1

        # b is the first part of the repeating sequence
        # e.g. sqrt(7) = [2;1,1,1,4], b = 1
        b = self.repeatedSeq[0]
        n = b * n1 + n2
        d = b * d1 + d2
        yield n, d

        # Need to calculate a + b first. So we start at the second part of the
        # repeating sequence
        # e.g. sqrt(7) = [2;1,1,1,4], c = 1
        index =  1

        while True:
            # Restart the repeated pattern
            if(index == len(self.repeatedSeq)):
                index = 0

            # Shift the values on n and d down the imaginary columns
            n2, n1 = n1, n
            d2, d1 = d1, d

            # We have precalculated a and b (previous two terms) so now we can
            # start looping over the rest of the sequence
            c = self.repeatedSeq[index]

            # e.g. n = c * previous + previous previous
            n = c * n1 + n2
            d = c * d1 + d2
            yield n, d

            # Shift the values on a and b down the imaginary columns
            a, b = b, c
            index += 1
