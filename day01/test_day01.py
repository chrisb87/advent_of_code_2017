import unittest
from day01 import *

class TestDay1Part1(unittest.TestCase):
	def test_solve_examples(self):
		self.assertEqual(solvecaptcha(1122), 3)
		self.assertEqual(solvecaptcha(1111), 4)
		self.assertEqual(solvecaptcha(1234), 0)
		self.assertEqual(solvecaptcha(91212129), 9)
