import sys

input = sys.stdin.readline

n = int(input().rstrip())
plan = list(input().rstrip().split())

result = [1, 1]

for action in plan:
	if action == 'L':
		if result[1] == 1:
			continue
		else:
			result[1] -= 1
	elif action == 'R':
		if result[1] == n:
			continue
		else:
			result[1] += 1
	elif action == 'U':
		if result[0] == 1:
			continue
		else:
			result[0] -= 1
	else:
		if result[0] == n:
			continue
		else:
			result[0] += 1
print(' '.join(map(str, result)))