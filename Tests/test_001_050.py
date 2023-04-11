#-------------------------------------------------------------------------------
# Name:        test_001_050.py
#
# Links:
#
# Notes:        
#
# TODO:
#-------------------------------------------------------------------------------

import unittest

import sys
sys.path.append('Problems 001 - 050')

import problem_001
import problem_002

class TestProblems(unittest.TestCase):
    def test_problem_001(self):
        self.assertEqual(problem_001.main(), 233168)

    def test_problem_002(self):
        self.assertEqual(problem_002.main(), 4613732)

if __name__ == '__main__':
    unittest.main()