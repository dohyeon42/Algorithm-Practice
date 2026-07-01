import time

n, m = map(int, input().split())

start_time = time.time()
# for i in range(n):
#     result.append(list(map(int, input().split())))
result = [list(map(int, input().split())) for i in range(n)]

result = max([min(result[i]) for i in range(n)])

print(result)
end_time = time.time()
print(f"작동 시간 : {end_time - start_time}")
