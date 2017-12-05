def solvecaptcha1(input):
	solution = 0
	input = str(input)
	for i in xrange(len(input)):
		left = input[i]
		right = input[(i + 1) % len(input)]
		if left == right:
			solution += int(left)
	return solution

def solvecaptcha2(input):
	solution = 0
	input = str(input)
	offset = len(input) / 2
	for i in xrange(len(input)):
		left = input[i]
		right = input[(i + offset) % len(input)]
		if left == right:
			solution += int(left)
	return solution

if __name__ == '__main__':
	print solvecaptcha2(open('day01/input.txt').read().strip())