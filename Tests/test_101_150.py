#-------------------------------------------------------------------------------
# Name:        test_101_150.py
#
# Links:
#
# Notes:       
#
# TODO:
#-------------------------------------------------------------------------------

import unittest

import sys
sys.path.append('Problems 101 - 150')

import problem_102

class TestProblems(unittest.TestCase):
    def test_problem_102(self):
        self.assertEqual(problem_102.main(), 228)



if __name__ == '__main__':
    unittest.main()