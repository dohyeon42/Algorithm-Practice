import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# for i in range(n):
#     result.append(list(map(int, input().split())))
result = [list(map(int, input().split())) for i in range(n)]
result = max(min(data) for data in result)

print(result)