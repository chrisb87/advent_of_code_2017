import re
from itertools import combinations
from pdb import set_trace

def checksum1(inputfile):
	total = 0
	text = open(inputfile).read().strip()
	for line in text.split('\n'):
		cells = [int(val) for val in re.split(r'\s+', line)]
		min = max = cells[0]
		for cell in cells:
			if cell < min:
				min = cell
			if cell > max:
				max = cell
		total += max - min
	return total

def checksum2(inputfile):
	total = 0
	text = open(inputfile).read().strip()
	for line in text.split('\n'):
		cells = [int(val) for val in re.split(r'\s+', line)]
		for c1, c2 in combinations(cells, 2):
			a, b = sorted([c1, c2])
			if (float(b) / float(a)) % 1 == 0:
				total += b / a
				break
	return total


if __name__ == '__main__':
	print checksum('day02/testinput2.txt')
