import time
import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())

start_time = time.time()

result = n - ((n//k)*k)
n = (n//k)*k
while n != 1:
    n //= k
    result += 1

print(result)

end_time = time.time()

print(end_time - start_time)