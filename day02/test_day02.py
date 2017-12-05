import unittest
from day02 import *

class TestDay2Part1(unittest.TestCase):
	def test_solve_example(self):
		self.assertEqual(checksum1('day02/testinput.txt'), 18)

	def test_solve_actual(self):
		self.assertEqual(checksum1('day02/input.txt'), 37923)

class TestDay2Part2(unittest.TestCase):
	def test_solve_example(self):
		self.assertEqual(checksum2('day02/testinput2.txt'), 9)

	def test_solve_actual(self):
		self.assertEqual(checksum2('day02/input.txt'), 263)
