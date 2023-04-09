#-------------------------------------------------------------------------------
# Name:        Problem 108
#
# Links:       http://en.wikipedia.org/wiki/Highly_composite_number
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from fractions import Fraction

# We can rearrange and solve the equation and solve for 2 variables (x and n)
# a + b = c --> b = c - a
# 1/x + 1/y = 1/n --> 1/y = 1/n - 1/x
def SolveForUnknownFraction(n, x):
    return Fraction(1, n) - Fraction(1, x)

# There will always be the same 2 solutions for each number. If a number is prime
# it will only have these, other numbers will have these plus others. Other
# solutions will be in this range
#
# The two solutions are:
# 1/n+1 + 1/y = 1/n
# 1/2n + 1/2n = 1/n
#
# For example:
# 67 is prime and therefore has 2 solutions
# 1/68 + 1/y = 1/67 (y = 4556)
# 1/134 + 1/134 = 1/67
#
# So look between these for all other solutions
def SolutionsCount(n):
    answer = 0
    for x in range(n+1, (n*2)+1):
        f = SolveForUnknownFraction(n, x)
        if f.numerator == 1:
            answer += 1

    return answer

# Lets get some data to play with.
# Biggest solution count below 10 = 6 (5 solutions)
# Biggest solution count below 100 = 60 (23 solutions)
# Biggest solution count below 1000 = 840 (95 solutions)
# 6 has prime factors of [2, 3] 60 has prime factors [2^2, 3, 5] 840 has prime
# factors [2^3, 3, 5, 7]
# We can see that we need highly composite numbers so i basically guessed various
# combinations along that theme
#
# [2, 3, 5, 7, 11, 13] = 30030 (365 solutions)
# [2, 3, 5, 7, 11, 13, 17] = 510510 (1094 solutions)
# having found this is not the solution, we need to be bigger than our first
# guess but lower than the second. So we need to use exponents
# [2^2, 3, 5, 7, 11, 13] = 60060 (608 solutions)
# [2^3, 3, 5, 7, 11, 13] = 120120 (851 solutions)
# [2^4, 3, 5, 7, 11, 13] = 240240 (1094 solutions)
# too big
# [2, 3^2, 5, 7, 11, 13] = 90090 (608 solutions)
# [2^2, 3^2, 5, 7, 11, 13] = 180180 (1013 solutions)
# Eureka!
def main():
    print(SolutionsCount(180180))

if __name__ == '__main__':
    main()
