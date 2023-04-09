#-------------------------------------------------------------------------------
# Name:        Helper.py
#
# Purpose:     To define a useful script full of tips, tricks and usefull
#              functions to create a common code base
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from datetime import datetime
from re import sub
from math import log10, floor

# //////////////////////////////////////////////////////////////////////////////
# Lists
# //////////////////////////////////////////////////////////////////////////////

def product(seq = None):
    tmp = 1
    for element in seq:
        tmp *= element
    return tmp

def shift_index(index, stride, seq = None):
    size = len(seq)
    index = size + stride
    while(index > size):
        index -= size
    return index

def shift_seq(stride, seq = None):
    shiftedSeq = []
    for i in range(len(seq)):
        shiftedSeq.append(seq[(i-stride) % len(seq)])
    return shiftedSeq

#from collections import Counter

    # Counters version
    # counter = Counter(seq)
    # for number in seq:
    #     if counter[number] > 1:
    #         return False
    # return True

# //////////////////////////////////////////////////////////////////////////////
# Utility
# //////////////////////////////////////////////////////////////////////////////

def time_function(func):
    start = datetime.now()
    func()
    end =  datetime.now()
    return end - start

def is_permutation(x, y):
    a, b = x, y
    if isinstance(a, int):
        a, b = str(x), str(y)

    return ''.join(sorted(a)) == ''.join(sorted(b))

def is_palindrome(x):
    s = x
    if isinstance(s, int):
        s = str(x)

    return s == s[::-1]

# Checks for palindromes in language. For example, "Madam, in Eden I'm Adam" is
# a palindrome even though it has punctuation.
def is_language_palindrome(p):
    s = p
    # Take out anything that isn't a-z or A-Z
    s = sub('[^a-zA-Z]+', '', s)
    # Make all charcaters into the same case for comparison
    s = s.lower()

    return s == s[::-1]

def sum_of_digits(n):
    return sum(int(c) for c in str(n))

def sum_in_range(n):
    return int((n + 1) * (n/2))
    #return (n * (n + 1)) // 2

def length_of_number(n):
    return int(floor(log10(n)) + 1)

def is_pandigital(x, allowZero = False):
    compareStr = ''
    numberStr = ''.join(sorted(str(x)))
    length = len(numberStr)

    # Will we allow zero? e.g. is 20134 pandigital?
    if allowZero:
        compareStr = ''.join([str(i) for i in range(0, length)])
    else:
        compareStr = ''.join([str(i) for i in range(1, length+1)])

    return numberStr == compareStr
