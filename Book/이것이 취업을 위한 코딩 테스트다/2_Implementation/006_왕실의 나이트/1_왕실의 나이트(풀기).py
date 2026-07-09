n = input()

altonu = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5,
	'f': 6,
	'g': 7,
	'h': 8
}

n = [altonu[n[0]], int(n[1])]

actions = [
	[1, -2], 
	[2, -1], 
	[2, 1], 
	[1, 2], 
	[-1, 2], 
	[-2, 1], 
	[-2, -1], 
	[-1, -2]
]

result = 0

for action in actions:
	if 1 <= n[0]+action[0] <= 8 and 1 <= n[1]+action[1] <= 8:
		result += 1

print(result)