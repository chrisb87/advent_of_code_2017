import unittest
from day02 import *

class TestDay1Part1(unittest.TestCase):
	def test_solve_example(self):
		self.assertEqual(checksum('day02/testinput.txt'), 18)

	def test_solve_actual(self):
		self.assertEqual(checksum('day02/input.txt'), 37923)
