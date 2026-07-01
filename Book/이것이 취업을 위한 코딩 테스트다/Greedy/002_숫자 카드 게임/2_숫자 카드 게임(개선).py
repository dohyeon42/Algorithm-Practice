import time
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# for i in range(n):
#     result.append(list(map(int, input().split())))
result = [list(map(int, input().split())) for i in range(n)]

start_time = time.time()
result = max(min(data) for data in result)

print(result)
end_time = time.time()
print(f"작동 시간 : {end_time - start_time}")