import sys

if len(sys.argv) < 2:
	print("Usage: python3", sys.argv[0], "input.txt")
	exit(1)

data = [sum(int(j) for j in i.split("\n")) for i in open(sys.argv[1]).read().rstrip().split("\n\n")]
print("max: ", max(data))
data.sort(reverse=True)
print("top three:", sum(data[:3]))
