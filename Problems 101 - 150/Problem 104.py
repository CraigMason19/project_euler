#-------------------------------------------------------------------------------
# Name:        Problem 104.py
#
# Notes:
#
# Links:
#
# TODO:        Add mul, sub, div and other methods to IntegerRight
#-------------------------------------------------------------------------------

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
# 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...

import sys
sys.path.append('Helper')

from general import is_pandigital
from fibonacci import first_digits_of_fib

class IntegerRight:
    """ A class represting part of an larger integer on it's right side (last
        few digits). Digits will never grow bigger than the size defined in the
        constructor """
    def __init__(self, size, n=0):
        self.digits = "0" * size
        self.size = size
        self.__iadd__(n)

    def __add__(self, other):
        return self.__iadd__(other)

    # += operator
    def __iadd__(self, other):
        tmp = 0

        if isinstance(other, int):
            # only use the last few digits if it is a large number
            tmp = int(self.digits) + int(str(other)[-self.size:])

        if isinstance(other, IntegerRight):
            tmp = int(self.digits) + other.AsInt()

        # The result may be bigger than the digit size. e.g. 999 + 999 = 1998
        self.digits = str(tmp)[-self.size:]
        # zfill pads the string with zeros from the left until it is the correct
        # width. As this is part of a number leading 0's may be significant.
        self.digits = self.digits.zfill(self.size)
        return self

    def AsInt(self):
        return int(self.digits)

    def __str__(self):
        return self.digits

    def __repr__(self):
        return "IntegerRight(%s)" % (self.digits)
        pass

def main():
    # Start at 0, 1
    frA, frB = IntegerRight(9), IntegerRight(9, 1)

    counter = 0
    while True:
        frA, frB = frB, frA + frB
        counter += 1
        if is_pandigital(frA):
            if is_pandigital(first_digits_of_fib(counter, 9)):
                print(counter)
                break

if __name__ == '__main__':
    main()
