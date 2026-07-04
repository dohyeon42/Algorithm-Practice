import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())

result = n - ((n//k)*k)
n = (n//k)*k
while n != 1:
    n //= k
    result += 1

print(result)