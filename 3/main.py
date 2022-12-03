import sys

if len(sys.argv) < 2:
	print("Usage: python3", sys.argv[0], "input.txt")
	exit(1)

prios = {chr(i):(i-ord("a")+1) for i in range(ord("a"),ord("z")+1)}
prios |= {chr(i):(i-ord("A")+27) for i in range(ord("A"),ord("Z")+1)}

data = open(sys.argv[1]).read().rstrip().split("\n")

def part1(data):
	score = 0
	for i in data:
		dups = set(i[:len(i)//2]).intersection(i[len(i)//2:])
		for d in dups:
			score += prios[d]
	return score

print(part1(data))

def part2(data):
	score = 0
	for i in range(0,len(data),3):
		dups = set(data[i]).intersection(data[i+1]).intersection(data[i+2])
		for d in dups:
			score += prios[d]
	return score

print(part2(data))
