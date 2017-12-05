import unittest
from day01 import *

class TestDay1Part1(unittest.TestCase):
	def test_solve_examples(self):
		self.assertEqual(solvecaptcha1(1122), 3)
		self.assertEqual(solvecaptcha1(1111), 4)
		self.assertEqual(solvecaptcha1(1234), 0)

class TestDay1Part2(unittest.TestCase):
	def test_solve_examples(self):
		self.assertEqual(solvecaptcha2(1212), 6)
		self.assertEqual(solvecaptcha2(1221), 0)
		self.assertEqual(solvecaptcha2(123425), 4)
		self.assertEqual(solvecaptcha2(123123), 12)
		self.assertEqual(solvecaptcha2(12131415), 4)
