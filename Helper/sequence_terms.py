#-------------------------------------------------------------------------------
# Name:        sequence_terms.py
#
# Purpose:     A collection of useful, common or easy to create sequences
#              created from terms
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

# https://oeis.org/A001318
def pentagonal(term):
    return term * (3 * term-1) // 2

# https://oeis.org/A000041
# Generalized pentagonal numbers are obtained from the same formula as
# pentagonal numbers but with n taking values in the sequence
# 0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5,...
def generalized_pentagonal(term):
    if term == 0:
        return term

    if term%2 == 0:
        return Pentagonal(-(term // 2))

    return Pentagonal((term + 1) // 2)