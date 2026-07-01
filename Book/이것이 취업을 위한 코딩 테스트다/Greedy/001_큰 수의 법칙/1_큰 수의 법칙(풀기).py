import time

n, m, k = map(int, input().split())
array = list(map(int, input().split()))
result = 0

# 시간 측정 시작
start_time = time.time()

array.sort(reverse = True)
while m:
    result += array[0]*k
    m -= k
    if not m:
        break;
    result += array[1]
    m -= 1
print(result)

# 시간 측정 종료
end_time = time.time()
print(f"작동 시간 : {end_time - start_time}")