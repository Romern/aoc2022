import sys
from parse import parse

if len(sys.argv) < 2:
	print("Usage: python3", sys.argv[0], "input.txt")
	exit(1)

data = [parse("{:d}-{:d},{:d}-{:d}",i).fixed for i in open(sys.argv[1]).read().splitlines()]

def part1(data):
	count = 0
	for i1,i2,j1,j2 in data:
		if i1 >= j1 and i2 <= j2 or j1 >= i1 and j2 <= i2:
			count += 1
	return count

print(part1(data))

def part2(data):
	count = 0
	for i1,i2,j1,j2 in data:
		if i1 in range(j1,j2+1) or i2 in range(j1,j2+1) or j1 in range(i1,i2+1) or j2 in range(i1,i2+1):
			count += 1
	return count

print(part2(data))
