def solvecaptcha(input):
	solution = 0
	input = str(input)
	for i in xrange(len(input)):
		left = input[i]
		right = input[(i + 1) % len(input)]
		if left == right:
			solution += int(left)
	return solution

if __name__ == '__main__':
	print solvecaptcha(1111)
	print solvecaptcha(open('day01/input.txt').read().strip())