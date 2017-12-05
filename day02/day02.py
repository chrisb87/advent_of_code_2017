import re
from pdb import set_trace

def checksum(inputfile):
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

if __name__ == '__main__':
	print checksum('day02/input.txt')
