import sys

def new_input():
	return sys.stdin.readline().rstrip().split()

N, M = map(int, new_input())
x, y, d = map(int, new_input())
world = []
for _ in range(N):
	world.append(list(map(int, new_input())))
visit = [[0]*M for _ in range(N)]
visit[x][y] = 1
turn_time = 0
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
count = 0

def turn_left():
	global d
	d -= 1
	if d == -1:
		d = 3

while True:
	turn_left()
	nx, ny = x+dx[d], y+dy[d]
	if world[nx][ny] + visit[nx][ny] == 0:
		x, y = nx, ny
		turn_time = 0
		visit[x][y] = 1
	else:
		turn_time += 1
	if turn_time == 4:
		nx, ny = x-dx[d], y-dy[d]
		if world[nx][ny] == 0:
			x, y = nx, ny
			turn_time = 0
		else:
			break
	
for l in visit:
	count += l.count(1)
print(count)
