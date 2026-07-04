import sys

input = sys.stdin.readline

n = int(input().rstrip())
x = y = 1
plan = input().rstrip().split()


# 중요!! L, R, U, D에 따른 이동방향 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for action in plan:
    for i in range(len(move_types)):
        if action == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)