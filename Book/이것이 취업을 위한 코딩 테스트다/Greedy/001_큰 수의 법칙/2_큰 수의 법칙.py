import time

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

# 시간 측정 시작
start_time = time.time()

array.sort()

# 가장 큰 수가 더해지는 횟수
count = (m//(k+1)) * k
count += m % (k+1)

result = 0
result += count * array[n-1]
result += (m - count) * array[n-2]

print(result)

# 시간 측정 종료
end_time = time.time()
print(f"작동 시간 : {end_time - start_time}")