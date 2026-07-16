import sys

def n_input():
	return sys.stdin.readline().rstrip()
	
n, m = map(int, n_input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, n_input())))
	
def dfs(x, y):
	if not (0 <= x < n and 0 <= y < m) or graph[x][y] != 0:
		return 0 
	if graph[x][y] == 0:
		graph[x][y] = 1
		dfs(x+1, y)
		dfs(x-1, y)
		dfs(x, y+1)
		dfs(x, y-1)
		return 1

count = 0

for i in range(n):
	for j in range(m):
		count += dfs(i, j)

print(count)