import sys

if len(sys.argv) < 2:
	print("Usage: python3", sys.argv[0], "input.txt")
	exit(1)

#A Rock     --> Paper    Y
#B paper    --> Scissors Z
#C scissors --> Rock     X

score_map_part1 = {
	("A", "X"): 1 + 3,
	("B", "X"): 1 + 0,
	("C", "X"): 1 + 6,
	("A", "Y"): 2 + 6,
	("B", "Y"): 2 + 3,
	("C", "Y"): 2 + 0,
	("A", "Z"): 3 + 0,
	("B", "Z"): 3 + 6,
	("C", "Z"): 3 + 3
}

data = [tuple(i.split(" ")) for i in  open(sys.argv[1]).read().rstrip().split("\n")]

def calc_score_part1(data):
	return sum(score_map_part1[i] for i in data)

print(calc_score_part1(data))

score_map_part2 = {
	("A", "X"): 3 + 0,
	("B", "X"): 1 + 0,
	("C", "X"): 2 + 0,
	("A", "Y"): 1 + 3,
	("B", "Y"): 2 + 3,
	("C", "Y"): 3 + 3,
	("A", "Z"): 2 + 6,
	("B", "Z"): 3 + 6,
	("C", "Z"): 1 + 6
}

def calc_score_part2(data):
	return sum(score_map_part2[i] for i in data)
print(calc_score_part2(data))
